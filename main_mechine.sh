#!/bin/bash
 
#ARRAY=('192.168.1.107' '192.168.1.104' '192.168.1.118' '192.168.1.119' '192.168.1.114' '192.168.1.109' '192.168.1.127')
ARRAY=('10.0.0.51' '10.0.0.53' '10.0.0.54' '10.0.0.55' '10.0.0.56' '10.0.0.58')
# Get size of the array
# From 0 to (sizeof(array) - 1)
# So NUM = NUM - 1 
NUM=${#ARRAY[@]}
echo "cluster_number:"$NUM
NUM=`expr $NUM - 1`

SRC_PATH=/home/msms/codes/Repair_optimal/prototype/run_memcached
# DIR_NAME=run_memcached
DIS_DIR=/home/msms
#NETWORKCORE_IP='192.168.1.121'
NETWORKCORE_IP='10.0.0.61'
NETWORKCORE_PORT=12222
for i in $(seq 0 $NUM)
do
temp=${ARRAY[$i]}
    echo $temp
    if [ $1 == 0 ]
    then
        ssh msms@$temp 'ps -aux |grep memcached | wc -l'
        ssh msms@$temp 'sudo kill -9 $(pidof memcached)'
        echo 'kill memcached'
        ssh msms@$temp 'ps -aux |grep memcached | wc -l'
    else
        if [ $1 == 1 ]
        then
            rsync -rtvpl ${SRC_PATH} msms@$temp:${DIS_DIR}
        fi
        ssh msms@$temp 'hostname'
        ssh msms@$temp 'cd /home/msms/run_memcached;bash cluster_run_memcached.sh;bash cluster_run_memcached.sh'
        echo 'memcached process number:'
        ssh msms@$temp 'ps -aux |grep memcached | wc -l'
    fi
done

if [ $1 == 1 ]
then
    ssh msms@$NETWORKCORE_IP 'git clone https://github.com/magnific0/wondershaper.git'
fi

if [ $1 == 0 ]
then
    ssh msms@$temp 'ps -aux |grep memcached | wc -l'
    ssh msms@$NETWORKCORE_IP 'sudo kill -9 $(pidof memcached)'
    ssh msms@$temp 'ps -aux |grep memcached | wc -l'
else
    if [ $1 == 1 ]
    then
        rsync -rtvpl $SRC_PATH msms@$NETWORKCORE_IP:$DIS_DIR
    fi 
    ssh msms@$NETWORKCORE_IP 'cd /home/msms/run_memcached;bash networkcore.sh;bash networkcore.sh'
    echo "Networkcore:"$NETWORKCORE_IP
    ssh msms@$NETWORKCORE_IP 'hostname'
    echo 'memcached process number:'
    ssh msms@$NETWORKCORE_IP 'ps -aux |grep memcached | wc -l'
fi

#rsync -rtvpl /home/msms/codes/Repair_optimal/prototype/run_memcached msms@192.168.1.121:/home/msms
#ps -aux |grep memcached | wc -l
#ssh msms@192.168.1.114 'ps -aux |grep memcached | wc -l'