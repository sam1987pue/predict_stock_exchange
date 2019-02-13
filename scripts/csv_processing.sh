cp -R ../../workspace/Get\ data\ from\ Pandas/csv_files .

cd csv_files

files=$(ls -la *.csv | cut -d: -f2 | cut -d' ' -f2)


for file in $files; do

	ok=$(tail -n 2 $file | grep -e ",0." -e ",1\." -e ",2\." -e ",3\." -e ",4\." -e ",5\." -e ",6\.") || true
	ok_two=$(tail -n 2 $file | cut -d, -f5 | head -n1 | awk '{print int($1+0.5)}') || true
	if [ ! -z "$ok" ]; then
		rm $file
        echo "removing $file"
    elif [ "$ok_two" -gt 100 ]; then
    	rm $file
        echo "removing $file"
    else
    	columns="0 30 70"
    	for column in $columns; do
    		sed -i "s/$/,$column/g" $file
        done
    fi
done
