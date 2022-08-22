
def keys_and_vals_to_dict(keys, vals):
    return dict(zip(keys, vals))

def two_dicts_into_one(dict1, dict2):
    return dict(zip(list(dict1.keys()) + list(dict2.keys()), list(dict1.values()) + list(dict2.values())))

def print_val_of_key_history(sampleDict):
    print(sampleDict['class']['student']['marks']['history'])

def init_keys_with_same_value(keys, vals):
    new_dict = dict.fromkeys(keys, vals)
    print(new_dict)

# we want to extract the values from the sample dict using the keys
def extract_vals_from_keys(sample_dict, keys):
    d = dict()
    for key in keys:
        d.update({key: sample_dict[key]})
    return d   

def check_value_exists_in_dict(d, val):
    if val in d.values():
        return True
    else:
        return False 


sample_dict = {'a': 100, 'b': 700, 'c': 300}
#print(check_value_exists_in_dict(sample_dict, 200))

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}



#sample_dict['location'] = sample_dict.pop('city')

#print (sample_dict)

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

for key, val in sample_dict.items():
    if val['name'] == "Brad":
        val['salary'] = 8500 

print (sample_dict)




