'''
Created on Sep 4, 2013

@author: tharindurusira
'''

from sys import platform as _userplatform

class DataHandler(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def downloadCSV(self,data_arg):
        
        if(len(data_arg)==4):
            
            client= data_arg[0]
            ssf=data_arg[1]
            sskey=data_arg[2]
            wskey=data_arg[3]
            
            # make an HTTP request and download the file to
            
            
            if _userplatform == 'linux' or _userplatform == 'linux2':
                #download the file to some location
                pass
            elif _userplatform == 'win32':
                #download to another location
                pass
            
            