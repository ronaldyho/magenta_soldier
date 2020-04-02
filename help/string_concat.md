# Write to file 
```python
thefile.write("Status code:" + str(req.status_code) + '\r\n'\
    "Response Body" + str(req.text) + '\r\n'\
    "Request time: " + str(req.elapsed.total_seconds()) + '\r\n')
```
Status code:400    
Response Body{"error":{"code":1,"reason":"Invalid username"}}    
Request time: 0.127136    


# CSV to and fro excel
```python
# [1/25] Added sep=| to the first row of the CSV so that you can read the file in excel as well
import re
import pprint
f = open('C:/Logs/PPS_FS/London_2372-567/pps_inventory.txt','r')
g = open('C:/Logs/PPS_FS/London_2372-567/pps_inventory.csv','w')
s = ""
# REGEX -- Start with any character; Next 5-10 characters will be digits from 0-9.
pattern = re.compile("^...[0-9]{5,10}")

row = ["sep=|\n| ","| ","| ","| ","| ","| ","| ","| "]

for line in f:
	if re.search(r"^# file",line):
		pprint.pprint(row[0], width=100)
		if row[0] != "|":
			g.write(row[0] + "|" + row[1] + "|" + row[2] + "|" + row[3] + "|" + row[4] + "|" + row[5] + "|" + row[6] + "|" + row[7] + "| \n")
			row = ["| ","| ","| ","| ","| ","| ","| ","| "]
		row[0] = row[0] + line.rstrip() + " "
	elif re.search(r"^# owner",line):
		row[1] = row[1] + line.rstrip() + " "
	elif re.search(r"^# group",line):
		row[2] = row[2] + line.rstrip() + " "
	elif re.search(r"^user:",line):
		row[3] = row[3] + line.rstrip() + " "
	elif re.search(r"^mask:",line):
		row[4] = row[4] + line.rstrip() + " "
	elif re.search(r"^group:",line):
		row[5] = row[5] + line.rstrip() + " "
	elif re.search(r"^other:",line):
		row[6] = row[6] + line.rstrip() + " "
	elif pattern.search(line):
		row[7] = row[7] + line.rstrip() + " "

g.close()
f.close()
```


# SORT FILES
```
str_pkg_lines = str_pkg.split('\n')
str_pkg_lines.sort()
```

# JOIN list into string again
```
# str_pkg = "\n".join(str_pkg_lines)
```

# CSV to be launch-able in Excel
```
g = open('C:/Logs/updateDetailResponse.csv','w')
g.write("sep=|\n Name | ID | Operation | Version | Type | Size | Checksum ")
g.write(str_pkg)
```

# Printing text - using format 
```
print( "You have {} seen anything; this is {} of this world".format("NOT", "out") )
```

# Printing time 
```
def getSTRtimeNow(format):
    # Returns STRING  
    # time.strftime('%Y-%m-%d %H:%M %Z', time.localtime(t))
    #
    # REF :- Stick to time to prevent DST ambiguity : https://is.gd/rZ7aL2

    import time

    t = time.time()
    if format == 0 or format == "long":
        # 2020-1-1|12:34:59
        return time.strftime('%Y-%m-%d|%H-%M-%S', time.localtime(t))
    elif format == 1 or format == "short":
        # 094818am040220
        return time.strftime('%I%M%S%P%d%m%y', time.localtime(t))
    elif format == 2 or format == "epoch":
        # 1580780901
        return int( t )
    else:
        # 1580780901.5277028
        return t
```
