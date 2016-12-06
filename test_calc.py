import sys
import json
import bunch
import importlib

# !! set path to your local folder with the scripts
sys.path.append('C:\Development\Python\HRA')
from hra2016_calcengine import *

#rec = bunch.Bunch()
rec = bunch.Bunch({ "demo_gender": 1,"demo_pregnant": -8,"demo_age": 46})
rec.test = 0
hra = HRACalcData(rec)
print("Demo_gender: ",rec.demo_gender)

# if need to reload library...
# importlib.reload(hra2016_calcengine)

