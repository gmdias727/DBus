## Custom Services on Linux OS's
### Using python and D-Bus

<br/>

![version](https://img.shields.io/)

### Requirements for running this application:
- Python ^3.6
- Dasbus ^1.6
- PyGObject ^3.42.1
- Poetry ^1.1.13

<br/>

Before start installing the dependencies, read carrefully:

<div style=" margin: auto; text-align: center;">
    <img src="Docs/UbuntuLogo.png" alt="Arch Linux" style="height: 50px; width:50px;"/>
    <p>If you are using a Debian/Ubuntu environment</p>
</div>

Type:
<br/>

```console
sudo apt install libgirepository1.0-dev
```
If `libgirepository1.0-dev` is not installed, might leed to a problem in the future. <br/>
If the package is already installed, our package manager will update it to a brand new version.

<br/>

<div style=" margin: auto; text-align: center;">
    <img src="Docs/ArchLinuxLogo.png" alt="Arch Linux" style="height: 50px; width:50px;"/>
    <p>if you are using an Arch Linux environment.</p>
</div>

I highly this following guide <u>[here.](https://pygobject.readthedocs.io/en/latest/getting_started.html#arch-getting-started)</u>

<br/>

---

<br/>

<h2 style="text-align: center">Now let's install <u>✨Poetry✨</u></h2>


<div style="">
You'll need to install Poetry it creates a virtual environment for you, is a tool for dependency management and packaging in Python, and also protects you from downloading unofficial and unprotected packages. 
</div>

Read more in: [Poetry Docs](https://python-poetry.org/)

In your favorite CLI type:
```console
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```
The above command installs Poetry on your machine



<!-- 

### Authors:
Gabriel Dias Mazieri -->
