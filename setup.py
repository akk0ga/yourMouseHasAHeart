from distutils.core import setup
import pyautogui
from pygame import mixer
import abc
from win32api import GetSystemMetrics
import time
from random import randint
import os.path
from mouse.Mouse import Mouse
import voice
import py2exe


setup(console=['main.py'])