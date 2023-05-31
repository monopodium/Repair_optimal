#!/bin/bash

function start_close_memcached()
{
    local CLUSTER_ARRAY=('10.0.0.51' '10.0.0.53' '10.0.0.54' '10.0.0.55' '10.0.0.56' '10.0.0.58')
    local CLUSTER_NUM=${#CLUSTER_ARRAY[@]}
    local CLUSTER_NUM=`expr $CLUSTER_NUM - 1`
    local SRC_PATH_RUN_MEMCACHED=/home/msms/codes/Repair_optimal/prototype/run_memcached
    local DIS_DIR_HOME=/home/msms
    local NETWORKCORE_IP='10.0.0.61'
    local NETWORKCORE_PORT=12222
    local CLUSTER_NUMBER_EACH=20
    local PORT_START=31400
    
    for i1 in $(seq 0 $CLUSTER_NUM)
    do
    echo i1
    echo $i1
    NODE_IP_IN=${CLUSTER_ARRAY[$i1]}
    echo $NODE_IP_IN
    if [ $1 == 0 ]
    then
        ssh msms@$NODE_IP_IN 'sudo kill -9 $(pidof memcached)'
        echo 'kill memcached'
        ssh msms@$NODE_IP_IN 'ps -aux |grep memcached | wc -l'
    else
        if [ $1 == 1 ]
        then
            rsync -rtvpl ${SRC_PATH} msms@$NODE_IP_IN:${DIS_DIR_HOME}
        fi
        ssh msms@$NODE_IP_IN 'hostname'
        for j1 in $(seq 0 $CLUSTER_NUMBER_EACH)
        do
            Port=`expr $j1 + $PORT_START`
            echo $Port
            #ssh msms@$NODE_IP_IN 'kill -9 $(lsof -i:'$Port' -t)'
            ssh msms@$NODE_IP_IN 'cd /home/msms/run_memcached;./memcached/bin/memcached -m 1024 -p '$Port' --max-item-size=16777216 -d'
        done
        echo 'memcached process number:'
        ssh msms@$NODE_IP_IN 'ps -aux |grep memcached | wc -l'
    fi
    done
    if [ $1 == 1 ]
    then
        ssh msms@$NETWORKCORE_IP 'git clone https://github.com/magnific0/wondershaper.git'
    fi
    if [ $1 == 0 ]
    then
        ssh msms@$NETWORKCORE_IP 'sudo kill -9 $(pidof memcached)'
        ssh msms@$NETWORKCORE_IP 'ps -aux |grep memcached | wc -l'
    else
        if [ $1 == 1 ]
        then
            rsync -rtvpl $SRC_PATH msms@$NETWORKCORE_IP:$DIS_DIR_HOME
        fi
        #ssh msms@$NETWORKCORE_IP 'kill -9 $(lsof -i:'$NETWORKCORE_PORT' -t)'
        ssh msms@$NETWORKCORE_IP 'cd /home/msms/run_memcached;./memcached/bin/memcached -m 1024 -p '$NETWORKCORE_PORT' --max-item-size=16777216 -d'
        echo "Networkcore:"$NETWORKCORE_IP
        ssh msms@$NETWORKCORE_IP 'hostname'
        echo 'memcached process number:'
        ssh msms@$NETWORKCORE_IP 'ps -aux |grep memcached | wc -l'
    fi

}
start_close_memcached $1
#ARRAY=('192.168.1.107' '192.168.1.104' '192.168.1.118' '192.168.1.119' '192.168.1.114' '192.168.1.109' '192.168.1.127')
# ARRAY=('10.0.0.51' '10.0.0.53' '10.0.0.54' '10.0.0.55' '10.0.0.56' '10.0.0.58')
# # Get size of the array
# # From 0 to (sizeof(array) - 1)
# # So NUM = NUM - 1 
# NUM=${#ARRAY[@]}
# echo "cluster_number:"$NUM
# NUM=`expr $NUM - 1`

# SRC_PATH=/home/msms/codes/Repair_optimal/prototype/run_memcached
# # DIR_NAME=run_memcached
# DIS_DIR=/home/msms
# #NETWORKCORE_IP='192.168.1.121'
# NETWORKCORE_IP='10.0.0.61'
# NETWORKCORE_PORT=12222
# for i in $(seq 0 $NUM)
# do
# temp=${ARRAY[$i]}
#     echo $temp
#     if [ $1 == 0 ]
#     then
#         ssh msms@$temp 'ps -aux |grep memcached | wc -l'
#         ssh msms@$temp 'sudo kill -9 $(pidof memcached)'
#         echo 'kill memcached'
#         ssh msms@$temp 'ps -aux |grep memcached | wc -l'
#         #ssh msms@$temp 'sudo ./wondershaper/wondershaper -c -a enp4s0f1'
#     else
#         if [ $1 == 1 ]
#         then
#             rsync -rtvpl ${SRC_PATH} msms@$temp:${DIS_DIR}
#         fi
#         ssh msms@$temp 'hostname'
#         ssh msms@$temp 'cd /home/msms/run_memcached;bash cluster_run_memcached.sh;bash cluster_run_memcached.sh'
#         echo 'memcached process number:'
#         ssh msms@$temp 'ps -aux |grep memcached | wc -l'
#     fi
# done

# if [ $1 == 1 ]
# then
#     ssh msms@$NETWORKCORE_IP 'git clone https://github.com/magnific0/wondershaper.git'
# fi

# if [ $1 == 0 ]
# then
#     ssh msms@$temp 'ps -aux |grep memcached | wc -l'
#     ssh msms@$NETWORKCORE_IP 'sudo kill -9 $(pidof memcached)'
#     ssh msms@$temp 'ps -aux |grep memcached | wc -l'
#     ssh msms@$NETWORKCORE_IP 'sudo ./wondershaper/wondershaper -c -a enp4s0f1'
# else
#     if [ $1 == 1 ]
#     then
#         rsync -rtvpl $SRC_PATH msms@$NETWORKCORE_IP:$DIS_DIR
#     fi 
#     ssh msms@$NETWORKCORE_IP 'cd /home/msms/run_memcached;bash networkcore.sh;bash networkcore.sh'
#     echo "Networkcore:"$NETWORKCORE_IP
#     ssh msms@$NETWORKCORE_IP 'hostname'
#     echo 'memcached process number:'
#     ssh msms@$NETWORKCORE_IP 'ps -aux |grep memcached | wc -l'
# fi

# #rsync -rtvpl /home/msms/codes/Repair_optimal/prototype/run_memcached msms@192.168.1.121:/home/msms
# #ps -aux |grep memcached | wc -l
# #ssh msms@192.168.1.114 'ps -aux |grep memcached | wc -l'