for (( i = 0 ; i <= 13 ; i++));
do
    if [ $i -lt 10 ]; then
        python3 crack.py ./flag0$i.zip
    else
        python3 crack.py ./flag$i.zip
    fi
done | grep  -oP "'\K[^']+" | tr -d '\n' > hasilCrack.txt