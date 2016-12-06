import sys
import json
import bunch
import importlib

# !! set path to your local folder with the scripts
sys.path.append('C:\Development\Python\HRA')
from hra2016_classes import *

# to use bunch with dictionary data -->
#rec = bunch.Bunch({"data":1})

#use json data file (place data in sys.path you entered above) ->
with open('HRACaseData.json') as json_data:
    data = json.load(json_data)
    #print(d)
    
rec = bunch.Bunch(data)

# use the following if you want to manually enter just a few data elements--> 
#rec = bunch.Bunch({ "demo_gender": 1,"demo_pregnant": -8,"demo_age": 46})

# create test variable
rec.test = 0

# pass the questionnaire data to the HRAData2016 class 
hra = HRAData2016(rec)

print("done!  demo_age: ",rec.demo_age)

# if need to reload library...
# importlib.reload(hra2016_calcengine)

