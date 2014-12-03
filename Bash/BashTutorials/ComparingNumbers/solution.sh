read x
read y
if [ $x -gt $y ]; then
    echo "X is greater than Y"
elif [ $x -eq $y ]; then
    echo "X is equal to Y"
else
    echo "X is lesser than Y"
fi
