# Typer   
simplifies CLI built applications -> helps you to build CLI appliations   
### How to Use It   
1. Create a Venv   
~~~
# go to the dir you want to create the venv in
c~ python3 -m venv venv 
~~~   
2. Install the Typer library   
~~~
pip install typer
~~~       
~~~python
import typer

def main(name : str, surname : str = "", formal: bool = False):
    if formal:
        print(f"Your name is  {name}  and your surname is {surname}")
    else:
        print(f"Your numbers are  {name}   {surname} maDawg")
    

if __name__ == "__main__":
    typer.run(main)
~~~
