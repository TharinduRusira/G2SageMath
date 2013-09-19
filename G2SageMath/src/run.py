"""
run.py
Main script in G2SageMath
"""

#############################################################################
#       Copyright (C) 2013 Tharindu Rusira <tharindurusira@gmail.com>
#  Distributed under the terms of the GNU General Public License (GPL)
#  The full text of the GPL is available at:
#                  http://www.gnu.org/licenses/
#############################################################################


from g2sagemathlogin import LogIn
from g2sagemathdata import DataHandler
import sys
import gflags

def main(argv):
    # Let the gflags module process the command-line arguments
    l=LogIn()
    m=DataHandler()
    
    try:
        argv = l.FLAGS(argv)        
        x=l.login()
        y= l.showDrive(x)
        z=l.userChoice(y)
        final_details = l.readWorksheets(z)
        m.downloadCSV(data_arg=final_details)
        
    except gflags.FlagsError, e:
        print '%s\\nUsage: %s ARGS\\n%s' % (e, argv[0], l.FLAGS)
        sys.exit(1)
     
if __name__ == '__main__':
    main(sys.argv)