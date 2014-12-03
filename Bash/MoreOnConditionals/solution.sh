read x
read y
read z

if [ $x -eq $y ]; then
    if [ $y -eq $z ]; then
        echo "EQUILATERAL"
    else
        echo "ISOSCELES"
    fi
else
    echo "SCALENE"
fi
