files=$(ls -la *.csv | cut -dj -f2 | cut -d' ' -f4)

for file in $files; do
	ok=$(tail -n 2 $file | grep -e ",0." -e ",1\." -e ",2\.")
	
	if [ ! -z "$ok" ]; then
		echo $file
		mv $file bad_stocks/	
	#	contra=$( tail $file | grep -e ",3." -e ",4." -e ",5." -e ",6." -e ",7." -e ",8." -e ",9.")
	#	if [ -z "$contra" ]; then
	#		echo $file
	#		mv $file bad_stocks/
	#	fi
        fi	       
done
