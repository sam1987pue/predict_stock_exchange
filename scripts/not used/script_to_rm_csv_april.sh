files=$(ls -la *csv | cut -da -f2 | cut -d' ' -f4-)
for file in $files; do
	ok=$(find /home/linux/mercadovalores/nasdaqhistoric -name ${file}.png)
	#echo $ok
	if  [ -z $ok ];then
		echo $file
		rm $file
#		d=$(echo $ok | cut -d/ -f7-)
#		echo $d
#		echo $file
#		mv $d $file /home/linux/mercadovalores/nasdaqhistoric/historic26.04/moved
	fi
done

			
