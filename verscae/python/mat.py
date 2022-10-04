from rich import console; print = console.Console().print

import matplotlib.pyplot as plt

def main():
    print("Enter something : ", style="red", end="")
    arg1 = input()
    second(arg1)
    
def second(arg1):
    time = [0, 1, 2, 3]
    position = [0, 100, 200, 300]
    plt.plot(time, position)
    plt.xlabel('Time (hr)')
    plt.ylabel('Position (km)')
    plt.show()
    print("This is arg 1 : ", style="green", end="")
    print(f"{arg1}", style="red", end="\n")
main()