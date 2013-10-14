"""
Created on Aug 6, 2013
@author: tharindurusira
"""

#############################################################################
#       Copyright (C) 2013 Tharindu Rusira <tharindurusira@gmail.com>
#  Distributed under the terms of the GNU General Public License (GPL)
#  The full text of the GPL is available at:
#                  http://www.gnu.org/licenses/
#############################################################################

import gflags
import os
'''
import httplib2
from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
'''
import gdata.spreadsheet.service
from gdata.client import BadAuthentication

import logging
import getpass
import sys

logging.basicConfig()
import gdata.docs.service



class LogIn:
    """
        This module will provide functions to login, search documents and select a spreadsheet 
    """

    # OAuth 2.0 variables
    FLAGS = gflags.FLAGS
    CLIENT_SECRETS = 'client_secrets.json'
    MISSING_CLIENT_SECRETS_MESSAGE = "%s" % os.path.join(os.path.dirname(__file__), CLIENT_SECRETS)
    REDIRECT_URI = ''   
    
        
    def __init__(self, redirect_uri='urn:ietf:wg:oauth:2.0:oob'):
        
        print "+--------------------------------------------------------------------+"
        print "| G2SageMath Version 1.0, Release Date: 2013-10-14                   |"
        print "| Integrating Google spreadsheets to Sage                            |"
        print "| Author: M.P. Tharindu Rusira Kumara (tharindurusira@gmail.com)     |"
        print "+--------------------------------------------------------------------+" 
        
        #self.REDIRECT_URI = redirect_uri # for OAuth 2.0 redirection
        
        
    def login(self):
        
        # Auth2.0 Login does not support gdata.spreadsheets service
        # This method implements ProgrammaticLogin() where a user will have to provide 
        # user name and password on the terminal itself
        
        client = gdata.spreadsheet.service.SpreadsheetsService()
        doc_client =gdata.docs.service.DocsService()
        client.ssl = True
        try:
            client_email =raw_input("Gmail address: ")
            client.email = client_email
            doc_client.email=client_email
            client_pwd = getpass.getpass("Password: ")
            client.password = client_pwd
            doc_client.password=client_pwd

            client.ProgrammaticLogin()
            doc_client.ProgrammaticLogin()
            return [client,doc_client]
        except BadAuthentication:
            print "Check user name/password and retry..."
            sys.exit(1)
        except KeyboardInterrupt:
            print "\nAborting G2SageMath...\n"
            sys.exit()
        except Exception as e:
            if(str(e)=="[Errno 113] No route to host"):
                print "Network ERROR. Check your Internet connection...\n"
                sys.exit()
            else:
                print "Error occured..., Aborting G2SageMath\n"
                sys.exit(2)
 
    ''' outh2Login commented out 
         
    def oauth2Login(self):
        """
        Login to a Google account using OAuth 2.0
        
        """
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
    '''  
            
                            
    def show_drive(self, data_arg):
        """
            data_arg is a list where data_arg[0] is of the type gdata.spreadsheet.service.SpreadsheetsService()
            returned from login() method 
            
            data_arg[1] --> doc_client
        """
        client= data_arg[0]
        doc_client= data_arg[1]
        try:
            if isinstance(client,gdata.spreadsheet.service.SpreadsheetsService):
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
                return [client,spreadsheetfeed,name_list,doc_client]       
        except:
            print "Error occurred while fetching spreadsheets..."
            sys.exit(3)               
            
    def user_choice(self,ssdata_arg):
        
        """
            ssdata_arg[0] is the instance of gdata.spreadsheet.service.SpreadsheetsService()
            passed from above methods
            ssdata_arg[1] is the SpreadSheetFeed
            ssdata_arg[2] is the list of spreadsheet names
            ssdata_arg[3] doc_client
        
        """
        
        if(ssdata_arg != None):
            
            client= ssdata_arg[0]
            ssf=ssdata_arg[1]
            ss_name_list=ssdata_arg[2]
            doc_client=ssdata_arg[3]
            
            choice= raw_input("Number of the file from the above list: ")
            # a little sanity check
            try:
                choice=int(choice,10)
                if(choice>=0):
                    sheet= ss_name_list[choice]
                    choice_key=ssf.entry[choice].id.text.rsplit('/',1)[1]
                    #print choice_key
                    return [client,ssf,choice_key,doc_client,choice]
                else:
                    sys.exit(4)
            except ValueError:
                print "Invalid input"
                sys.exit(5)
            except Exception as e:
                print e
                sys.exit(6)
        else:
            print "spreadsheet argument returned None"
            sys.exit(7)
        
    def read_worksheets(self,data_arg):
        """
            data_arg[0] is a client object
            data_arg[1] is the SpreadSheetFeed
            data_arg[2] is the spreadsheet choice made by the user
            data_arg[3] doc_client
            data_arg[4] list index of the spreadsheet in spreadsheetfeed
        """
        
        client= data_arg[0]
        spreadsheetfeed=data_arg[1]
        sskey=data_arg[2]
        doc_client= data_arg[3]
        sschoice=data_arg[4]
        
        print "\nWorksheets in the Spreadsheet\n\n"
        
        j=1
        try:
            worksheetfeed= client.GetWorksheetsFeed(sskey) 
            
            for worksheet in worksheetfeed.entry:
                print "["+str(j)+"] "+ worksheet.title.text
                j=j+1
             
            ws_choice= raw_input("Number of the file from the above list: ")
            ws_choice=int(ws_choice)-1 # worksheets start with 0            
            output= [client,spreadsheetfeed,sskey,ws_choice,doc_client,sschoice]
            return output
                          
        except:
            print "Error occurred while fetching worksheets..."
            sys.exit(8)