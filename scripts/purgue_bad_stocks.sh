
cd csv_files

files=$(ls -la *.csv | cut -d: -f2 | cut -d' ' -f2)

for file in $files; do
		#TR_files=$(grep "42d" $file)
    last_line=$(awk '/./{line=$0} END{print line}' $file | sed 's/  /,/g' | sed 's/,,/,/g')
    line_252_trend=$( echo $last_line | cut -d, -f11 |  awk '{printf("%d\n",$1 + 0.5)}'  )
    line_42_trend=$( echo $last_line | cut -d, -f10 | awk '{printf("%d\n",$1 + 0.5)}'  )
    line_close=$( echo $last_line | cut -d, -f5 | awk '{printf("%d\n",$1 + 0.5)}'  )
    five_days_ago=$(tail -5 $file | head -5 | awk 'NR == 1' | cut -d, -f5| awk '{printf("%d\n",$1 + 0.5)}')
    thirty_days_ago=$(tail -30 $file | head -30 | awk 'NR == 1' | cut -d, -f5| awk '{printf("%d\n",$1 + 0.5)}')
    line_macds=$( echo $last_line | cut -d, -f13 |  awk '{printf("%d\n",$1 + 0.5)}'  )
    line_rsi=$( echo $last_line | cut -d, -f18 | awk '{printf("%d\n",$1 + 0.5)}'  )

    if [ -z $(grep "42d" $file) ];then
      if [ $line_rsi -gt 70 ] ||  [ $line_rsi -lt 30 ] || [ $line_macds -lt 0 ]; then
          echo $file
      #other=$(echo $file | sed "s/TR_//g")
      #rm $other
          rm $file
      fi
    else
      if [ $five_days_ago -gt $line_close ] || [ $thirty_days_ago -gt $line_close ] || [ $line_252_trend -gt $line_42_trend ]; then
          # other=$(echo $file | sed "s/TR_//g")
          #
          # if [ ! -z $( find . -name $other) ]; then
          #   rm $other
          # fi
          echo $file
          rm $file
                #echo $line_252_trend $line_42_trend
      fi
      # if ; then
      # #          other=$(echo $file | sed "s/TR_//g")
      # #          rm $othe
      #     echo $file
      #     rm $file
      #           #echo $line_252_trend $line_42_trend
      # fi
      # if ; then
      #     other=$(echo $file | sed "s/TR_//g")
      #     rm $other
      #     echo $file
      #     rm $file
      #           #echo $line_252_trend $line_42_trend
      # fi
    fi

done
