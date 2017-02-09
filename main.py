import class_loader
from logic_ai import AI

print ("loading brain structure..")

brain = class_loader.load(AI)

print ("start learning")
for x in range(0,100):
    pass

class_loader.save(brain)