#different paramter
result_path='/home/msms/codes/Repair_optimal/result_xorbas.txt'
#1k
PLACEMENT_PLAN=('Flat' 'Random' 'Best_Placement')
PLACEMENT_NUM=${#PLACEMENT_PLAN[@]}
PLACEMENT_NUM=`expr $PLACEMENT_NUM - 1`

BLOCK_SIZE_ARRAY=(1 4 16 256 1024 4096)
NUM=${#BLOCK_SIZE_ARRAY[@]}
echo $NUM
NUM=`expr $NUM - 1`
NETWORKCORE_IP='10.0.0.61'
ssh msms@$NETWORKCORE_IP 'sudo ./wondershaper/wondershaper -c -a enp4s0f1'
ssh msms@$NETWORKCORE_IP 'sudo ./wondershaper/wondershaper -a enp4s0f1 -d 986710'
echo 'ssh msms@$NETWORKCORE_IP 'sudo ./wondershaper/wondershaper -a enp4s0f1 -d 986710''>>$result_path
RUN_TIMES=10
for i in $(seq 0 $NUM)
do
    block_size=${BLOCK_SIZE_ARRAY[$i]}
    n_k_r='12 8 4'
    bash main_mechine.sh 2
    for j in $(seq 0 $PLACEMENT_NUM)
    do
        placement=${PLACEMENT_PLAN[$j]}
        echo './prototype/cmake/build/client false Xorbas '$placement' '$n_k_r' '$block_size' '$RUN_TIMES''>>$result_path
        #./prototype/cmake/build/client false Xorbas $placement $n_k_r $block_size $RUN_TIMES
    done
     bash main_mechine.sh 0
done
ssh msms@$NETWORKCORE_IP 'sudo ./wondershaper/wondershaper -c -a enp4s0f1'

#different paramter,1M,4M
N_K_R_ARRAY=('16 10 5' '15 10 5' '10 6 3' '7 4 2')
NUM=${#N_K_R_ARRAY[@]}
echo $NUM
NUM=`expr $NUM - 1`
ssh msms@$NETWORKCORE_IP 'sudo ./wondershaper/wondershaper -c -a enp4s0f1'
ssh msms@$NETWORKCORE_IP 'sudo ./wondershaper/wondershaper -a enp4s0f1 -d 986710'
echo 'ssh msms@$NETWORKCORE_IP 'sudo ./wondershaper/wondershaper -a enp4s0f1 -d 986710''>>$result_path
for i in $(seq 0 $NUM)
do
    n_k_r=${N_K_R_ARRAY[$i]}
    block_size=1024
    bash main_mechine.sh 2
    for j in $(seq 0 $PLACEMENT_NUM)
    do
        placement=${PLACEMENT_PLAN[$j]}
        echo './prototype/cmake/build/client false Xorbas '$placement' '$n_k_r' '$block_size' '$RUN_TIMES''>>$result_path
        #./prototype/cmake/build/client false Xorbas $placement $n_k_r $block_size $RUN_TIMES
    done
    block_size=4096
    for j in $(seq 0 $PLACEMENT_NUM)
    do
        placement=${PLACEMENT_PLAN[$j]}
        echo './prototype/cmake/build/client false Xorbas '$placement' '$n_k_r' '$block_size' '$RUN_TIMES''>>$result_path
        #./prototype/cmake/build/client false Xorbas $placement $n_k_r $block_size $RUN_TIMES
    done
    bash main_mechine.sh 0
done
ssh msms@$NETWORKCORE_IP 'sudo ./wondershaper/wondershaper -c -a enp4s0f1'

#different bandwidth,1M,4M
Bandwidth_RATIO_ARRAY=(1 5 15 20)
Bandwidth_ARRAY=(9867100 1973420 657806 493355)

NUM=${#Bandwidth_RATIO_ARRAY[@]}
echo $NUM
NUM=`expr $NUM - 1`

for i in $(seq 0 $NUM)
do
    bandwidth=${Bandwidth_ARRAY[$i]}
    n_k_r='12 8 4'
    ssh msms@$NETWORKCORE_IP 'sudo ./wondershaper/wondershaper -c -a enp4s0f1'
    ssh msms@$NETWORKCORE_IP 'sudo ./wondershaper/wondershaper -a enp4s0f1 -d '$bandwidth
    echo 'ssh msms@'$NETWORKCORE_IP' 'sudo ./wondershaper/wondershaper -a enp4s0f1 -d ''$bandwidth''>>$result_path
    block_size=1024
    bash main_mechine.sh 2
    for j in $(seq 0 $PLACEMENT_NUM)
    do
        placement=${PLACEMENT_PLAN[$j]}
        echo './prototype/cmake/build/client false Xorbas '$placement' '$n_k_r' '$block_size' '$RUN_TIMES''>>$result_path
        #./prototype/cmake/build/client false Xorbas $placement $n_k_r $block_size $RUN_TIMES
    done
    block_size=4096
    for j in $(seq 0 $PLACEMENT_NUM)
    do
        placement=${PLACEMENT_PLAN[$j]}
        echo './prototype/cmake/build/client false Xorbas '$placement' '$n_k_r' '$block_size' '$RUN_TIMES''>>$result_path
        #./prototype/cmake/build/client false Xorbas $placement $n_k_r $block_size $RUN_TIMES
    done
    bash main_mechine.sh 0
    ssh msms@$NETWORKCORE_IP 'sudo ./wondershaper/wondershaper -c -a enp4s0f1'
done
