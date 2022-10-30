#include <cstdlib>
#include <iostream>
#include <stdlib.h>
#include <string>

using namespace std;

const string R_Version = "4.6.6";

const string L_Link = "https://github.com/Ze7111/Versace/releases/latest/download/LinuxVersace";
const string W_Link = "https://github.com/Ze7111/Versace/releases/latest/download/WindowsVersace";

const string Final_Link_W = W_Link + R_Version + ".zip";
const string Final_Link_L = L_Link + R_Version + ".zip";

const string Win_F_Name = "WindowsVersace" + R_Version + ".zip";
const string Lin_F_Name = "LinuxVersace" + R_Version + ".zip";

const string Win_F_DIR = "WindowsVersace" + R_Version;
const string Lin_F_DIR = "LinuxVersace" + R_Version;

void WIN_INSTALLER(string osname, string colors[5])
{

    string x; string SETPATHX = "[Environment]::SetEnvironmentVariable(\"Path\", [Environment]::GetEnvironmentVariable(\"Path\", \"User\") + \";$HOME\\versace\\" + Win_F_DIR + "\", \"User\")"; // Set Path
    
    cout << colors[0] << "\n\nPlease copy the following command all together\n" << endl;
    cout << colors[3] << "New-Item \"$HOME\\versace\" -ItemType \"directory\" -Force" << endl;
    cout << colors[3] << "Invoke-WebRequest \""+ Final_Link_W +"\" -OutFile \"$HOME\\versace\\versace.zip\"" << endl;
    cout << colors[3] << "Expand-Archive \"$HOME\\versace\\versace.zip\" -DestinationPath \"$HOME\\versace\" -Force" << endl;
    cout << colors[3] << "Remove-Item \"$HOME\\versace\\versace.zip\" -Force" << endl;
    cout << colors[3] << "[Environment]::SetEnvironmentVariable(\"Path\", [Environment]::GetEnvironmentVariable(\"Path\", \"User\") + \";$HOME\\versace\\" + Win_F_DIR + "\", \"User\")" << endl;
    cout << colors[0] << "\nPress Enter to continue once you have copied the command ";
    
    system("pause >nul");
    system("cls");
    
    cout << colors[0] << "Please paste the copied commands into a non-administrator PowerShell window. then you can use versace" << endl;
    cout << colors[4];
    
    exit(0);
}

void LIN_INSTALLER(string osname, string colors[5])
{
    string x; string SETPATHX = "export PATH=$PATH:$HOME/versace/" + Lin_F_DIR; // Set Path
    
    cout << colors[0] << "\n\nPlease copy the following command all together\n" << endl;
    cout << colors[3] << "mkdir $HOME/versace" << endl;
    cout << colors[3] << "wget -O $HOME/versace/versace.zip " + Final_Link_L << endl;
    cout << colors[3] << "unzip $HOME/versace/versace.zip -d $HOME/versace" << endl;
    cout << colors[3] << "rm $HOME/versace/versace.zip" << endl;
    cout << colors[3] << "export PATH=$PATH:$HOME/versace/" + Lin_F_DIR << endl;
    cout << colors[0] << "\nPress Enter to continue once you have copied the command ";
    
    system("pause >nul");
    system("clear");
    
    cout << colors[0] << "Please paste the copied commands into a terminal. then you can use versace" << endl;
    cout << colors[4];
    
    exit(0);
}

void CAR(string osname, string LatestReleaseTag, string WindowsLink, string LinuxLink)
{
    // make a list of 3 color codes
    string colors[5] = {"\033[1;31m", "\033[1;32m", "\033[1;34m", "\033[1;33m", "\033[0m"};
    //                     red          green          blue         yellow        reset
    if (system("cls")) system("clear"); // clear the screen
    
    cout << colors[0] << "Welcome to the Versace Installer" << colors[4] << endl; // print the welcome message
    cout << colors[1] << "Your Operating System is: " << colors[3] << osname << colors[4] << endl; // print the os name
    cout << colors[1] << "Latest Release Tag: " << colors[3] << LatestReleaseTag << colors[4] << endl; // print the latest release tag
    cout << colors[1] << "Windows Link: " << colors[3] << WindowsLink << colors[4] << endl; // print the windows link
    cout << colors[1] << "Linux Link: " << colors[3] << LinuxLink << colors[4] << endl; // print the linux link
    cout << colors[1] << "Windows File Name: " << colors[3] << Win_F_Name << colors[4] << endl; // print the windows file name
    cout << colors[1] << "Linux File Name: " << colors[3] << Lin_F_Name << colors[4] << endl; // print the linux file name

    if (osname == "Windows") { WIN_INSTALLER(osname, colors); } // if the osname is Windows run the Windows installer Function
    else if (osname == "Linux") { LIN_INSTALLER(osname, colors); } // if the osname is Linux run the Linux installer Function
    else { cout << colors[0] << "Your Operating System is not supported" << colors[4] << endl; exit(0); } // if the osname is not supported exit the program
}

void CIUHVI() // Check if the user has Versace installed
{   
    string choice;
    string colors[5] = {"\033[1;31m", "\033[1;32m", "\033[1;34m", "\033[1;33m", "\033[0m"};
    //                     red          green          blue         yellow        reset
    cout << colors[3] << "Checking if Versace is installed..." << endl;
// [Environment]::SetEnvironmentVariable(\"Path\", [Environment]::GetEnvironmentVariable(\"Path\", "User\") + \";$HOME\\Versace\\" + "Win_F_Name + "\", \"User\")"
    // check if the versace -version command works
    if (system("versace -version") == 0) {   
        cout << colors[1] << "Latest Version: " << colors[0] << R_Version << endl;
        // ask if the user wants to update
        cout << colors[3] << "Do you want to update? (y/n): " << colors[2];
        cin >> choice;

        if (choice == "y") {
            cout << colors[4];
            return;
        
        } else {
            // exit
            cout << colors[4];
            exit(0);
        }
    }  
    
    else  {
        cout << colors[0] << "Versace will be installed." << endl;
        cout << colors[4];
        return; 
    }
}

int main()
{
    // clear screen
    if (system("cls")) system("clear");

    // Initialize variables
    string LatestReleaseTag = R_Version;
    string WindowsLink = Final_Link_W;
    string LinuxLink = Final_Link_L;

    // check what the OS is
    string osname = "Windows";    

    CIUHVI(); // CIUHVI = Check if the user has Versace installed

    // check if the OS is supported if so, reroute to the correct function
    CAR(osname, LatestReleaseTag, WindowsLink, LinuxLink); // CAR = Check And Redirect
    
    return 0; // exit
}


/*
New-Item "$HOME\versace" -ItemType "directory" -Force
Invoke-WebRequest "https://github.com/Ze7111/Versace/releases/latest/download/Windows-Versace-4.6.6.zip" -OutFile "$HOME\versace\versace.zip"
[Environment]::SetEnvironmentVariable("Path", [Environment]::GetEnvironmentVariable("Path", "User") + ";$HOME\versace", "User")
*/
