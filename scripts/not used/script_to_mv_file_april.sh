files=$(ls -la *_last.csv | cut -dy -f2 | cut -d' ' -f5)
echo $files
for file in $files; do
	echo $file
	ok=$(find . -name ${file}_*)
	echo $ok
	if ! [ -z $ok ];then
		d=$(echo $ok | cut -d/ -f2)
		echo $d
		echo $file
		mv $d $file moved
	fi
done

			
