import os
from flask import Flask, jsonify, json, request

app = Flask(__name__)



def add_data(new_data):
    with open('storage.data') as openfile:
        data = json.load(openfile)
        data['person'].append(new_data)
        with open('storage.data','w') as outfile:
            json.dump(data, outfile,ensure_ascii=False,indent=2)

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

@app.route('/todo/api/v1/storage/json/all', methods=['GET'])
def get_all():
    with open("storage.data") as jsonFile:
        all = json.load(jsonFile)
    return jsonify({'result': all})

@app.route('/todo/api/v1/storage/json/readkey=<task_id>', methods=['GET'])
def get_val(task_id):
    with open("storage.data") as jsonFile:
        all = json.load(jsonFile)
    d = find_val(all,task_id)
    return jsonify({'result':str(d)[1:-1].replace("'","")})

@app.route('/todo/api/v1/storage/json/write', methods=['POST'])
def add_val():
    add_data(request.json)
    p = request.json
    return p

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))