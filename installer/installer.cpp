#include <iostream>
#include <stdlib.h>
// module for downloading files from the internet
using namespace std;

void WindowsInstall(string Link)
{
    string boldGreen("\033[1;32m"); // bold green
    string boldRed("\033[1;31m"); // bold red
    string reset("\033[0m"); // reset
    
    cout << boldRed << "Downloading Versace for Windows" << reset << endl; // prints "Downloading Versace for Windows"
    
    // download from the link into the current directory
    cout << boldRed;
    system("powershell ((new-object System.Net.WebClient).DownloadFile('https://github.com/Ze7111/Versace/releases/download/4.1.1/Windows-Versace-4.1.1.zip','Versace.zip'))");
    cout << boldGreen << "Downloaded Versace.zip" << reset << endl;
    
    cout << boldRed;
    // extract the zip file into the current directory without using unzip or 7zip command
    system("powershell Expand-Archive -Force 'Versace.zip' 'Versace'");
    cout << boldGreen << "Extracted Versace.zip" << reset << endl;
    
    // inside the new Versace folder, thre is a Windows-Versace-4.1.1 folder move that to a directory that does not require admin permissions
    cout << boldRed;
    system("powershell Move-Item -Path 'Versace/Windows-Versace-4.1.1' -Destination '%AppData%/Versace'");
    cout << boldGreen << "Moved Versace to %%AppData%%/Versace" << reset << endl;

    // delete the zip file and the Versace folder
    cout << boldRed;
    system("powershell Remove-Item -Path 'Versace.zip'");
    system("powershell Remove-Item -Path 'Versace' -Recurse");
    cout << boldGreen << "Deleted Versace.zip and Versace folder" << reset << endl;
    
    // add the new Versace folder to the path permanently so that it can be run from anywhere
    cout << boldRed; 
    cout << boldGreen << "Failed to add Versace to the path" << reset << endl; 
    
    // exit
    cout << boldGreen << "Please add Versace to the path manually, it is located in 'C:\\Users\\(USERNAME)\\AppData\\Roaming\\Versace'" << reset << endl;
}

void LinuxInstall(string Link)
{
    string boldGreen("\033[1;32m"); // bold green
    string boldRed("\033[1;31m"); // bold red
    string reset("\033[0m"); // reset
    
    cout << boldRed << "Downloading Versace for Linux" << reset << endl; // prints "Downloading Versace for Linux"
    
    // download from the link into the current directory
    cout << boldRed;
    system("wget https://github.com/Ze7111/Versace/releases/download/4.1.1/Linux-Versace-4.1.1.zip");
    cout << boldGreen << "Downloaded Linux-Versace-4.1.1.zip" << reset << endl;
    
    cout << boldRed;
    // extract the zip file into the current directory without using unzip or 7zip command
    system("unzip Linux-Versace-4.1.1.zip");
    cout << boldGreen << "Extracted Linux-Versace-4.1.1.zip" << reset << endl;
    
    // inside the new Versace folder, thre is a Linux-Versace-4.1.1 folder move that to a directory that does not require admin permissions
    cout << boldRed;
    system("mv Linux-Versace-4.1.1 ~/.Versace");
    cout << boldGreen << "Moved Versace to ~/.Versace" << reset << endl;
    
    // delete the zip file and the Versace folder
    cout << boldRed;
    system("rm Linux-Versace-4.1.1.zip");
    system("rm -r Linux-Versace-4.1.1");
    cout << boldGreen << "Deleted Linux-Versace-4.1.1.zip and Linux-Versace-4.1.1 folder" << reset << endl;
    
    // add the new Versace folder to the path permanently so that it can be run from anywhere
    cout << boldRed;
    system("echo 'export PATH=$PATH:~/.Versace' >> ~/.bashrc");
    cout << boldGreen << "Added Versace to the path" << reset << endl;
    
    // exit
    cout << boldGreen << "Please restart your terminal to use Versace" << reset << endl;
}

int main() 
{
    string boldGreen("\033[1;32m");
    string boldRed("\033[1;31m");
    string reset("\033[0m");
    string WindowsInstallLink("https://github.com/Ze7111/Versace/releases/download/4.1.1/Windows-Versace-4.1.1.zip");
    string LinuxInstallLink("https://github.com/Ze7111/Versace/releases/download/4.1.1/Linux-Versace-4.1.1.zip");
    // print "This is the installer for Versace" in bold green
    cout << boldGreen << "This is the installer for Versace" << reset << endl;
    // print "Funfact this installer is written in C++" in bold green
    cout << boldGreen << "Funfact this installer is written in C++" << reset << endl;
    // find out which OS the user is using
    // if the user is using Windows
    cout << boldGreen;
    if (system("ver") == 0) 
    {
        cout << reset;
        // call the WindowsInstall Function
        WindowsInstall(WindowsInstallLink);
    }
    else if (system("uname") == 0) 
    {
        cout << reset;
        LinuxInstall(LinuxInstallLink);
    }
    else 
    {
        cout << reset;
        // print "Your OS is not supported" in bold red
        cout << boldRed << "Your OS is not supported" << reset << endl;
        // print "Please download the installer for your OS from the releases page" in bold red
        cout << boldRed << "Please download the installer for your OS from the releases page" << reset << endl;
        // print "Press enter to exit" in bold red
        cout << boldRed << "Press enter to exit" << reset << endl;
        // wait for the user to press enter
        cin.get();
        // exit the program
        exit(0);
    }
};
