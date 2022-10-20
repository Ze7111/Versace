"""
This is the main installer script for the versace. It is responsible for
installing the versace and all of its dependencies. It is also responsible
for creating the versace executable. and adding it to PATH.
"""
# side-note this program was written in versace and decompiled to python

try:
    import rich
    import playsound
    import requests
    
except:
    print("Installing dependencies...")
    import os
    if os.name == "nt":
        try:
            ("pip install rich playsound requests")
        except:
            os.system("pip3 install rich playsound requests")
    elif os.name == "posix":
        try:
            os.system("pip3 install rich playsound requests")
        except:
            os.system("pip install rich playsound requests")
    elif os.name == "mac":
        try:
            os.system("pip3 install rich playsound requests")
        except:
            os.system("pip install rich playsound requests")
    else:
        print("Unsupported operating system.")
        exit()
        
    print("Dependencies installed!")
    

def main():
    import os, shutil, sys, requests
    from rich import console; print = console.Console().print
    
    osname = os.name
    os_names = {
        "nt" : "Windows",
        "posix" : "Linux",
        "mac" : "MacOS"
    }
    links = {
        "nt" : "https://github.com/Ze7111/Versace/releases/download/4.1.1/Windows-Versace-4.1.1.zip",
        "posix" : "https://github.com/Ze7111/Versace/releases/download/4.1.1/Linux-Versace-4.1.1.zip",
        "mac" : ""
    }
    
    if os.name == "mac":
        print("[bold red]MacOS is not supported yet.")
        print("[bold red]Please download the versace.py from the releases page. and put it in the same directory as where will run versace files from.")
        exit()
        
    if os.name in os_names:
        print(f"[bold green]Installing versace on {os_names[os.name]}...")
        print("[bold green]Is this correct? (y/n) : ", end="")
        choice = input()
        
        if choice == "y":
            pass
        
        else:
            print("[bold green]What is your operating system? [Windows/Linux/MacOS] : ", end="")
            choice = input()
            
            if choice == "Windows":
                osname = "nt"
            elif choice == "Linux":
                osname = "posix"
            elif choice == "MacOS":
                osname = "mac"    
            else:
                print("[bold red]Unsupported operating system.")
                exit()
    
    print("[bold red]Downloading versace...")
    versace = requests.get(links[osname])
    print("[bold green]Downloaded versace")
    # extract versace to current directory and then move it a directory that does not require admin permissions
    
    if os.name == "nt":
        open("Windows-Versace-4.1.1.zip", "wb").write(versace.content)
    elif os.name == "posix":
        open("Linux-Versace-4.1.1.zip", "wb").write(versace.content)
    else:
        print("[bold red]Unsupported operating system.")
        print("[bold red]How did you even make it this far?")
        exit()
        
    print("[bold red]Extracting versace...")
    if os.name == "nt":
        os.system("unzip Windows-Versace-4.1.1.zip")
    elif os.name == "posix":
        os.system("unzip Linux-Versace-4.1.1.zip")
    else:
        print("[bold red]Unsupported operating system.")
        print("[bold red]How did you even make it this far?")
        exit()
    print("[bold green]Extracted versace")
    
    print("[bold red]Moving versace...")
    # move the whole Windows-Versace-4.1.1 or Linux-Versace-4.1.1 to a directory that does not require admin permissions
    try:
        if os.name == "nt":
            shutil.move("Windows-Versace-4.1.1", f"C:\\users\\{os.getlogin()}\\AppData\\Local\\versace")
        elif os.name == "posix":
            shutil.move("Linux-Versace-4.1.1", "/usr/bin/Versace")
        else:
            print("[bold red]I dont even know how you got here.")
            exit()
    except Exception as e:
        print("[bold red]Failed to move versace.")
        print(f"[bold red]Error: {e}")
        pass
        
    print("[bold green]Moved versace")
    
    print("[bold red]Adding versace to PATH...")
    if os.name == "nt":
        os.system(f"setx PATH %PATH%;C:\\users\\{os.getlogin()}\\AppData\\Local\\versace")
    elif os.name == "posix":
        os.system("export PATH=$PATH:/usr/bin/Versace")
    else:
        print("[bold red]I dont even know how you got here.")
        exit()
    print("[bold red]Failed to add versace to PATH.")
    print(f"[bold red]Please add versace to PATH manually.")
    print(f"[bold green]The path is: C:\\users\\{os.getlogin()}\\AppData\\Local\\versace")
    exit()

    print("[bold green]Added versace to PATH")
    
    print("[bold green]Installed versace!")
    
    print("[bold green]To run versace, type 'versace' in your terminal.")
    print("[bold green]To run a versace file, type 'versace <filename>' in your terminal.")
    print("[bold green]To run a versace file with arguments, type 'versace <filename> <arguments>' in your terminal.")
    
main()