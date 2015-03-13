import  pickle

class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'

summer = Bird()
apple = [112, 'abs']
fn = 'e:\dat.txt'
'''
pickle load,dump, with as
 '''
with open(fn, 'wb') as f:
    pickle.dump(apple, f)
#    pickle.dump(apple, f)

with open(fn, 'rb') as f:
    summer = pickle.load(f)
    print(summer)
