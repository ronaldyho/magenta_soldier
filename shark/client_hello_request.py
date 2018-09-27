# Python3
import re
import sys

f = "sample.txt"
cnt_ignore = 0

# After this is observed, print starting from the 13th line
s_0 = "Frame"
s_1 = "Secure Sockets Layer"
imptData = ["Cipher Suite", "Handshake Protocol:", "Supported Group", "Signature Algorithm"]

for line in open(f, 'r'):
    if re.search( s_1 ,line ):
        cnt_ignore = 1


    if cnt_ignore == 1:
        i = 0
        while i < len(imptData):
            if re.search( imptData[i] ,line ):
                print(line, end=" ")
                break
            else:
                i += 1


    if re.search( s_0 ,line ):
        cnt_ignore = 0

print("Done")
