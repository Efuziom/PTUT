#json editor module to use an external storage of ESP IPs
#! function started by '_' is private

import json
import os.path
from urllib.request import urlopen

#--------------------------------------------------------
#>publics functions used as interface

#build a exemple json file about ESP IPs
#arg: a name of json file (like "test.json")
def buildEspFileExemple(jFile):
    espInfos= {'ESP':[{'id':1, 'ip':"192.168.1.22"},{'id':2, 'ip':"192.168.1.25"}]}
    _writeFile(jFile, espInfos)

#build an empty json file for ESP IPs
#arg: a name of json file (like "test.json")
def buildEspFileTemplate(jFile):
    espInfos= {'ESP':[]}
    _writeFile(jFile, espInfos)

#load an array, containing all ESP specifications (list of dictionarys (format "'id':int,'ip':str"))
#arg: a name of json file (like "test.json")
def loadEspSpecList(jFile):
    if (os.path.exists(jFile)):
        with open(jFile) as f:
            data= json.load(f)
        return data.get('ESP')
    return None

#load an array, containing all ESP IDs
#arg: a name of json file (like "test.json")
def loadEspIDList(jFile):
    if (os.path.exists(jFile)):
        with open(jFile) as f:
            data= json.load(f)
        IDs= []
        for elem in data.get('ESP'):
            IDs.append(elem.get('id'))
        return IDs
    return None

#load an array, containing all ESP IPs
#arg: a name of json file (like "test.json")
def loadEspIPList(jFile):
    if (os.path.exists(jFile)):
        with open(jFile) as f:
            data= json.load(f)
        IPs= []
        for elem in data.get('ESP'):
            IPs.append(elem.get('ip'))
        return IPs
    return None

#load the specified IP using a ESP ID
#arg: a name of json file (like "test.json") and an ID
def loadEspIPFromID(jFile, Id):
    if (os.path.exists(jFile)):
        with open(jFile) as f:
            data= json.load(f)
        for elem in data.get('ESP'):
            if(elem.get('id')==Id):
                return elem.get('ip')
    return None

#add a new ESP entry in a json file
#args: an name of json file and ESP specifications (id and ip (str))
def addEspToFile(jFile, Id, ip):
    if (os.path.exists(jFile)):
        with open(jFile) as f:
            data= json.load(f)
        specList= data.get('ESP')
        specList.append({'id':Id, 'ip':ip})
        data['ESP']= specList
        _writeFile(jFile, data)
    else:
        buildEspFileTemplate(jFile)
        addEspToFile(jFile, Id, ip)

#remove ESPs with the specified ID from the json file
#args: an name of json file and ESP ID
def rmEspToFile(jFile, Id):
    if (os.path.exists(jFile)):
        with open(jFile) as f:
            data= json.load(f)
        ESPs= data.get('ESP')
        for elem in ESPs:
            if(elem.get('id')==Id):
                ESPs.remove(elem)
        data['ESP']= ESPs
        _writeFile(jFile, data)

#--------------------------------------------------------
#>privates functions:

#write (replace) in an existing or new json file
#args: a name of json file and the saved dictionary
def _writeFile(jFile, infos):
    with open(jFile, 'w') as f:
        json.dump(infos, f, indent= 2)

#--------------------------------------------------------
#>main function used if jsonFileEditor is directly called

#create an exemple file when the .py is used as main
#arg: a name of json file (like "test.json")
if __name__== "__main__":
    import sys
    try:
        buildEspFileTemplate(str(sys.argv[1]))
    except:
        print("An argument (name file) is required")

#-------------------------------------------------------

##open online json:
#with urlopen("https://"+"192.168.1.22"+"/json") as response:
#    data= json.load(response.read())
#
##write json:
#with open("test.json", 'w') as f:
#    json.dump(espInfos, f, indent= 2)
#
##open json:
#with open("test.json") as f:
#    data= json.load(f) #data have keys who coresponds at values (values= data['objName'])
#
##count elements (in the group of esp):
#print(len(data['ESP'])) #if we have B in A; "len(data['A']['B'])"
