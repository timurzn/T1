import json
import argparse

# add values in file
def add_data(key,val):
    new_data = {key: val}
    with open('storage.data') as openfile:
        data = json.load(openfile)
        data['person'].append(new_data)
        with open('storage.data','w') as outfile:
            json.dump(data, outfile,ensure_ascii=False,indent=2)

#Find value in file
def find_val(myjson, key):
    results = []
    def _find_val(myjson, key):
        if type(myjson) is dict:
            for jsonkey in myjson:
                if type(myjson[jsonkey]) in (list, dict):
                    _find_val(myjson[jsonkey], key)
                elif jsonkey == key:
                    results.append(myjson[jsonkey])        
        elif type(myjson) is list:
            for item in myjson:
                if type(item) in (list, dict):
                    _find_val(item, key)
    _find_val(myjson, key)
    return results  
    

parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()

if args.key is not None and args.val is not None:
    add_data(args.key,args.val)
elif args.val is None and args.key is not None:
    with open("storage.data") as jsonFile:
        my_dictionary = json.load(jsonFile)
    if not find_val(my_dictionary,args.key) :
        print("None")
    else:
        print(*(find_val(my_dictionary,args.key)), sep = ",")
else:
    print('Incorrect data')

