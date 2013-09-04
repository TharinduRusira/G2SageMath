from g2sagemathlogin import LogIn
import sys
import gflags

def main(argv):
    # Let the gflags module process the command-line arguments
    l=LogIn()
    try:
        argv = l.FLAGS(argv)        
        x=l.login()
        y= l.showDrive(x)
        z=l.userChoice(y)
        final_details = l.readWorksheets(z)
        print final_details
        
    except gflags.FlagsError, e:
        print '%s\\nUsage: %s ARGS\\n%s' % (e, argv[0], l.FLAGS)
        sys.exit(1)
    
    
    
if __name__ == '__main__':
    main(sys.argv)