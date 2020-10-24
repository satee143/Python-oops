d = {
        'owner': {
            'name': {'first_name': 'Steven', 'last_name': 'Smith'},
            'lottery_nums': [1, 2, 3, 'four', '11', None],
            'address': {},
            'tuple': (1, 2, 'three'),
            'tuple_with_dict': (1, 2, 'three', {'is_valid': False}),
            'set': {1, 2, 3, 4, 'five'},
            'children': [
                {'name': {'first_name': 'Jessica',
                          'last_name': 'Smith', },
                 'children': []
                 },
                {'name': {'first_name': 'George',
                          'last_name': 'Smith'},
                 'children': []
                 }
            ]
        }
    }
from benedict import benedict 
#d={'a':1,'k':{3:{'c':4}}}
d = benedict(d)
f = d.flatten(separator='_')
print(f)