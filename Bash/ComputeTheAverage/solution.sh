read lines
sum=0
for i in $(seq 1 $lines);
do
    read n
    sum=$(($sum+$n))
done;
printf "%.3f" $(echo "$sum / $lines" | bc -l)
