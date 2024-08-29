# Deploy a Streamlit Project   
There are 3 main processes invoolved in deploying an application   
1 . ***Installing python , Streamlit and other dependencies  in the deployment env***
#   
2 . ***Handling secrets and private information***
#   
3 . ***starting the application***   
#
## pip and requirement.txt   
You need to tell the container , if you are going to run the application via a container the dependencies   
You do this by "requirements.txt" file , save all your dependencies here   
~~~
pip freeze > requirements.txt

# if you want to be more specific
pandas==3.2.1 or streamlit => 3.1.4
~~~  
# Managing Secrets   
 Do not expose your keys or databases to the repo      
 