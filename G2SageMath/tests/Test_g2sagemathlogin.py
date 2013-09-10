'''
Created on Aug 17, 2013

@author: tharindurusira
'''
import unittest
import g2sagemathlogin


class LoginTest(unittest.TestCase):
    
    # CLASS VARIABLES
    # defined as global variables because we are testing units here
    # if these are declared to be returned from another test case, -
    # - succeeding tests will depend on the previous tests
    # otherwise login will be needed for every other test case
        
    @classmethod
    def setUpClass(self):
        self.l1=g2sagemathlogin.LogIn()
        self.c=self.l1.login()
        self.ss_client = self.c[0]
        self.doc_client=self.c[1]
           
    
    '''
    Test id= 1
        Unit to test = g2sagemathlogin.LogIn.login()
        Assumptions= correct authentication code is given
        Test data= a valid authentication code
        Steps 
        1. Run the test 
        2. follow instructions on the terminal
        
        Expected result= a value of type "gdata.spreadsheet.service.SpreadsheetsService"
    '''
    
    def test_login_output0(self):
        
        try:
            self.assertEqual(str(type(self.ss_client)),"<class 'gdata.spreadsheet.service.SpreadsheetsService'>") 
        except:
            self.assertRaises(SystemExit)
            
    '''
    Test id= 2
        Unit to test = g2sagemathlogin.LogIn.logIn()
        Assumptions= 
        Test data= 
        Steps 
               
        Expected result=
    '''        
    def test_login_output1(self):
        try:
            self.assertEqual(str(type(self.doc_client)),"<class 'gdata.docs.service.DocsService'>")
        except:
            self.assertRaises(SystemExit)
        
    '''
    Test id= 3
        Unit to test = g2sagemathlogin.LogIn.logIn()
        Assumptions= 
        Test data= 
        Steps 
               
        Expected result=
    '''        
    def test_login_output_size(self):
        
        self.assertEqual(len(self.c),2)
               
            
    '''
    Test id= 
        Unit to test = g2sagemathlogin.LogIn.Oauth2Login()
        Assumptions= 
        Test data= 
        Steps 
        1. Run the test 
        2. follow instructions on the terminal
        
        Expected result= a value of type "gdata.spreadsheet.service.SpreadsheetsService"
    '''
    @unittest.skip("not implemented")      
    def test_oauth2login(self):
        pass
      
    '''
    Test id= 
        Unit to test = g2sagemathlogin.LogIn.ShowDrive()
        Assumptions= 
        Test data= 
        Steps 
               
        Expected result=
    '''
    
    def test_showdrive_output_type(self):
        
        d=[self.ss_client]
        try:
            out_list=self.l1.showDrive(data_arg=d)
            self.assertEqual(type(out_list),type([]))
        except:
            self.assertRaises(SystemExit)
            
    
    '''
    Test id= 
        Unit to test = g2sagemathlogin.LogIn.ShowDrive()
        Assumptions= 
        Test data= 
        Steps 
                 
        Expected result= 
    '''
             
    def test_showdrive_output_size(self):
        
        try:
            out_list=self.l1.showDrive([self.ss_client])
            self.assertEqual(len(out_list),4)

        except:
            self.assertRaises(SystemExit)
             
    '''
    Test id= 
        Unit to test = g2sagemathlogin.LogIn.ShowDrive()
        Assumptions= 
        Test data= 
        Steps 
                 
        Expected result= 
    '''
     
    def test_showdrive_output_content_0(self):
        
        try:
            out_list=self.l1.showDrive([self.ss_client])
            self.assertEqual(str(type(out_list[0])),"<class 'gdata.spreadsheet.service.SpreadsheetsService'>")
        except:
            self.assertRaises(SystemExit)
            
    
    def test_showDrive_output_content_1(self):
        
        try:
            out_list=self.l1.showDrive([self.ss_client])
            self.assertEqual(str(type(out_list[1])),"<class 'gdata.GDataFeed'>")
            self.assertEqual(type(out_list[2]),type([]))
        except:
            self.assertRaises(SystemExit)
            
    def test_showDrive_output_content_2(self):
        
        try:
            out_list=self.l1.showDrive([self.ss_client])
            self.assertEqual(type(out_list[2]),type([]))
        except:
            self.assertRaises(SystemExit)
             
       
    '''
    Test id= 
        Unit to test = g2sagemathlogin.LogIn.UserChoice()
        Assumptions= 
        Test data= 
        Steps 
        
         
        Expected result= 
    '''
    @unittest.skip("not implemented")
    def test_userchoice(self):
        pass
 
     




# def main(self):
#     test1= LoginTest()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLogin']
    unittest.main()