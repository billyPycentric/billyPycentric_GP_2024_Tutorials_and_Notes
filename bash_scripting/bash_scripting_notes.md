
# Bash Scripting Notes
## Vim Navigation
1. Create and Open a file in vim
~~~
// vim filename plus extention
vim names.txt
~~~
2. Edit Contents of the File   
* i - for insert -> edit contents
* esc in windows   
* : w  , to write the contents of the file   
* : q to quit   
* :wq to write and quit   
    
## Creating the first .sh script   
1. run vim with "filename".sh   
~~~
vim shelltest.sh
~~~   
2. To automatically make the script a bash script   
~~~bash
run echo $SHELL 
# you will see the output 

{/usr/bin/bash} -> go into you .sh script and add "#!" before the line
// the line after adding the "#!"

#!/usr/bin/bash

~~~   
3. Give the .sh executable permission   
~~~bash
chmod u+x filename.sh   

~~~   
4. Now you can run the .sh files with ./filename.sh command   
## Creating an Interactive shell
~~~bash
echo -> display
read -> interact with shell
~~~   
How it would look like   
~~~bash
#!/usr/bin/bash

echo Enter your first name
read $FIRSTNAME

echo Enter your last name
read $LASTNAME

echo Hi there $FIRSTNAME $LASTNAME
~~~
Remember to use :   
~~~ bash
chmod u+x filename.sh  , for executing bin/executables
~~~   
## Positional Arguments   
Args that are taken along with the .sh command   
~~~bash
// suposed you .sh file looks like this
#!/usr/bin/bash
echo My name is $1 $2 , $1 $2 -> these will be your pos_arg
~~~
expected output:   
~~~
./filename.sh Abongile Billy -> Abongile being $1 and Billy being $2

// output:

My name is Abongile Billy

~~~   
## Pipping   
>pipe is used to combine two or more commands   

you can filter using pipping i.e grep -> used to filter and show out put
1st - command == ls
2nd - command == grep   
### Pipping in Action   
Suppose we wanted to use this command   
~~~bash
ls -l usr/bin
# this command list all the list of directories/files in the usr/bin path
~~~
So with ***PIPPING*** we would use :   
~~~bash
ls -ls usr/bin | grep bash
~~~
## Output Redirection   
1. writing to a file >   
2. appending a file >>   
i.e :
~~~bash
echo I am learning bash > bash.txt

echo i am appending to the bash.txt file >> bash.txt
~~~   
### feed input into a command by using :   
1. <  
~~~bash
wc -w filename.txt

# it will return number of chars in available in the file

then 

wc -w filename.txt 

# it will only return the number of chars now
~~~
2. <<   
~~~bash 
cat << EOF 

expected output:
> ""
>""
>""
>""
EOF it will end the text

~~~  

3. <<<  
~~~bash
wc -w <<< "Hi billy"

# it will show the number of letters
~~~   
## Test Opperator   
Comparing if two or more vars are -eq   
~~~bash
[ hello = hello ]

#to check if -eq
echo $?
~~~
This will help if ***if , elif , else*** statements   
## ***if , elif , else***   
> Using ***if*** stament  
if [ hello = hello ]; then  
      echo "they are equal"   
fi  
 or   
if [ ${1,,} == billy ]; then
     echo "Welcome billy"   
fi   

**NB** Always add fi after last line of statements
### DEMO On Using all Test Statements   
~~~bash
//#!/usr/bin/bash

if [ ${1,,} = billy ]; then
    echo "Welcome Again Mr Billy , Do you want Coffee"

elif [ ${1,,} = --help ]; then
    echo "You chode the help OPTION , how can we help you"

else
     echo "You dont have any access , please excuse yourself"  

fi
#fi means EOF -> end of file
#Basically here what happens is that , check first for billy if TRUE show statement , then check for --help if TRUE statement AND id NOT(billy && --help) , You are an intruder
~~~   
## Case Statements   
Is an advanced ***if ,elif ,else*** statement   
Here is the demonstration :  
~~~bash
"#!/usr/bin/bash"
case ${1,,} in 
    abongile | billy | lord)
        echo "Welcome , my Lord , How are you"
        ;;
    help | --help)
        echo "Please talk to the administrator"
        ;;
    *)
        echo "Police are on the way , You FRAUD"

esac
~~~   
## Arrays | Lists   
how to declare:   
~~~bash

LIST_OF_NAMES=(abo jane thato thabo funa mercy)

# Then if you want to DISPLAY
echo $LIST_OF_NAMES  -> dislay only the first one

# for displaying the entire list
echo ${LIST_OF_NAMES[@]}

# for a certain index only
echo ${LIS_OF_NAMES[n]} , where n is the desired index
~~~      
### Traverse through List using ***for loop***   
1. Declare your list   
~~~ bash
MY_LIST_OF_TERMINALS=(powershell gitBash ubuntu cmd AzureCloud)
~~~   
2. Use a loop to traverse   
~~~bash
for item in ${MY_LIST_OF_TERMINALS[@]};do echo $item;done
## expected output
powershell
gitBash
ubuntu
cmd
AzureCloud
~~~   
3. Getting rid of spaces   
~~~
for item in ${LIST_OF_TERMINALS[@]};do echo -n $item;done
# -n gets rid of space/lines

## expected output
powershellgitBashubuntucmdAzureCloud
~~~   
4. So if you want to add **MORE CONDITIONS TO THE LOOP** this is the structure :   
~~~bash
for $ in ${LIST[@]};do something;do this;do that;done

## at the end of the last statement add ;done
~~~   
## Functions
Structure   
~~~bash
myfunc(){
    # list of things to be done
    #i.e display list of items
    MY_LIST=(1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19)   
    for item in ${MY_LIST[@]};do echo $item;done
    echo "I am done my good sir"
}
myfunc
~~~   


