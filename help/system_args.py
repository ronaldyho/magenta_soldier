import sys

def main(argv):

    if len(sys.argv) == 3:
        ### <this script>.py _user _file
        print("argv==3")
        _user = sys.argv[1]
        _file = sys.argv[2]

        print("[Ad-Hoc] u:" + _user + " f:" + _file)
        exec200Test(_user, _file)

    elif len(sys.argv) == 1:
        ### <this script>.py
        print("argv==1")
        exec_StoS_101()

        input("Press enter to continue")

    else:
        print( "argv==", str(len(sys.argv)) )
        print(""" Accepts two arguments (arg) OR None 
         ARG[1] = User 
         ARG[2] = File 

         When executed without arguments ... 
        """)


#######################################################

if __name__ == "__main__":
# Of course, ^this is not necessary for python3 
    main(sys.argv[1:])
