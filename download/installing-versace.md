# Installing Versace

## Installing Versace

### Step 1: Download Versace

Download the latest version of Versace from [here](https://github.com/Ze7111/Versace/releases/latest). Make sure to download the one that says `installer.py` and not `source code`.

{% hint style="info" %}
If you do not want to download the installer, there is a more manual way to install Versace. You can find it here.
{% endhint %}

### Step 2: Run the installer

Run the installer by double clicking on it. If you get a warning, click `Run anyway`. If you get a warning about Windows Defender SmartScreen, click `More info` and then `Run anyway`.

If you get a warning about Python, click `Install Now`.

An alternative way to run the installer is to open a command prompt in the folder where the installer is located and run `python3 installer.py` or `python installer.py` depending on weather you installed python from the Microsoft Store or not.

{% hint style="warning" %}
The Versace installer does require Python 3.6 or higher to be installed along with admin privileges ([why?](installing-versace.md#why-do-i-need-admin-privileges)). If you do not have Python installed, you can download it [here](https://www.python.org/downloads/).
{% endhint %}

### Step 3: Test Versace

To test if Versace is installed correctly, open a command prompt and run `versace --version`. If you get a version number, Versace is installed correctly.

If you see something like this, you have installed Versace correctly:

<figure><img src="../.gitbook/assets/image (5).png" alt=""><figcaption><p>x.x.x represents a version number.</p></figcaption></figure>

### Why do I need admin privileges?

The Versace installer needs admin privileges to install the Versace command line tool. This is because the installer needs to add the Versace command line tool to the PATH environment variable. This is needed so that you can run the Versace command line tool from anywhere on your computer.

### Why does the installer require Python?

The Versace installer is written in Python. This is because it is a lot easier to write an installer in Python than in a compiled language like C++. Which will require you to compile the installer for every platform you want to support. This is why the Versace installer is written in Python.
