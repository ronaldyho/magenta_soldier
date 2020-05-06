import multiprocessing, timeit

def printString( PS_arg1, PS_arg2, PS_arg3, PS_arg4):
    print( "This method prints {} and {} as well as {} also {}".format(PS_arg, PS_arg, PS_arg, PS_arg) )


def main():
  valStartRecordTime = timeit.default_timer()

  nThreads = 10
  listThreads = []

  for i in range( nThreads ):
      print( "t:{}\t{}".format(i, timeit.default_timer()) )
      t = multiprocessing.Process( target=printString, args=( "1", "2", "3", "nvr 4" ) )
      listThreads.append(t)
      t.start()
  
  
