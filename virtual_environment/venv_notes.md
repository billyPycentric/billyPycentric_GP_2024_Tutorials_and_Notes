# Creation of a Virtual Environments - venv   
**venv** module support creating light-weight virtual environments , and has its only separate set of ***Python packages*** which are independent of the base Python installation and ***pip*** is one of the tools used to install those packages   
venv is :   
* located at the same directory as the project
* Contains all the lib and bin files needed to run the project   
* Not tracked by bit , ussually has venv or .venv   
* Cannot be moved , can also be deleted and started from scratch   
## Create a Virtual Environment   
~~~
//  run the command
python -m venv venv
 // This will create the target folder with pyvenv.cfg and executables that will be needed during run time
~~~   
You invoke the environment by   
~~~
// using powershell
.venv/Scripts/activate  , then enter
~~~   
### Install dependencies and Deactivate  
~~~
 python -m pip install <package-name> # install

deactivate  # deactivating it
~~~    
## Why Venv   
* Side step dependency conflicts
* avoid installing privilages   
* Helps with dependency relevancy
* Avoid System Pollution    

Python virtual environments aim to provide a lightweight, isolated Python environment that you can quickly create and then discard when you don’t need it anymore. The folder structure that you’ve seen above makes that possible by providing three key pieces: 
~~~
A copy or a symlink of the Python binary
A pyvenv.cfg file
A site-packages directory
~~~

