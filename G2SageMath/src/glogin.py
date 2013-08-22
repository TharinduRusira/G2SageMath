'''
Created on Aug 6, 2013
@author: tharindurusira
'''
import gflags
import httplib2
import os

from apiclient.discovery import build
from oauth2client.client import AccessTokenRefreshError
from oauth2client.client import flow_from_clientsecrets

import logging
logging.basicConfig()



class LogIn:
    '''
    Login to a Google account using OAuth 2.0
    This module will provide functions to login, search documents and select a spreadsheet
    '''
    
    #OAuth 2.0 variables
    FLAGS = gflags.FLAGS
    CLIENT_SECRETS = 'client_secrets.json'
    MISSING_CLIENT_SECRETS_MESSAGE = "%s" % os.path.join(os.path.dirname(__file__),CLIENT_SECRETS)
    REDIRECT_URI=''
    
    

    #Spreadsheet variables
    
        
    def __init__(self,redirect_uri='urn:ietf:wg:oauth:2.0:oob'):
        print 'G2SageMath\nIntegrating Google spreadsheets to Sage\n' 
        print 'Author: M.P. Tharindu Rusira Kumara (tharindurusira@gmail.com)'
        self.REDIRECT_URI=redirect_uri
        
        
    def login(self):
        # Set up a Flow object to be used for authentication.
        FLOW = flow_from_clientsecrets(self.CLIENT_SECRETS,scope=['https://spreadsheets.google.com/feeds'],message=self.MISSING_CLIENT_SECRETS_MESSAGE,redirect_uri=self.REDIRECT_URI)
        
        auth_url=FLOW.step1_get_authorize_url()
        print "Go to following URL to get access code\n\n\n" + auth_url+ "\n\n"
        
        try:
            
            code = raw_input('Enter verification code: ').strip()
            credentials= FLOW.step2_exchange(code)
           
        except:
            print 'Validation code ERROR !'
            
        try:    
            http = httplib2.Http()
            http = credentials.authorize(http)
            service = build('drive', 'v2', http=http)
            return True
        except :
            print 'HTTP initialization error'
            return False
        
        

            
    def showDrive(self):
        
        try:
            # gdata code goes here
            pass
               
            
        except AccessTokenRefreshError:
            print ("The credentials have been revoked or expired, please re-run the application to re-authorize")
    
        

    