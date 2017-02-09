import class_loader
from logic_ai import AI

print ("loading brain structure..")

brain = class_loader.load(AI)

print ("start learning")


class_loader.save(brain)