from iteration_utilities import  deepflatten

d=(1,2,(3,[4,5],{'a':99},6,(7,((8)))))
print(list(deepflatten(d)))

from benedict import benedict 
d={'a':1,'k':{3:{'c':4}}}
d = benedict(d)
f = d.flatten(separator='_')
print(f)

def flat_items(d, key_separator='.'):
    """
    Flattens the dictionary containing other dictionaries like here: https://stackoverflow.com/questions/6027558/flatten-nested-python-dictionaries-compressing-keys

    >>> example = {'a': 1, 'c': {'a': 2, 'b': {'x': 5, 'y' : 10}}, 'd': [1, 2, 3]}
    >>> flat = dict(flat_items(example, key_separator='_'))
    >>> assert flat['c_b_y'] == 10
    """
    for k, v in d.items():
        if type(v) is dict:
            for k1, v1 in flat_items(v, key_separator=key_separator):
                yield key_separator.join((k, k1)), v1
        else:
            yield k, v
            
print(next(flat_items(d)))