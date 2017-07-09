import json

def put(data, filename):
    try:
        jsondata = json.dumps(data, indent=4, skipkeys=True, sort_keys=True)
        fd = open(filename, 'w')
        fd.write(jsondata)
        fd.close()
    except:
        print 'ERROR writing', filename
        pass

def get(filename):
    returndata = {}
    fd = open(filename, 'r')
    text = fd.read()
    fd.close()
    returndata = json.loads(text)
    return returndata

def pretty(data):
    return json.dumps(data,sort_keys=True, indent=4, separators = (',', ': '))


db_file = "/Volumes/Verbinski/02_SCRIPTING/GitHub/postyr/nuke/manifest.json"
db_obj = get(db_file)
db_str = pretty(db_obj)

#how to read keys
include_files = db_obj["include_files"]
include_folders = db_obj["include_folders"]
exclude_files = db_obj["exclude_files"]
exclude_folders = db_obj["exclude_folders"]

#how to read keys' values
print ", ".join(include_files)

#how to add to list []
db_obj["include_files"].append("something")

#how to add to dict {}
db_obj['somethingNew'] = ["one","two","three"]

db_str = pretty(db_obj)
print db_str