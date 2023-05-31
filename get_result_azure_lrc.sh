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
# start_close_memcached 1
result_path='/home/msms/codes/Repair_optimal/result_azure_lrc.txt'
RUN_TIMES=5
NETWORKCORE_IP='10.0.0.61'
PLACEMENT_PLAN=('Best_Placement' 'Random' 'Flat')
PLACEMENT_NUM=${#PLACEMENT_PLAN[@]}
PLACEMENT_NUM=`expr $PLACEMENT_NUM - 1`
#different paramter
#1k
BLOCK_SIZE_ARRAY=(1 4 16 256 1024 4096)
BLOCK_SIZE_NUM=${#BLOCK_SIZE_ARRAY[@]}
echo $BLOCK_SIZE_NUM
BLOCK_SIZE_NUM=`expr $BLOCK_SIZE_NUM - 1`
ssh msms@$NETWORKCORE_IP 'sudo ./wondershaper/wondershaper -c -a enp4s0f1'
ssh msms@$NETWORKCORE_IP 'sudo ./wondershaper/wondershaper -a enp4s0f1 -d 986710'
echo '#different size'>>$result_path
echo 'ssh msms@$NETWORKCORE_IP 'sudo ./wondershaper/wondershaper -a enp4s0f1 -d 986710''>>$result_path
# ENCODE_TYPE='Xorbas'
ENCODE_TYPE='Azure_LRC'
# ENCODE_TYPE='Azure_LRC_1'
n_k_r='16 12 6'
# n_k_r='17 12 6'

for i2 in $(seq 0 $BLOCK_SIZE_NUM)
do
    block_size=${BLOCK_SIZE_ARRAY[$i2]}
    start_close_memcached 0
    start_close_memcached 2
    for j2 in $(seq 0 $PLACEMENT_NUM)
    do 
        #sleep 10s   
        placement=${PLACEMENT_PLAN[$j2]}
        pkill -9 client
        echo './prototype/cmake/build/client true '$ENCODE_TYPE' '$placement' '$n_k_r' '$block_size' '$RUN_TIMES''>>$result_path
        echo './prototype/cmake/build/client true '$ENCODE_TYPE' '$placement' '$n_k_r' '$block_size' '$RUN_TIMES''
        ./prototype/cmake/build/client true $ENCODE_TYPE $placement $n_k_r $block_size $RUN_TIMES $result_path     
    done
done
ssh msms@$NETWORKCORE_IP 'sudo ./wondershaper/wondershaper -c -a enp4s0f1'

#different paramter,1M,4M
# N_K_R_ARRAY=('16 10 5' '15 10 5' '10 6 3' '7 4 2')
N_K_R_ARRAY=('12 6 3' '16 10 5' '18 12 5' '24 15 5')
#N_K_R_ARRAY=('12 6 3' '15 10 5' '18 12 5' '24 15 5')
N_K_R_NUM=${#N_K_R_ARRAY[@]}
echo $N_K_R_NUM
N_K_R_NUM=`expr $N_K_R_NUM - 1`
ssh msms@$NETWORKCORE_IP 'sudo ./wondershaper/wondershaper -c -a enp4s0f1'
ssh msms@$NETWORKCORE_IP 'sudo ./wondershaper/wondershaper -a enp4s0f1 -d 986710'
echo '#different parameter'>>$result_path
echo 'ssh msms@$NETWORKCORE_IP 'sudo ./wondershaper/wondershaper -a enp4s0f1 -d 986710''>>$result_path
for i3 in $(seq 0 $N_K_R_NUM)
do
    n_k_r=${N_K_R_ARRAY[$i3]}
    block_size=1024  
    for j3 in $(seq 0 $PLACEMENT_NUM)
    do
        start_close_memcached 0
        start_close_memcached 2
        placement=${PLACEMENT_PLAN[$j3]}
        pkill -9 client
        echo './prototype/cmake/build/client true '$ENCODE_TYPE' '$placement' '$n_k_r' '$block_size' '$RUN_TIMES''>>$result_path
        echo './prototype/cmake/build/client true '$ENCODE_TYPE' '$placement' '$n_k_r' '$block_size' '$RUN_TIMES''
        ./prototype/cmake/build/client true $ENCODE_TYPE $placement $n_k_r $block_size $RUN_TIMES $result_path
    done
    block_size=4096
    for j3 in $(seq 0 $PLACEMENT_NUM)
    do
        start_close_memcached 0
        start_close_memcached 2
        placement=${PLACEMENT_PLAN[$j3]}
        pkill -9 client
        echo './prototype/cmake/build/client true '$ENCODE_TYPE' '$placement' '$n_k_r' '$block_size' '$RUN_TIMES''>>$result_path
        echo './prototype/cmake/build/client true '$ENCODE_TYPE' '$placement' '$n_k_r' '$block_size' '$RUN_TIMES''
        ./prototype/cmake/build/client true $ENCODE_TYPE $placement $n_k_r $block_size $RUN_TIMES $result_path
    done
done
ssh msms@$NETWORKCORE_IP 'sudo ./wondershaper/wondershaper -c -a enp4s0f1'

#different bandwidth,1M,4M
Bandwidth_RATIO_ARRAY=(1 5 15 20)
Bandwidth_ARRAY=(9867100 1973420 657806 493355)
n_k_r='16 12 6'

Bandwidth_ARRAY_NUM=${#Bandwidth_ARRAY[@]}
Bandwidth_ARRAY_NUM=`expr $Bandwidth_ARRAY_NUM - 1`
echo '#different bandwidth'>>$result_path
for i4 in $(seq 0 $Bandwidth_ARRAY_NUM)
do
    bandwidth=${Bandwidth_ARRAY[$i4]}
    ssh msms@$NETWORKCORE_IP 'sudo ./wondershaper/wondershaper -c -a enp4s0f1'
    ssh msms@$NETWORKCORE_IP 'sudo ./wondershaper/wondershaper -a enp4s0f1 -d '$bandwidth
    echo 'ssh msms@'$NETWORKCORE_IP' 'sudo ./wondershaper/wondershaper -a enp4s0f1 -d ''$bandwidth''>>$result_path
    echo 'ssh msms@'$NETWORKCORE_IP' 'sudo ./wondershaper/wondershaper -a enp4s0f1 -d ''$bandwidth''
    block_size=4096
    for j4 in $(seq 0 $PLACEMENT_NUM)
    do
        echo j4
        echo $j4  
        start_close_memcached 0
        start_close_memcached 2
        placement=${PLACEMENT_PLAN[$j4]}
        pkill -9 client
        echo './prototype/cmake/build/client true '$ENCODE_TYPE' '$placement' '$n_k_r' '$block_size' '$RUN_TIMES''>>$result_path
        echo './prototype/cmake/build/client true '$ENCODE_TYPE' '$placement' '$n_k_r' '$block_size' '$RUN_TIMES''
        ./prototype/cmake/build/client true $ENCODE_TYPE $placement $n_k_r $block_size $RUN_TIMES $result_path
    done
done
ssh msms@$NETWORKCORE_IP 'sudo ./wondershaper/wondershaper -c -a enp4s0f1'
start_close_memcached 0
