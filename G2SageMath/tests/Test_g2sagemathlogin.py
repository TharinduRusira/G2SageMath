'''
Created on Aug 17, 2013

@author: tharindurusira
'''
import unittest
import glogin

class LoginTest(unittest.TestCase):
    
    client=''
    ssf=''

    
    '''
    Test id= 1
        Unit to test = glogin.LogIn.login()
        Assumptions= correct authentication code is given
        Test data= a valid authentication code
        Steps 
        1. Run the test 
        2. follow instructions on the terminal
        
        Expected result= a value of type "gdata.spreadsheet.service.SpreadsheetsService"
    '''
    
    def test_login(self):
        print "---test_login---"
        l1=glogin.LogIn()
        try:
            c=l1.login()
            self.client = c[0]
            self.assertEqual(str(type(self.client)),"<class 'gdata.spreadsheet.service.SpreadsheetsService'>")
            
        except Exception as e:
            print "Test 1: login Exception captured successfully"
            self.assertRaises(SystemExit)
            
            
    '''
    Test id= 2
        Unit to test = glogin.LogIn.Oauth2Login()
        Assumptions= 
        Test data= 
        Steps 
        1. Run the test 
        2. follow instructions on the terminal
        
        Expected result= a value of type "gdata.spreadsheet.service.SpreadsheetsService"
    '''
            
    def test_oauth2login(self):
        pass
      
    '''
    Test id= 3
        Unit to test = glogin.LogIn.ShowDrive()
        Assumptions= 
        Test data= 
        Steps 
               
        Expected result= a value of type "gdata.spreadsheet.service.SpreadsheetsService"
    '''
    
    def test_showdrive_output_type(self):
        print "---test_showdrive_output_type---"
        l2=glogin.LogIn()
        d=[self.client]
        try:
            out_list=l2.showDrive(data_arg=d)
            self.assertEqual(type(out_list),type([]))
            print "showDrive returned a list"
        except Exception as e:
            print "Test 3: showDrive Exception captured successfully"
            self.assertRaises(SystemExit)
            
    
    '''
    Test id= 4
        Unit to test = glogin.LogIn.ShowDrive()
        Assumptions= 
        Test data= 
        Steps 
                 
        Expected result= a value of type "gdata.spreadsheet.service.SpreadsheetsService"
    '''
             
    def test_showdrive_output_size(self):
        print "---test_showdrive_output_size---"
        l3=glogin.LogIn()
        try:
            out_list=l3.showDrive([self.client])
            print len(out_list)
            self.assertEqual(len(out_list),3)
            print "showDrive returned a list of size 3"
        except Exception as e:
            print "Test 4: showDrive Exception captured successfully"
            self.assertRaises(SystemExit)
             
    '''
    Test id= 5
        Unit to test = glogin.LogIn.ShowDrive()
        Assumptions= 
        Test data= 
        Steps 
                 
        Expected result= a value of type "gdata.spreadsheet.service.SpreadsheetsService"
    '''
     
    def test_showdrive_output_content(self):
        print "---test_showdrive_output_content---"
        l4=glogin.LogIn()
        try:
            out_list=l4.showDrive([self.client])
            self.assertEqual(str(type(out_list[0])),"<class 'gdata.spreadsheet.service.SpreadsheetsService'>")
            self.assertEqual(str(type(out_list[1])),"<class 'gdata.GDataFeed'>")
            self.assertEqual(type(out_list[2]),type([]))
        except Exception as e:
            self.assertRaises(SystemExit)
             
    '''
    Test id= 6
        Unit to test = glogin.LogIn.UserChoice()
        Assumptions= 
        Test data= 
        Steps 
        
         
        Expected result= a value of type "gdata.spreadsheet.service.SpreadsheetsService"
    '''
     
    def test_userchoice(self):
        pass
 
     




def main(self):
    test1= LoginTest()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLogin']
    unittest.main()