# Author:zyx
# import json
import pickle


def sayhi(name):
    print("hello", name)


with open('test', 'rb') as f:
    # data = json.loads(f.read())
    data = pickle.loads(f.read())
print(data['func']('zyx'))
