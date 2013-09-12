'''
Created on Sep 4, 2013

@author: tharindurusira
'''
import os
from sys import platform as _userplatform
import tempfile

class DataHandler(object):
    '''
        This class includes methods to handle a datafile
        and Sage related methods
    '''
       
    def downloadCSV(self,data_arg):
        
        '''
            data_arg[0] --> gdata.Spreadsheet.service client
        '''
        
        
        if(data_arg is not None and len(data_arg)==6):
           
            client= data_arg[0]
            ssf=data_arg[1]
            sskey=data_arg[2]
            wskey=data_arg[3]
            doc_client= data_arg[4]
            
            uri="http://docs.google.com/feeds/spreadsheets/ccc?key=%s#gid=%d" %(sskey,wskey)
            print uri
            
            #Authentication Token is required at this point
#             doc_outh_token= doc_client.GetClientLoginToken()
#             doc_client.SetClientLoginToken(client.GetClientLoginToken())
              
             
            if _userplatform == 'linux' or _userplatform == 'linux2':
                #print "Downloading...."
                directory="/tmp"
                #temp_file= tempfile.mkstemp(suffix=".csv", prefix="g2sagemath", dir=directory)
                #doc_client.Download(entry_or_id_or_url=uri, file_path=temp_file)
                #print "Download complete..."
                #os.remove(temp_file)
                 
                 
            elif _userplatform == 'win32':
                #download to another location
                pass
                 
                # make an HTTP request and download the file to
                
             
        else:
            print "Error in arguments"
            
            
            
            