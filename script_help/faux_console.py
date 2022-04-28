from logging import *   ###<< Is in same directory
import saveToPickle        ###<< Is in same directory
import os, sys

class qaronConsole(object): 

### FUNCTIONS  #########################################################

    ### The user can choose the test cases for execution 
    def __init__(self):
        global glbcurrentUser
        glbcurrentUser = savepoint.getCurrentUser()
        
        logging.info("Current User: \t" + glbcurrentUser)

        self.runConsole()

    ### A console "app" where the user will give an input
    ### Input will be prefixed with the method_prefix value and function will be called  
    def runConsole(self):
        execVal = input("(cmd)> ")
        logging.critical( "{} [ARG_ID] => {}".format( str(qol.getSTRtimeNow(0)), str(execVal)) )

        method_prefix = 'exec_'
        method_name = method_prefix + str(execVal)  ## User enters "1001" and be intepreted as "exec_1001"
        method = getattr(self, method_name, lambda :'Invalid [ARG_ID] specified; Please refer to Docs')
        return method()

    def exec_1001(self):
        
        timeX = ""        
        x = input("""
                  [1] 30 sec
                  [2] 60 sec
                  [3] 86,400 sec / 1 day
                  [4] 345,600 sec / 4 days
        [?]>""")
        
        if int(x) == 1:
            timeX = 30
        elif int(x) == 2:
            timeX = 60
        elif int(x) == 3:
            timeX = 86400
        elif int(x) == 4:
            timeX = 345600
        else:
            sys.exit()
        
        logging.debug( timeX )            
        self.runConsole()

########################################################################

ss = qaronConsole()
## EOF ##
