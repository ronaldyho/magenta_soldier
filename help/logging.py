import logging

############# ############# ############# ############# #############
# REFERENCE:
#   https://stackoverflow.com/questions/13479295/python-using-basicconfig-method-to-log-to-console-and-file
############# ############# ############# ############# #############

loglevel = logging.DEBUG

logging.basicConfig(
    filename='app.log', 
    filemode='w', 
    level=loglevel,
    format='[%(levelname)s] %(message)s',
    datefmt='%H:%M:%S'
)
# set up logging to console
console = logging.StreamHandler()
console.setLevel( loglevel )

# set a format which is simpler for console use
formatter = logging.Formatter('%(levelname)-8s %(message)s')
console.setFormatter(formatter)

# add the handler to the root logger
logging.getLogger('').addHandler(console)

logger = logging.getLogger(__name__)


### Logging Levels ###
#
# CRITICAL 50
# ERROR    40
# WARNING  30
# INFO     20
# DEBUG    10 (also EXCEPTION)
# NOTSET   0
#
# https://docs.python.org/3/library/logging.html#levels
###
