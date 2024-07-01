# Git Notes
## Git Initialization
### Initialize Directory
Before you try use **git** commands you need to initialize your Repo using the command :  
1. Turning your Current Directory into a Repo  
~~~
git init
~~~
2. Making a new Repo  
~~~
git init "Your desired Repo Name"
~~~  
**NB** : **You Only Use The "git init" command once**  
### Git Important Concepts
Every File/Diretory that is inside your Repo will be tracked , and it is good practice  to ***ALWAYS*** check the changes you make to a file/directory use the command :  
~~~
# checking the changes
git status 
~~~
And There is also a "COMMIT" command , the command here is responsible for committing code Here is how you write/use it:  
~~~
git commit -m "Your commit"
~~~
**Do not forget the -m tag "" , it is going to help you to track the commit**

Also "ADD" command , the command lets to to add the file/directory into the staging area -> **Tracked** , here is how you use it :  
1. Adding ***all*** files/directory into staging area
~~~
git add .
~~~
2. Adding ***Only 1 file***  
~~~
git add "filename"
~~~
**NB** Always try to add one file at the time for tracking to be easier

Also remember this flow:  
Simple Version:
```
   Write-->Add-->Commit
```
Full Version:  
```
    Working Dir-->git add-->Staging Area-->git commit-->Repo-->git push-->github
```  
## Git Commits and Logs  
Logs helps with with project history , displays snapshots of a commits:  
1. Listing all logs  
~~~
git log
~~~
![Git logs](https://drive.google.com/drive/folders/1FiM_fX5k81ntiPhRHeckOI1uIBIHOYl9)  
Logs structure is usually:
* Author -> who wrote the code
* commit -> commit Id  
* commit message -> commit message  
2. Summary of Log  
 ![git log]() 
~~~
git log --oneline
~~~