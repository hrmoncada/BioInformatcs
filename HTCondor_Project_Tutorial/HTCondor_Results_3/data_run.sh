#!/bash/sh
vi Split_Sequence_bigger_chucks.py
echo "Press any key to continue..."
read -n1 -t5 any_key
python Split_Sequence_bigger_chucks.py
echo "Chunking the data is Finish"
echo "Press any key to continue..."
read -n1 -t5 any_key
vi  blastp_submit2_sweep
echo "Ready to submit jobs on the pool"
echo "Press any key to continue..."
read -n1 -t5 any_key
condor_submit blastp_submit2_sweep
echo "Submition is done!!"
