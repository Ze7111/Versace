# Installation

## Prerequisites 🖥️

* <mark style="color:blue;">**Windows 10 (x64)**</mark> or above
* <mark style="color:green;">**Code editor**</mark>, I recommend [**Visual Studio Code**](https://code.visualstudio.com/download), along with the [**Versace Extension**](https://marketplace.visualstudio.com/items?itemName=ZE7111.Versace). &#x20;
* <mark style="color:yellow;">Python 3.6.0</mark> **** or above **** (optional) if you do not have it you can download it [**here!**](https://www.python.org/downloads/release/python-3110/)****

## Installation ✅

#### **Powershell:**&#x20;

Paste & run the following command in Powershell (`win + r` -> `powershell.exe`)

```powershell
New-Item "$HOME\versace" -ItemType "directory" -Force
Invoke-WebRequest "https://github.com/Ze7111/Versace/releases/latest/download/Windows-Versace-4.0.0rw.zip" -OutFile "$HOME\versace\versace.zip"
Expand-Archive "$HOME\versace\versace.zip" -cestinationPath "$HOME\versace" -Force
Remove-Item "$HOME\versace\versace.zip" -Force
[Environment]::SetEnvironmentVariable("Path", [Environment]::GetEnvironmentVariable("Path", "User") + ";$HOME\versace\Windows-Versace-4.0.0rw", "User")
```

### Installation without Powershell (Mac and Linux)

{% hint style="danger" %}
This method is **not** entirely reliable, due to the you having to do all the steps manually.
{% endhint %}

{% hint style="warning" %}
For installing for **Mac** or **Linux** click [**here.**](https://github.com/Ze7111/Versace/releases/latest)****
{% endhint %}

1. Download the `(yourOS)-Versace-(version).zip` from the respective post.
2. Unzip the file in an appropriate directory - This will be the location where Versace will live.
3. Add the file called `versace.pkg` to **PATH**, if you do **not** know how to add files to **PATH**, follow this [**link (Linux)** ](https://linuxize.com/post/how-to-add-directory-to-path-in-linux/)and this[ **link (Mac)**](https://osxdaily.com/2014/08/14/add-new-path-to-path-command-line/).
4. Once you have done to above steps, restart you shell (log out and back in)
5. Open a new terminal/shell window, and run this command `versace -v` if you see an output, success
6. If you do **not,** please contact me [**here**](../ISSUES.md).

{% hint style="success" %}
#### I do not trust this, where can I find the source code?

I completely understand if you do not trust, this, hence the code for Versace is open source, and is available below this post.
{% endhint %}

{% embed url="https://github.com/Ze7111/Versace/tree/re-written" %}

### Once you are done installing Versace head over [HERE](../basics/basic-rules-to-know-in-versace.md).
