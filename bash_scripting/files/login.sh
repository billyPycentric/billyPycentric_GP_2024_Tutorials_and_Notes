#!/usr/bin/bash

case ${1,,} in 
	abongile | billy | tebogo)
		echo "Welcome , my Lord How are You"
		;;
	help | --help)
		echo "Please try to contact the admin"
		;;
	*)
		echo "You are a froud , plice are on their Way"
esac
