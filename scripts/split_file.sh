files=$(ls -la *_macd.csv | cut -d: -f2 | cut -d' ' -f2)

for file in $files; do
	#ok=$(grep 2018 $file)
	
        #if ! [ -z $ok ]; then
		grep -e "2017-" -e "2018-" -e date $file > ${file}_last.csv
	#echo ola
	#fi
done

