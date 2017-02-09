from logic_ai import AI

print ("loading brain structure..")
filename = 'brain_ai.txt'
file = open(filename,'r')
dataPickle = file.read()
file.close()

self.__dict__ = cPickle.loads(dataPickle)
brain = AI()

print ("start learning")
for x in range(0,100):


file = open(filename,'w')
file.write(cPickle.dumps(self.__dict__))
file.close()