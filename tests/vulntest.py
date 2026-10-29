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
    p = subprocess.Popen("Calculator")
    pp = Popen("Calculator", shell=True)
    
    pickle.loads("Somefile")
    loads("Somefile")
    
    os.path.join("Desktop", "/root")
    
    urllib.parse.urljoin("https://good.com", "https://evil.com")
    urljoin("https://good.com", "https://evil.com")
    
    yaml.load("Somefile")
    load("Somefile")
    
    pathlib.Path.joinpath("Desktop", "/root")
    Path.joinpath("Desktop", "/root")

