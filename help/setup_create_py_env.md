

# Using miniconda 
https://docs.conda.io/en/latest/miniconda.html


I will wget the script for Miniconda3 Linux 64-bit (not other type) for the python version i need, mostly python 3.8.     
Then install.    
```
wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.10.3-Linux-x86_64.sh
bash Miniconda3-py38_4.10.3-Linux-x86_64.sh
```

it will prompt you where you want to install
in our usual deployment, we normally install in /opt/miniconda3
after install, it will prompt if you want to init conda
i normally answer no 

miniconda uses different method, but same step
```
source /opt/miniconda3/etc/profile.d/conda.sh

# To create venv, 
conda create -n myenvironmentname python=3.8 pip
   -n : name of the environment
        eg. i used publicapitest as the environment name
```


To enter the environment,
```
$ conda activate publicapitest
(publicapitest) [corona@fedora ~]$ 
```

From here, we will `pip install requirements.txt` 
REFERENCE on how to create the requirements.txt: https://note.nkmk.me/en/python-pip-install-requirements/

But its roughly something like this:
```
After your development and testing, you may want to export the current pips you have installed
pip freeze > requirements.txt 

So other user can download the requirements.txt and install into their venv
pip install -r requirements.txt

NOTE: We will want to specify the specific versions 
```
