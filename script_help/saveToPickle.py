### Data to pickle 

import os, sys, pickle


### DEF ###
def openMyJarOfPickles():
    if os.path.exists( pickleFile ):
        picklesFromMyJar = open( pickleFile, 'rb')
    else:
        out = chngCurrentUser()
        picklesFromMyJar = open( pickleFile, 'rb')
    return picklesFromMyJar    


def readFromPickle():
### Returns DICT 
    if os.path.exists( pickleFile ):    
        with open( pickleFile, 'rb') as inputFile:
            try:
                out = pickle.loads( inputFile.read() ) #<< Main
                logging.info( out )
                return out
            except:
                logging.exception(sys.exc_info())
                sys.exit()
    else:
        createNewX()

        with open( pickleFile, 'rb') as inputFile:
            try:
                out = pickle.loads( inputFile.read() ) #<< Main
                logging.info( out )
                return out
            except:
                logging.exception(sys.exc_info())
                sys.exit()


def writeToPickle( usr_name, grp_name ):
    dictDetails = {}
    
    if os.path.exists( pickleFile ) == True:
        logging.debug( os.path.exists(pickleFile) )
        with open( pickleFile, 'rb') as inputFile:
            try:
                dictDetails = pickle.load( inputFile ) #<< Main
                logging.debug("Current Pickle: \n" + str(dictDetails))
                inputFile.close()
            except:
                logging.exception(sys.exc_info())
                sys.exit()

    logging.debug("1:" + str(dictDetails) )

    with open( pickleFile, 'wb') as fileWritePickle:
        
        if usr_name != None:
            dictDetails['USER_NAME'] = usr_name
        if grp_name != None:
            dictDetails['USER_NAME'] = usr_name
            dictDetails['GRP_NAME'] = grp_name

        pickle.dump( dictGroupDetails, fileWritePickle, protocol=pickle.HIGHEST_PROTOCOL)

    logging.debug("2:" + str(dictDetails) )

