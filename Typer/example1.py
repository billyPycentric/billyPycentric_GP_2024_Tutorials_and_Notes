import typer

def main(name : str, surname : str = "", formal: bool = False):
    if formal:
        print(f"Your name is  {name}  and your surname is {surname}")
    else:
        print(f"Your numbers are  {name}   {surname} maDawg")
    

if __name__ == "__main__":
    typer.run(main)