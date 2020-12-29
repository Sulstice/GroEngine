#!/usr/bin/env python3
#
# GroEngine Package
#
# ---------------

# Authentication to Apollo

class GroEngine(object):

    __version__ = '0.0.1'

    def __init__(self, target_directory, target_trajectory, username = None, hostname = None):

        '''

        Initialize to find the target logs and readers

        '''

        if username == None and hostname == None:
            self.user, self.hostname = self._read_authentication()
        else:
            self.user = username
            self.hostname = hostname

        self.target_directory = target_directory
        self.target_trajectory = target_trajectory
        self.file_paths = []

    def _read_authentication(self):


        """

        Read in the authentication file into apollo


        """

        from ruamel.yaml import YAML
        yaml = YAML()

        import os

        cwd = os.path.dirname(os.path.abspath(__file__))

        with open(os.path.join(cwd, 'auth_apollo.yml')) as auth_file:

            try:
                auth_info = yaml.load(auth_file)
            except Exception as exc:
                print('Problems handling in reading in the authentication file')


        user = auth_info['username']
        hostname = auth_info['host']

        return user, hostname

    def _collect_file_paths(self):

        '''

        This function will collect the file paths necessary for the transferring of data

        '''

        from fabric.connection import Connection

        with Connection(self.hostname, self.user) as portal:

            # Find the file paths
            file_paths_stream = portal.run('find ' + self.target_directory + ' -type f -name "' + self.target_trajectory + '"', hide=True)
            file_paths = file_paths_stream.stdout.strip().split('\n')

            portal.close()

        return file_paths



    def transfer_files(self, target_directory):

        """

        This function will fetch GROMACS files necessary for rewrapping of trajectories
        
        File list is as needed:
            
            tpr (topology)
            ndx (indexing files of the group)
            xtc (trajectory file)

        """

        self.file_paths = self._collect_file_paths()

        for file_path in self.file_paths:

            # Fetch the file paths in question and get ready for transfer
            import os
            head, tail = os.path.split(file_path)
            
            # Create the directories in your root machine
            import subprocess
            data_path = os.path.join(target_directory, head)
            dir_creation_process = subprocess.Popen('mkdir -p ' + data_path, shell=True)
            dir_creation_process.wait()
            
            # Fetch Trajectory File
            start = self.user + '@' + self.hostname + ':~/' + file_path
            end = os.path.join('./', data_path, tail)
            fetch_trajectory = subprocess.Popen('rsync -v ' + start + ' ' + end, shell=True)
            fetch_trajectory.wait()
            
            # Fetch Index File
            start = self.user + '@' + self.hostname + ':~/' + head + '/index.ndx'  
            end = os.path.join('./', data_path, 'index.ndx')
            fetch_index = subprocess.Popen('rsync -v ' + start + ' ' + end, shell=True)
            fetch_index.wait()
                
            # Fetch Topology File
            start = self.user + '@' + self.hostname + ':~/' + head + '/md_3.tpr'  
            end = os.path.join('./', data_path, 'md_3.tpr')
            fetch_topology = subprocess.Popen('rsync -v ' + start + ' ' + end, shell=True)
            fetch_topology.wait()
            
            
    def rewrap_trajectories(self, target_directory):
        
        '''
        
        This function will handle the bulk rewrapping of the trajectories synchronously 
        
        '''
        
        self.file_paths = self._collect_file_paths()
        
        for file_path in self.file_paths:

            # Fetch the file paths in question and get ready for transfer
            import os
            head, tail = os.path.split(file_path)
            
            # Create the directories in your root machine
            import subprocess
            data_path = os.path.join(target_directory, head)
            tail = 'concatenated.xtc'
            trajectory = os.path.join('./', data_path, tail)
            topology = os.path.join('./', data_path, 'md_3.tpr')
            index = os.path.join('./', data_path, 'index.ndx')
            outfile = os.path.join('./', data_path, 'md_3_wrapped_nowater.xtc')
            
            gromacs_rewrap = subprocess.Popen('gmx trjconv -f ' + trajectory + \
                                              ' -s ' + topology + ' -n ' + index + \
                                              ' -pbc mol -o ' + outfile,
                                              shell=True,
                                              universal_newlines=True,
                                              stdin=subprocess.PIPE)
            gromacs_rewrap.communicate(input='2')
            gromacs_rewrap.wait()
