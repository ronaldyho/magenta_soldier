#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Windows 10
# Python 3.7 (At least 3.5)
import re, sys
import subprocess

print("Version 20180928-2")

global file_out
global file_out_proc
file_out = "zlast_tshark_out.txt"
file_out_proc = "zlast_ssl_tshark__out.txt"

def tshark_decode(argz):

    try:
        PCAP_FILE = str(argz[1])
        PORT_FILTER = "tcp.port==" + str(argz[2]) + ",ssl"

        ### WIN CMD :  tshark -r "Captured_9222.pcap" -Y "ssl.handshake" -d tcp.port==9222,ssl"
        with open( 'zlast_tshark_out.txt', "w" ) as write_to_file:
            subprocess.run(["tshark", "-r", PCAP_FILE, "-Y", "ssl.handshake", "-d", PORT_FILTER, "-V"], stdout=write_to_file)

    except IndexError:
        print()
        print("!! File is not found !!")
        print("Usage:")
        print("  thisScript.py [PCAP file] [PORT]")


def proc_ssl():

    # I am assuming that the script only takes in ONE file name

    # Variables s_0 and s_1 are used to determine when I should start filtering for information
    #   The hopes is that by toggling when I should start filter and when I should not, will help
    #   to make this script more efficient
    # imptData array contains the values I should look for and print out
    s_0 = "Frame"
    s_1 = "Secure Sockets Layer"
    imptData = ["Cipher Suite", "Handshake Protocol:", "Supported Group", "Signature Algorithm"]
    sharkfile = open( file_out_proc, 'wt')

    cnt_ignore = 0

    try:
        for line in open( file_out , 'r'):
            if re.search( s_1 ,line ):
                cnt_ignore = 1


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

        print("Done")

    except:
        print()

if __name__ == "__main__":

    # 1 tshark to decode PCAP and pipe to text
    tshark_decode( sys.argv )
    
    # 2 Process text output and print to screen
    proc_ssl()

