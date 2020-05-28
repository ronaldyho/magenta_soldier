import multiprocessing, threading
import timeit

def testFunction( PS_arg1, PS_arg2, PS_arg3, PS_arg4):
    print( "This method prints {} and {} as well as {} also {}".format(PS_arg, PS_arg, PS_arg, PS_arg) )
  

########### MultiProcessing ##########

# def multiProc_Erato( ranged_tasks ):
# ###  https://pymotw.com/2/multiprocessing/basics.html
# #    ! This will run operations in sequence
# #    This will be slower when executing with a higher range 
# 
#     logging.critical("MultiProc ERATO")
# 
#     range_tasks = range( ranged_tasks )
#     
#     # Calulate time taken    
#     valStartRecordTime = timeit.default_timer()  #Alastor
# 
#     ### Testing shows that number of processes executed cannot be > Num of CPU cores
#     ### It is possible to create more processes, but the rest will not be executed
#     ### In other words, specifying processes > multiprocessing.cpu_count is a waste
# 
#     with multiprocessing.Pool( processes=multiprocessing.cpu_count() ) as pool:
#          pool.map( messaging_p11_send_message, range_tasks )
# 
#     print("DONE", timeit.default_timer() - valStartRecordTime)


def multiProc_Thalia( numOftasks ):
###  https://stackoverflow.com/questions/35908987/multiprocessing-map-vs-map-async
#    This will run operations async; NOT in sequence (in theory)
#    ! This will be FASTER when executing with a higher range 

    logging.critical("MultiProc THALIA; async")

    range_tasks = range( numOftasks )

    # Calulate time taken    
    valStartRecordTime = timeit.default_timer()  #Alastor

    ### Testing shows that number of processes executed cannot be > Num of CPU cores
    ### It is possible to create more processes (ps), but the rest will not be executed
    ### In other words, specifying processes > multiprocessing.cpu_count is a waste
    pool = multiprocessing.Pool( processes=multiprocessing.cpu_count() )
    pp = pool.map_async( testFunction, range_tasks )

    #^ Partial() can help for multiple arguments 
    #   http://python.omics.wiki/multiprocessing_map/multiprocessing_partial_function_multiple_arguments

    pp.wait()
    print("DONE", timeit.default_timer() - valStartRecordTime)

    #pool.close()
    #pool.join()



########### THREADING ##########

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        valStartRecordTime = timeit.default_timer()  #Alastor
        logging.critical( "Multithreading Melpomene : {}".format(self.threadID) )
        testFunction( self.counter )
        logging.critical( "D O N E : {} | {}".format(self.threadID, timeit.default_timer() - valStartRecordTime) )    #Alastor



def multiThreaded_Melpomene( rangedTasks ):
### https://www.tutorialspoint.com/python3/python_multithreading.htm
### Testing shows that THREADING is a better option over MultiProcess
###   WHEN testing Concurrent API calls     

    global usr_init 
    global usr_target

    range_tasks = range( rangedTasks )
    
    for z in range_tasks:
        ( lambda t :  myThread(t, "thread{}".format(t), t).start() )(z)




########### MultiProcessing + Threading ##########
# " No, I haven't make it work. I think I should 
#   give up, before I give up my sanity "


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###

nCPU = multiprocessing.cpu_count()
print("CPU cores # ", nCPU )

range_tasks = 10

# NOT using Erato

# Using Thalia for - Number of operations = Number of CPU cores 
multiProc_Thalia( range_tasks )

# Using Melpomene - To create concurrent API calls 
multiThreaded_Melpomene( range_tasks )
