#!/usr/bin/bash

myfunc(){
	MY_NUMBERS=(1 2 3 4 5 6 7 8 9 11 12 13 14 15 16 17 18)
	for item in ${MY_NUMBERS[@]};do echo $item;done
	echo "And Tjose are you numbers my Good sir"

}
myfunc
