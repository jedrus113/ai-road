import class_loader
from logic_ai import AI

print ("loading brain structure..")

location = 0
def step(how_much, sygnal_history):
    location += how_much

brain = class_loader.load(AI)

print ("start learning")
for x in range(0,100):


class_loader.save(brain)