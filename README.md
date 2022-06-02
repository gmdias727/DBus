## Custom Services on UNIX operating systems
### Creating custom UNIX services using Dasbus

<br/>

![version](https://img.shields.io/badge/Python-3.10.4-blue)
![dependencies](https://img.shields.io/badge/dependencies-LTS-blue)

### Requirements for running this application:
- Python ^3.6
- Dasbus ^1.6
- PyGObject ^3.42.1
- Poetry ^1.1.13
- Beautifulsoup4 ^4.11.1
- Requests ^2.27.1
- Halo ^0.0.31

<br/>

You need to clone this project repository to your local machine, just type the following on your favorite terminal:

```console
$ git clone git@github.com:grandehe4rt/DBus.git
```

> **Note** *<br/> 
> Be sure to have a validated SSH public Key on your github account <br/>
> Refer to: [How to create and validate a SSH public key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)



The above command clones the project repository to your local machine inside the directory you're currently located.

Type:

```console
$ cd DBus
```

<br/>

Before start installing the dependencies, read carrefully:

<div style=" margin: auto; text-align: center;">
    <img src="Docs/UbuntuLogo.png" alt="Arch Linux" style="height: 50px; width:50px;"/>
    <p>If you are using a Debian/Ubuntu environment</p>
</div>

Type:
<br/>

```console
$ sudo apt install libgirepository1.0-dev
```
If `libgirepository1.0-dev` is not installed, might leed to a problem in the future. <br/>
If the package is already installed, our package manager will update it to a brand new version.

<br/>

<div style=" margin: auto; text-align: center;">
    <img src="Docs/ArchLinuxLogo.png" alt="Arch Linux" style="height: 50px; width:50px;"/>
    <p>if you are using an Arch Linux environment.</p>
</div>

I highly recommend reading this following guide <u>[here.](https://pygobject.readthedocs.io/en/latest/getting_started.html#arch-getting-started)</u>

<br/>

---

<br/>

<h3 style="text-align: center">Now let's install <u>✨Poetry✨</u></h3>

Poetry creates a virtual environment for you, is a tool for dependency management and packaging in Python, and also protects you from downloading unofficial and unprotected packages. 

Read more in: [Poetry Docs](https://python-poetry.org/)

In your favorite CLI type:
```console
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```
The above command install Poetry on your machine.

<br/>

Type:
```console
$ poetry install
```
This command will install every dependecy you'll need to run the project.

<br/>

Type:
```console
$ poetry shell
```
This command activates our virtual environment so we're able to run the app without.


Now we can run the app

D-Bus Authors:
- Havoc Pennington, Red Hat, Inc.
- Alexander Larsson, Red Hat, Inc.
- Anders Carlsson, CodeFactory AB.
- Sven Herzberg, Imendio AB.
- Simon McVittie, Collabora Ltd.
- David Zeuthen.

Authors of Dasbus:
* Dasbus Creator - Vendula Poncova - GitHub: [poncovka](https://github.com/poncovka)
* Dasbus Co-Creator - Woodrow Douglass - Github: [wdouglass](https://github.com/wdouglass)

M.M. McKerns, L. Strand, T. Sullivan, A. Fang, M.A.G. Aivazis,
"Building a framework for predictive science", Proceedings of
the 10th Python in Science Conference, 2011;
http://arxiv.org/pdf/1202.1056

Michael McKerns and Michael Aivazis,
"pathos: a framework for heterogeneous computing", 2010- ;
https://uqfoundation.github.io/project/pathos


