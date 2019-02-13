files=$(ls -la *.csv | cut -d: -f2 | cut -d' ' -f2 | grep -v macd)
#echo $files
for file in $files; do
#	echo $file
	ok=$(find . -name ${file}_\*)
	oks=$(echo $ok | wc -w)
	#echo $oks
	#echo $ko

	if [ $oks = 4 ];then
#		echo $oks
#		echo $ko

		for ko in $ok; do

		#	echo $oks
		#	echo $ko
			d=$(echo $ko | cut -d/ -f2)
		#	echo $d
			mv $d moved
		#echo $file
	#	mv $d $file moved
		done
	fi
done

			
