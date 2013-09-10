'''
Created on Sep 4, 2013

@author: tharindurusira
'''
from sys import platform as _userplatform

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
            sschoice=data_arg[5]
            
            uri="http://docs.google.com/feeds/spreadsheets/private/full/key=%s" %sskey
            print uri
            
            #Authentication Token is required at this point
            doc_outh_token= doc_client.GetClientLoginToken()
            doc_client.SetClientLoginToken(client.GetClientLoginToken())
            '''
            class DocsService(gdata.service.GDataService)
            
                Export(self, entry_or_id_or_url, file_path, gid=None, extra_params=None)
                    Downloads a document from the Document List in a different format.
                     
                    Args:
                      entry_or_id_or_url: a DocumentListEntry, or the resource id of an entry,
                          or a url to download from (such as the content src).
                      file_path: string The full path to save the file to.  The export
                          format is inferred from the the file extension.
                      gid: grid id, for downloading a single grid of a spreadsheet
                      extra_params: a map of any further parameters to control how the document
                          is downloaded
                     
                    Raises:
                      RequestError if the service does not respond with success
                                
            '''
              
             
            if _userplatform == 'linux' or _userplatform == 'linux2':
                print "Downloading...."
                directory="/tmp"
                #temp_file= tempfile.mkstemp(suffix=".csv", prefix="g2sagemath", dir=directory)
                doc_client.Export(entry_or_id_or_url=str(ssf.entry[sschoice]), file_path=directory,gid=wskey)
                print "Download complete..."
                #os.remove(temp_file)
                 
                 
            elif _userplatform == 'win32':
                #download to another location
                pass

             
        else:
            print "Error in arguments"
            
            
            
            