'''
Created on Sep 4, 2013

@author: tharindurusira
'''
from sys import platform as _userplatform

class DataHandler(object):
    '''
        This class includes methods to handle a data file
        and methods to access Sage
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
            ss_number=data_arg[5]
            
            uri="https://docs.google.com/spreadsheet/ccc?key=%s" %(sskey)
            print uri
            
            
            
            #Authentication Token is required at this point
#             doc_outh_token= doc_client.GetClientLoginToken()
#             doc_client.SetClientLoginToken(client.GetClientLoginToken())
              
             
            if _userplatform == 'linux' or _userplatform == 'linux2':
                print "Downloading...."
                directory="/tmp/g2sagemath.csv"
                
                doc_client.Export(entry_or_id_or_url=uri, file_path=directory,gid=wskey)
                
                print "Download complete..."
                
                 
                 
            elif _userplatform == 'win32':
                #download to another location
                pass
                 
                # make an HTTP request and download the file to
                
             
        else:
            print "Error in arguments"
            
            
            
            