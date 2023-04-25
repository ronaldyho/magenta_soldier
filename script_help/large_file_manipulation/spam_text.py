import random


fileWriting = open("passwordFile.txt", "w")


yy = ("@", "%", "+", "\\", "//", "!", "$", "^", "?", ":", ".", "~", "`", "-", "_")
y = range(0,120000)
for x in y:
    txtPass = "CarbonH3{}CHydro2{}CH2{}HydrOxyl{}\r\n".format(
        random.choice(yy),
        random.choice(yy),
        random.choice(yy),
        x)
    fileWriting.write(txtPass)

fileWriting.close()