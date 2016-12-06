def between(var,min,max):
    if min <= var <= max :
        return(True);
    else:
        return(False);
        
def between1(var,min,max):
    if isEmpty(var):
        return(True);
    else:
        if min <= var <= max :
            return(True);
        elif var < 0:
            return(True);
        else:
            return(False);
  
def setKeysToLower(dict):
    for key in dict:
        keylower = key.lower();
        if keylower != key:
            dict[keylower] = dict.pop(key);
    return(dict);

def isEmpty(item):
    if type(item) == str:
        item = str.strip(item);
        if not(item):
            return(True);
        else:
            return(False);
    else:
        return(False);

def nvl(item, value):
    result = value;
    if type(item) == str:
        if isEmpty(item):
            result = value
        else:
            result = item
    else:
        if item < 0 :
            result = value
        else:
            result = item
    return(result);

            
def trunc(number, decimals):
    fmt = '%.'+str(decimals)+'f'
    return float(fmt%(number))            
            
    
def postparms(dict):
    # specify fieldname: value in dict
    # Dictionary must be OrderDict e.g.,  dict = collections.OrderedDict();

    params = '{"params": [ ';
    i = 0;
    for key in dict.keys():
    #for key in dict:
        i = i + 1;
        if i > 1:
            params += ',';
            
        if type(dict[key]) == str:
            params += ' {"name": "';
            params += key+'"';
            params += ',"value":"';
            params += dict[key]
            params += '"}';
            
        else:
            params += ' {"name": "';
            params += key+'"';
            params += ',"value":'
            params += str(dict[key]);
            params += '}';

    params += ']}';
    return(params);
