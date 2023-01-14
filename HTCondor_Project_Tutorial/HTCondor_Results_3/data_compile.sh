#!/bash/sh
cd OUTPUT/
ls  -l
echo "Press any key to continue..OPEN OUTPUT"
read -n1 -t5 any_key
vi  output_1.txt
echo "Press any key to continue-ERASE FOLDER"
read -n1 -t5 any_key
rm output_*.txt
cd ..
echo "Press any key to continue..OPEN BLAST OUTPUT."
read -n1 -t5 any_key
cd BLAST_OUTPUT/
ls -l
echo "Press any key to continue..."
read -n1 -t5 any_key
vi  blast_output_6_1.out
echo "Press any key to continue-ERASE FOLDER"
read -n1 -t5 any_key
rm  blast_output_*.*
cd ..
echo "Folders OUTPUT and BLAS_OUTPUT are clean"
