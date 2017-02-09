import class_loader
from logic_ai import AI

print ("loading brain structure..")

ai = class_loader.load(AI)
steps = 0.0

print ("start learning")
def step_fun(forward, hist):
    global steps
    steps -= forward
    if steps < 0:
        print "Dead"
        pass # punishment shall be here
    else:
        print "lucky step"
        pass # prize

ai.setup(step_fun)
ai.start(0)

while ai.step():
    pass

class_loader.save(ai)