#from script import hra_stress_score

import sys
sys.path.append('/opt/dreamfactory/storage/scripting/python/hra/')

import common;
#from hra2016_classes import * ;

b = NeoBunch()
b.hello = 'world';

x = '';
#if isEmpty(x):
#    print('x is Empty');
#print(__name__);
print('pre-z');

#z =  hra2016_classes.HRAData2016([{"demo_gender": 1, "demo_age": 22, "Demo_pregnant":""}]);
#z = test();
#z = HRAData2016([{"demo_gender": 1, "demo_age": 22, "Demo_pregnant":""}]);
print('post-z:');

#z = hra2016_classes.test();    


#from ... storage import hra_stress_score
#from .. storage import hra_stress_score
#from . storage import hra_stress_score
# located in opt/dreamfactory/public/

verb = event.request.method;
if verb != 'GET':
    raise Exception('Only HTTP GET is allowed on this endpoint.');
 
# get resource, /math —> "", /math/add —> "add"
resource = event.resource;
 
# get query params from request
params = event.request.parameters;


 
s = hra_stress_score.stress_score(1,1,1,1,1,1); 

filter = 'fields=person_id&filter=(orguserid = ''HBI999998'') AND (organization_id = 349)';

url = 'pgsql-hra15dev/_table/user_person';
print(url);
result = platform.api.get(url);
print('post get...');
data = bunchify(json.loads(result.read()));
print(result);
print('post get data...');

# !!! this fails ? how to get data
rec = data.resource[0];
#rec = result['content']['resource'][0];
#id = rec.person_id;
print('post get 2...');

###i = result['status_code'];
#print(str(i));

#print('post get data...');
#rec = data.resource;
#print('data :'+data);
###recs = result['content']['resource'];
#recs = result['content'].resource;
###rec = result.content.resource[0];

#return acct_id;


#payload = event['request']['payload'];
#records = payload['resource'];  #all records in the post
#record = records[0];  # first record


#print('stress score: '+str(s));


