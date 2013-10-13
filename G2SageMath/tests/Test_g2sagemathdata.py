'''
Created on Sep 10, 2013

@author: tharindurusira
'''

#############################################################################
#       Copyright (C) 2013 Tharindu Rusira <tharindurusira@gmail.com>
#  Distributed under the terms of the GNU General Public License (GPL)
#  The full text of the GPL is available at:
#                  http://www.gnu.org/licenses/
#############################################################################


import unittest
from src import g2sagemathlogin, g2sagemathdata
import os

class DataHandlerTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        logger=g2sagemathlogin.LogIn()
        
        # I do not want to automate login procedure. It's obvious, isn't it?
        self._login = logger.login()
        self._show_drive_out = logger.show_drive(self._login)
        self._user_choice = logger.user_choice(self._show_drive_out)
        self._readws_out = logger.read_worksheets(self._user_choice)

        #### Assumptions
        # 1. setUp class returns a valid input. The respective code for these methods
        #     are tested in Test_g2sagemathlogin 
        ####

    def tearDown(self):
        pass

    def test_download_csv_input_check0(self):
        self.assertEqual(len(self._readws_out),6)
        
    def test_download_csv_input_check1(self):
        data_handler = g2sagemathdata.DataHandler()
        data_handler.download_csv(self._readws_out)
        self.failUnless("g2sagemath.csv" in os.listdir("/tmp"))
        
        
    def test_call_sage_system_path(self):
        # test if the PATH variable contains Sage
        pass
    
    


if __name__ == "__main__":
    #import sys;sys.arDataHandlerTest ['', 'DataHandlerTest.testName']
    unittest.main()