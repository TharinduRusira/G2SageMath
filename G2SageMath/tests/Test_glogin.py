'''
Created on Aug 17, 2013

@author: tharindurusira
'''
import unittest
import glogin

class LoginTest(unittest.TestCase):
    
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
    
    client=''
    ssf=''
    
    def test_login(self):
        print "---test_login---"
        l1=glogin.LogIn()
        try:
            self.client=l1.login()
            self.assertEqual(str(type(self.client)),"<class 'gdata.spreadsheet.service.SpreadsheetsService'>")
            return self.client
        except:
            self.assertRaises(SystemExit)
            
            
            
    def test_oauth2login(self):
        pass
      
    
    def test_showdrive_output_type(self):
        print "---test_showdrive_output_type---"
        l2=glogin.LogIn()
        try:
            out_list=l2.showDrive(self.client)
            self.assertEqual(type(out_list),type([]))
        except:
            self.assertRaises(SystemExit)
            
    def test_showdrive_output_size(self):
        print "---test_showdrive_output_size---"
        l3=glogin.LogIn()
        try:
            out_list=l3.showDrive(self.client)
            self.assertEqual(out_list.size(),2)
        except:
            self.assertRaises(SystemExit)
    
    def test_showdrive_output_content(self):
        print "---test_showdrive_output_content---"
        l4=glogin.LogIn()
        try:
            out_list=l4.showDrive(self.client)
            self.assertEqual(str(type(out_list[0])),)
        except:
            self.assertRaises(SystemExit)
    
    def test_userchoice(self):
        pass

    




def main(self):
    
    test1=LoginTest()
    test1.test_login()
    test1.test_showdrive_output_type(self.client)
    
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLogin']
    unittest.main()