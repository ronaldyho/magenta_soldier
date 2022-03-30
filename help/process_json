#  { "contentType": "Something", "time": "1648561966495" } < divide by 1000
#  { "contentType": "Something", "time": "1302180658" } < no need to divide


# https://hands-on.cloud/how-to-process-json-data-in-python/

import json, datetime

def printToScreen( JSONval ):
    json.dumps( JSONval, indent=4 )



## Loading from File
with open(f"export1.json", "r") as file_stream:
    data = file_stream.read()

    ## Deserializing string
    jsonBody = json.loads(data)

    #print(f'data variable type: {type(data)}')
    #print(f'data variable content: {data}')
 

for x in jsonBody:
    if x['contentType'] == "Something":

        time_in_epoch = x['time']
        time_in_datetime = datetime.datetime.fromtimestamp( int(time_in_epoch) / 1000)

        ## '%Y-%m-%d %H:%M:%S'
        print( str(time_in_epoch) + "|" +  time_in_datetime.strftime('%Y-%m-%d %H:%M:%S') )
