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
## Git Configuaration  
There will be some files/directories that you would want to track  
This is where the **".gitignore"** file comes in , you just put all the files/directories you do not want to be tracked  
How do you do it:  
1. Create a file named **".gitgnore "** 
2. add directory(s)/files  
## Branch , Merge and Configs  
With branching you are deviating from the timeline , making isolated changes from/to code without affecting the actual Code  
### Branch Commands  
1. Check Available Branch(s)  
~~~
git branch
~~~   
2. Create a New Branch  
~~~
git branch "yourBranchName"  
~~~  
3. Switch Branch(s)  
~~~
git branch checkout "desiredBranch"
~~~  
4. Create new Branch and Move to that branch  
~~~
git checkout -b "newBranchName"
~~~  
### Merging Branch(s)  
1. Fast-forward merge -> the Main/master is the only branchh that is not working/no changes  
#### Merging  
You need to go back to the master/Main branch first
 
2. Not Fast-forward merge -> all the branch(s) are changing simultaniously  
