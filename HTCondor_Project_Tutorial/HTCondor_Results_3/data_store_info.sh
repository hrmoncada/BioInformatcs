#!/bash/sh
condor_history  ClusterId = 145798 >> data_history_145798_1_12.txt
echo "Press any key to continue..."
read -n1 -t5 any_key
condor_history -constraint "CompletionDate > 0" -af Owner 145798 ProcId  RemoteUserCpu  RemoteWallClockTime CumulativeSlotTime CommittedTime QDate EnteredCurrentStatus CompletionDat >> data_time_145798_1_12.txt
echo "Data have been store"
