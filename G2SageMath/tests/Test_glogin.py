'''
Created on Aug 17, 2013

@author: tharindurusira
'''
import unittest
import glogin



'''
Test id= 1
Unit to test = glogin.LogIn.login()
Assumptions= correct authentication code is given
Test data= a valid authentication code
Steps 
1. Run the test 
2. follow instructions on the terminal

Expected result= True/ False
'''
class Test_glogin(unittest.TestCase):


    def testLogin(self):
        l=glogin.LogIn()
        x=l.login()
        self.assertEqual(x, True,"glogin.LogIn.login() passed")




def main(self):
    
    test1=Test_glogin()
    test1.testLogin()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLogin']
    unittest.main()