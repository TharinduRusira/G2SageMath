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
                    user_sage_path="PATH=$PATH:/host/Ubuntu_software/sage-5.11"
                    return_code= subprocess.call(["gnome-terminal -e 'bash -c \"cd ~ && %s && sage; exec bash\"'"%my_sage_path],shell=True)
                    
                
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
        
        
    def set_user_sage_path(self):
        """
            This method allows user to add sage path manually
        """
        try:
            readline.set_completer_delims(' \t\n;')
            readline.parse_and_bind("tab: complete")
            readline.set_completer(self.complete)
            custom_sage_path = raw_input('Enter sage path: ')
            return custom_sage_path
        except EOFError:
            print "User aborted the process"
            sys.exit()
        

    def complete(self,text, state):
        """
            Completer handler for readline.set_completer
        """
        return (glob.glob(text+'*')+[None])[state]
            
            
            