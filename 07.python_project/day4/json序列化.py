# Author:zyx
#import json
import pickle


def sayhi(name):
    print("hello", name)


info = {
    'name': 'zyx',
    'age': 22,
    'func': sayhi
}
with open('test', 'wb') as f:
    #f.write(json.dumps(info))
    f.write(pickle.dumps(info))
