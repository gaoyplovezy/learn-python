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
    pickle.dump(info, f)  # f.write(pickle.dumps(info))
