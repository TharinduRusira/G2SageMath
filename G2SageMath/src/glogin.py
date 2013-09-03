'''
Created on Aug 6, 2013
@author: tharindurusira
'''
import gflags
import httplib2
import os

from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
import gdata.spreadsheet.service

import logging
import getpass
import sys
from gdata.client import BadAuthentication

logging.basicConfig()



class LogIn:
    '''
        This module will provide functions to login, search documents and select a spreadsheet
        
    '''

    # OAuth 2.0 variables
    FLAGS = gflags.FLAGS
    CLIENT_SECRETS = 'client_secrets.json'
    MISSING_CLIENT_SECRETS_MESSAGE = "%s" % os.path.join(os.path.dirname(__file__), CLIENT_SECRETS)
    REDIRECT_URI = ''   
    
        
    def __init__(self, redirect_uri='urn:ietf:wg:oauth:2.0:oob'):
        print '\n\nG2SageMath\nIntegrating Google spreadsheets to Sage\n' 
        print 'Author: M.P. Tharindu Rusira Kumara (tharindurusira@gmail.com)\n\n'
        #self.REDIRECT_URI = redirect_uri
        
        
    def login(self):
        
        # Auth2.0 Login does not support gdata.spreadsheets service
        # This method implements ProgrammaticLogin() where a user will have to provide 
        # user name and password on the terminal itself
        
        client = gdata.spreadsheet.service.SpreadsheetsService()
        client.ssl = True
        client_email = raw_input("Gmail address: ")
        client.email = client_email
        client.password = getpass.getpass("Password: ")
        
        try:
            client.ProgrammaticLogin(captcha_token=None, captcha_response=None)
            return [client]
        except BadAuthentication:
            print "Check user name/password and retry..."
            sys.exit(-1)
        except Exception as e:
            print "ERROR..."+str(e)
            sys.exit(-1)
 
         
    def oauth2Login(self):
        '''
        Login to a Google account using OAuth 2.0
        
        '''
        # Set up a Flow object to be used for authentication.
        FLOW = flow_from_clientsecrets(self.CLIENT_SECRETS, scope=['https://spreadsheets.google.com/feeds'], message=self.MISSING_CLIENT_SECRETS_MESSAGE, redirect_uri=self.REDIRECT_URI)
        auth_url = FLOW.step1_get_authorize_url()
        
        print "Go to following URL to get access code\n\n\n" + auth_url + "\n\n"
        
        try:
            code = raw_input('Enter verification code: ').strip()
            credentials = FLOW.step2_exchange(code)
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
                  
    def showDrive(self, data_arg):
        '''
            data_arg is a list where data_arg[0] is of the type gdata.spreadsheet.service.SpreadsheetsService()
            returned from login() method 
        '''
        client= data_arg[0]
        try:
            
            #spreadsheetfeed = client.GetSpreadsheetsFeed(key=None, query=None, visibility='private', projection='full')
            spreadsheetfeed = client.GetFeed('http://spreadsheets.google.com/feeds/spreadsheets/private/full') 
            print "\n List of spreadsheets"
            i = 0
            name_list=[]
            for spreadsheet in spreadsheetfeed.entry:
                name= spreadsheet.title.text
                print "[" + str(i) + "] " + name
                #Shall we add file names to a list or something? For future reference
                name_list.append(name) 
                i = i + 1
            
            return [client,spreadsheetfeed,name_list]  
             
        except Exception as e:
            
            print "Error occurred while fetching spreadsheets..."+e
            sys.exit(-1)
                
            
    def userChoice(self,ssdata_arg):
        
        '''
            ssdata_arg[0] is the instance of gdata.spreadsheet.service.SpreadsheetsService()
            passed from above methods
            ssdata_arg[1] is the SpreadSheetFeed
            ssdata_arg[2] is the list of spreadsheet names
        
        '''
        
        if(ssdata_arg != None):
            
            client= ssdata_arg[0]
            ssf=ssdata_arg[1]
            ss_name_list=ssdata_arg[2]
            
            choice= raw_input("Number of the file from the above list: ")
            # a little sanity check
            try:
                choice=int(choice,10)
                sheet= ss_name_list[choice]
                choice_key=ssf.entry[choice].id.text.rsplit('/',1)[1]
                #print choice_key
                return [client,ssf,choice_key]
            except ValueError:
                print "Invalid input"
                sys.exit(-1)
            except Exception as e:
                print e
                sys.exit(-1)
        else:
            sys.exit(-1)
        
    def readWorksheets(self,data_arg):
        '''
            data_arg[0] is a client object
            data_Arg[1] is the SpreadSheetFeed
            data_Arg[2] is the spreadsheet choice made by the user
        '''
        
        client= data_arg[0]
        spreadsheetfeed=data_arg[1]
        sskey=data_arg[2]
        
        print "\nWorksheets in the Spreadsheet\n\n"
        
        j=0
        try:
            worksheetfeed= client.GetWorksheetsFeed(sskey) 
            for worksheet in worksheetfeed.entry:
                print "["+str(j)+"] "+ worksheet.title.text
                j=j+1
                
            ws_choice= raw_input("Number of the file from the above list: ")
                      
        except Exception as e: 
            print e
            print "Error occurred while fetching worksheets..."
            sys.exit(-1)
             
               
                
            
            
       

    
