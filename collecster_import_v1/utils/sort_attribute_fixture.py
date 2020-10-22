#!/usr/bin/env python

import json, functools

f = open("advideogame/fixtures/initial_attributes.json")
data = json.load(f)
data_attr = data[3:]
data_cat = data[:3]

def cmp(a, b):
    return (a > b) - (a < b) 

def pred(l, r):
    cat = cmp(l["fields"]["category"], r["fields"]["category"])
    if cat != 0:
        return cat
    else:
        return cmp(l["fields"]["name"], r["fields"]["name"])

sorted_attr = sorted(data_attr, key=functools.cmp_to_key(pred))

i = 0
def reassign_pk(attr):
    global i
    i+=1
    attr["pk"]=i
    return attr



new_data = data_cat + list(map(reassign_pk, sorted_attr))
o = open("initial_attributes_sorted.json", "w")
o.write(json.dumps(new_data, indent=4))
    
