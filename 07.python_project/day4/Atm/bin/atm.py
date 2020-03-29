__author__ = "zyx"
import os,sys

temp = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(temp)
sys.path.append(temp+'\core')

from core import main