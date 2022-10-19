import multiprocessing, threading
import timeit

def testFunction( PS_arg1 ):
    ...
  
### The BETTER Python3.x way 
# https://www.youtube.com/watch?v=0NNV8FDuck8

with concurrent.futures.ThreadPoolExecutor() as executor:
	result = executor.map(function, array)

with concurrent.futures.ProcessPoolExecutor() as executor:
	result = executor.map(function, array)


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

# class myThread (threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
# 
#     def run(self):
#         valStartRecordTime = timeit.default_timer()  #Alastor
#         logging.critical( "Multithreading Melpomene : {}".format(self.threadID) )
#         logging.critical( "D O N E : {} | {}".format(self.threadID, timeit.default_timer() - valStartRecordTime) )    #Alastor


# def multiThreaded_Melpomene( rangedTasks ):
#
# Stopped using this because its hard to scale and use in my structure
#   For one, it is hackish to use it for executing multiple tests 
#
# ### https://www.tutorialspoint.com/python3/python_multithreading.htm
# ### Testing shows that THREADING is a better option over MultiProcess
# ###   WHEN testing Concurrent API calls     
# 
#     global usr_init 
#     global usr_target
# 
#     range_tasks = range( rangedTasks )
# 
#     for z in range_tasks:
#         ( lambda t :  myThread(t, "thread{}".format(t), t).start() )(z)


def multiThreaded_Mneme( rangedTasks ):
### https://realpython.com/intro-to-python-threading/
###
###   This version of threading can scale better  
###
### Testing shows that THREADING is a better option over MultiProcess
###   WHEN testing Concurrent API calls     

    def thread_func( x ):
        valStartRecordTime = timeit.default_timer()  #Alastor
        logging.critical( "Multithreading Melpomene : {}".format(x) )
        testFunction( x )
        logging.critical( "D O N E : {} | {}".format(x, timeit.default_timer() - valStartRecordTime) )    #Alastor


    global usr_init 
    global usr_target

    range_tasks = range( rangedTasks )
    
    threadList = list()
    for z in range_tasks:
        tt = threading.Thread( target=thread_func, args=(z,))
        threadList.append(tt)
        tt.start()

    for index, thread in enumerate(threadList):
        thread.join()

def multiThreaded_Melete( rangedTasks ):
### https://realpython.com/intro-to-python-threading/
###
###   This version of threading can scale better
###   ThreadPoolExecutor is used, which is cleaner / easier
###
### Testing shows that THREADING is a better option over MultiProcess
###   WHEN testing Concurrent API calls     

    def threadFunc( x ):
        valStartRecordTime = timeit.default_timer()  #Alastor
        logging.critical( "Multithreading Melpomene : {}".format(x) )
        #messaging_p11_send_message( x )
        for m in range(3):
            print( "{} Alastor is dealt {} damage".format(x, m) )
        logging.critical( "D O N E : {} | {}".format(x, timeit.default_timer() - valStartRecordTime) )    #Alastor

    import concurrent.futures

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map( threadFunc, range(3) )

        
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

# Using Mneme - A more scalable threading technique 
multiThreaded_Mneme( range_tasks )

# Using Melete - Like Mneme, but with cleaner
multiThreaded_Melete( range_tasks )
