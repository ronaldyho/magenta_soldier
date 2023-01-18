#!/bin/bash

### Input a file 
list_services=$(<config.txt)

read -p "(1) List All (2) Stop and Start services" varInputCMD

if [ $(varInputCMD) = '1' ]; then

    for val in "${list_services[@]}";
    do
         systemctl show $val | grep -wE 'SubState|Id'
         read -p "..." varInput
    done

elif [ $(varInputCMD) = '2' ]; then

    ### String array 
    declare -a list_services=("logrotate" "csrss")

    for val in "${list_services[@]}";
    do
         systemctl stop $val
         sleep 3
         systemctl status $val
         read -p "(Press Enter to start service)" varInput
         systemctl start $val
    done

fi
