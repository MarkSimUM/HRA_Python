import sys
import json
#import bunch
#from infi.bunch import *
import infi.bunch 
import collections
from collections import OrderedDict



# !! set path to your local folder with the scripts
sys.path.append('C:\Development\Python\HRA')
from hra2016_classes import *

# to use bunch with dictionary data --> rec = Bunch({"data":1})
# to copy existing dictionary, use bunc.bunchify(dict)

#  To create ordered dict => dict = collections.OrderedDict()
# NOTE: I do not think you can OrderDictionary will be ordered by bunch

# main dictionary functions => dict.items(), dict.keys(), and dict.values() 



# use the following if you want to manually enter just a few data elements--> 
#rec = Bunch({ "demo_gender": 1,"demo_pregnant": -8,"demo_age": 46})

#use json data file (place data in sys.path you entered above) ->
with open('HRACaseData.json') as json_data:
    # use object_pairs_hook=OrderedDict to keep variables in same order
    data = json.load(json_data, object_pairs_hook=OrderedDict); 
    #data = json.load(json_data)
 
# TESTING of ordered dictionary
#print('OrderedDict')
#for k, v in data.items():
#    print( k, v)

# note: bunchifying data loses order
rec = infi.bunch.bunchify(data);
    
# TESTING iterate and print bunchified dictionary
#print('Bunchified dict')
#for k, v in rec.items():
#    print( '{}: {}'.format(k, v))

# create test variable
rec.test = 0

# example code to show how to add list to another list
##varlist = ['demo_gender'
##           , 'demo_age'
##           , 'mdctx_chrkidneydz_care']
##varl2 = ['demo_pregnant']
##varlist.extend(varl2);
##print(varlist);

# Example to copy selected elements (from varlist) of dictionary record to new variable
#newdict = {key:rec[key] for key in varlist}
# bunchify the dictionary (will not work with older version of bunch)
#newdict = infi.bunch.bunchify(newdict);
# print('newdict:', newdict);


# SurveyKeyVars checks that all necessary variables are included
#  critical_error set to non-zero if problem
# uncomment next two lines to use SurveyKeyVars -->

#checkhra = SurveyKeyVars(rec)
#print('SurveykeyVars critical error',checkhra.critical_error);

# create new HRAData2016 object
# pass the questionnaire data to the hra2016_classes.HRAData2016 class
hra = HRAData2016(rec)

print("done!  demo_age: ",rec.demo_age)

# !! DOCUMENTATION 
# Class information  --->
#  ALL use:
#   import sys
#   import json
#  from common import *
#  from bunch import *


#   !! hra2016_classes
#    imports -->
#      import hra2016_calcengine ;
#      import hra2016_messages ;
#  class SurveyKeyVars: (record)
#  class HRAData_Base: (record, varlist, biolist)
#  class HRAData2016(HRAData_Base): (record)


#   !! hra2016_calcengine
#   imports --->
#    import hra2016_func ;
#    import hra2016_util ;

#   class HRACalcData : (record)

#   !! hra2016_messages
#   class ReportMessageVarsBase: (record)
#      self.record = record
#      self.message = messages [new dictionary of messages]

#   class ReportMessageVars2016(ReportMessageVarsBase):   


