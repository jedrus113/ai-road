import cPickle

filename = 'brain_ai.txt'

def load(Class_to_load):
    file = open(filename, 'r')
    dataPickle = file.read()
    file.close()
    instance = Class_to_load()
    instance.__dict__ = cPickle.loads(dataPickle)
    return instance

def save(instance):
    file = open(filename, 'w')
    file.write(cPickle.dumps(instance.__dict__))
    file.close()