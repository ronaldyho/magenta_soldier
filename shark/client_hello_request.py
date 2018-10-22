#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Windows 10
# Python 3.7 (At least 3.5)
import re, sys
import subprocess

print("Version 20181022-1")

global file_out
global file_out_proc

def tshark_decode( argz, file_out ):

    try:
        PCAP_FILE = str(argz[1])
        PORT_FILTER = "tcp.port==" + str(argz[2])
        PORT_DECODE = "tcp.port==" + str(argz[2]) + ",ssl"

        ### WIN CMD :  tshark -r "Captured_9222.pcap" -Y "ssl.handshake && tcp.port==9222" -d "tcp.port==9222,ssl"
        with open( file_out, "w" ) as write_to_file:
            subprocess.run(["tshark", "-r", PCAP_FILE, "-Y", "ssl.handshake && " + PORT_FILTER, "-d", PORT_DECODE, "-V"], stdout=write_to_file)

    except IndexError:
        print()
        print("!! File is not found !!")
        print("Usage:")
        print("  thisScript.py [PCAP file] [PORT]")


def proc_ssl(file_out, file_out_proc):

    # I am assuming that the script only takes in ONE file name

    # Variables s_0 and s_1 are used to determine when I should start filtering for information
    #   The hopes is that by toggling when I should start filter and when I should not, will help
    #   to make this script more efficient
    # imptData array contains the values I should look for and print out
    s_0 = "Frame"
    s_1 = "Secure Sockets Layer"
    imptData = ["Cipher Suite", "Handshake Protocol:", "Supported Group", "Signature Algorithm", "algorithmIdentifier"]
    sharkfile = open( file_out_proc, 'wt')

    cnt_ignore = 0

    try:
        for line in open( file_out , 'r'):
            if re.search( s_1 ,line ):
                cnt_ignore = 1
                #print("==========", end=" \n")
                #sharkfile.write("========== \n")


            if cnt_ignore == 1:
                i = 0
                while i < len(imptData):
                    if re.search( imptData[i] ,line ):
                        print(line, end=" ")
                        sharkfile.write(line)
                        break
                    else:
                        i += 1

            if re.search( s_0 ,line ):
                cnt_ignore = 0

                if re.search( "Frame [0-9]{1,9}:",line ):
                    print(">>> " + line, end=" \n")
                    sharkfile.write("============ \n")
                    sharkfile.write(">>> " + line)

        print("Done")

    except:
        print()

if __name__ == "__main__":

    argz = sys.argv

    file_out = "zlast_tshark_out_" + str(argz[2]) + ".txt"
    file_out_proc = "zlast_ssl_tshark__out_" + str(argz[2]) + ".txt"


    # 1 tshark to decode PCAP and pipe to text
    tshark_decode( argz, file_out )
    
    # 2 Process text output and print to screen
    proc_ssl( file_out, file_out_proc )

