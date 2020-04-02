Possible BASH scripts 
```bash
# 02-29-2019
CURRENTDATE=`date +"%m-%d-%Y"`

# 2020 Apr 02 14:45:56
CURRENTLONGDATE=`date +"%Y %b %d %T"`

# 1585810300
SEC_SINCE_EPOCH=`date +%s`
SEC_SINCE_EPOCH_FRM_DATE=`date -d "Oct 21 1973" +%s`

echo SEC_SINCE_EPOCH
```

Calling BASH from PYTHON3
```sh
outputFile="./logging_out_"`date +%s`
echo ${outputFile}
#$ ./logging_out_1585810524
```
