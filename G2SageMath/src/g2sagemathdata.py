"""
Created on Sep 4, 2013

@author: tharindurusira
"""
#############################################################################
#       Copyright (C) 2013 Tharindu Rusira <tharindurusira@gmail.com>
#  Distributed under the terms of the GNU General Public License (GPL)
#  The full text of the GPL is available at:
#                  http://www.gnu.org/licenses/
#############################################################################

from sys import platform as _userplatform
import subprocess
import sys,os
import glob
import readline
from subprocess import CalledProcessError


class DataHandler(object):
    """
        This class includes methods to handle a data file
        and methods to access Sage
    """
       
    def download_csv(self,data_arg):
        
        """
        This method takes an argument(a list) and downloads the specified file
        ( after converting to .csv format)to a system specific temporary location.
        
        Input argument is resolved as follows 
            data_arg[0] --> gdata.Spreadsheet.service client
        """
    
        if(data_arg is not None and len(data_arg)==6):
           
            client= data_arg[0]
            ssf=data_arg[1]
            sskey=data_arg[2]
            wskey=data_arg[3]
            doc_client= data_arg[4]
            ss_number=data_arg[5]
            
            uri="https://spreadsheets.google.com/feeds/download/spreadsheets/Export?key=%s&exportFormat=csv" %(sskey)
            print uri
            
            #Authentication Token is required at this point
            ## doc_outh_token= doc_client.GetClientLoginToken()
            
            doc_client.SetClientLoginToken(client.GetClientLoginToken())
              
            if _userplatform == 'linux' or _userplatform == 'linux2':
                
                print "Downloading...."
                directory="/tmp/g2sagemath.csv"
                
                doc_client.Export(entry_or_id_or_url=uri, file_path=directory,gid=wskey)
                
                print "Download complete..."
                return ["linux"]
            elif _userplatform == 'win32':
                #download to another location
                return ["Windows"]
                
             
        else:
            print "Error in arguments"
            sys.exit(9)


    def call_sage(self):
        """
            This method will call Sage and ask Sage to load the csv file
            by sending a file pointer
        """
        print "Opening Sage..."
        if(_userplatform == 'linux' or _userplatform == 'linux2'):
            try: 
                #check if Sage is in the $PATH
                if self.is_sage_installed():
                    #call sage directly
                    return_code= subprocess.call(["gnome-terminal -e 'bash -c \"cd ~ && sage; exec bash\"'"],shell=True)
                else: 
                    print "Sage is not found in PATH variable\nDo you wish to add sage path manually?(y/n)"
                    user_will = raw_input()   
                    if user_will == 'y':
                        #user_sage_path="PATH=$PATH:/host/Ubuntu_software/sage-5.11"
                        user_sage_path = self.read_user_sage_path()
                        
                        #check if the path is exactly the sage path
                        if os.path.isfile(user_sage_path+"/sage"):
                            new_path = "PATH=$PATH:%s"%user_sage_path
                            SAGE_STARTUP_FILE= "g2sagemath.sage"
                            bash_cmd_startup_file= "SAGE_STARTUP_FILE=%s"%SAGE_STARTUP_FILE
                            return_code= subprocess.call(["gnome-terminal -e 'bash -c \"cd ~ && %s && %s && sage; exec bash\"'"%(new_path,bash_cmd_startup_file)],shell=True)
                            
                            #now reset SAGE_STARTUP_FILE to original value
                            DEFAULT_SAGE_STARTUP_FILE_PATH="~/.sage/init.sage"
                            bash_cmd_original_startup_file="SAGE_STARTUP_FILE=%s"%DEFAULT_SAGE_STARTUP_FILE_PATH
                            subprocess.call(["gnome-terminal -e 'bash -c \"cd ~ && %s; exec bash\"'"%bash_cmd_original_startup_file],shell=False) 
                            
                            print  return_code 
                        else:
                            print "Invalid sage path\n\n"
                            sys.exit(12)
                    elif user_will == 'n':
                        print "Aborting the process..."
                        sys.exit(10)
                    else:
                        print "Invalid input. Aborting G2SageMath..."
                        sys.exit(11)
                        
                
            except CalledProcessError as e:
                print e
        
    def is_sage_installed(self):
        """
            This method checks if sage is available in the system path
        """
        try:
            if os.system("sage -v")== 0:
                return True
            else:
                return False            
        except:
            return False
        
        
    def read_user_sage_path(self):
        """
            This method allows user to add sage path manually
        """
        try:
            readline.set_completer_delims(' \t\n;')
            readline.parse_and_bind("tab: complete")
            readline.set_completer(self.complete)
            custom_sage_path = raw_input('Enter sage path: ')
            return custom_sage_path
        except EOFError: # Ctrl+D
            print "User aborted the process"
            sys.exit(13)
        

    def complete(self,text, state):
        """
            Completer handler for readline.set_completer
        """
        return (glob.glob(text+'*')+[None])[state]
            
            
            