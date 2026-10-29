import subprocess
import pickle
from subprocess import Popen
from pickle import loads
import os
from urllib.parse import urljoin
import urllib
from yaml import load
import yaml
import pathlib
from pathlib import Path

if __name__ == '__main__':
    p = subprocess.Popen("Calculator")#, shell=True)
    pp = Popen("Calc", shell=True, stdout="lol")
    
    pickle.loads("idk")
    loads("idk")
    
    os.path.join("/lol", "/error")
    
    urllib.parse.urljoin("https://lol.com", "https://lolevil.com")
    urljoin("https://lol.com", "https://lolevil.com")
    
    yaml.load("Who cares")
    load("who cares")
    
    pathlib.Path.joinpath("/root")
    Path.joinpath("/root")

