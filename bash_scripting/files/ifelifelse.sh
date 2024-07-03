#!/usr/bin/bash

if [ ${1,,} = billy ]; then
	echo "Hi billy , welcome"
elif [ ${1,,} = abongile ]; then
	echo "We are the Pycentric , how can we help you?"
else
	echo "You dont have admin right to be here"
fi
