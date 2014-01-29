# !/bin/bash
#'xor2.txt' 'nand2.txt' 'nor2.txt' 'pal_input' 'seven_input' 'majority_input' 'parity_input')
mkdir -p data
files=('xor2.txt')
for i in "${files[@]}"
do
	echo $i
	outputFile=data/output_$i
	rm -f $outputFile
	for j in `seq 1 9`;
	do
		echo $j
		eta=$(bc <<< "scale=1; 0.1*$j")
		python prop.py $i $eta >> $outputFile
	done
done
