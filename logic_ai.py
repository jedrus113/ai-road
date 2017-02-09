from collections import OrderedDict

class SignalManager:
    signals = []

    def add(self, signal):
        self.signals.append(signal)

    def pulse(self):
        old_signals = self.signals
        self.signals = []
        for sig in old_signals:
            self.signals.extend(sig.pulse())

        if not self.signals:
            return False
        return True

class Signal:
    def __init__(self, neuron, power=1, waittime=0, history=[]):
        self.neuron = neuron #sign is here
        self.waittime = waittime #time from sinapse
        self.power = power
        self.history=history
        self.history.append(self.neuron)

    def pulse(self):
        if self.waittime:
            self.waittime -= 1
            return [self]
        elif isinstance(self.neuron, Output):
            self.neuron.power(self.power)
            return []
        else:
            signals = []
            for nextneuron, synapse in self.neuron.connected_to.items():
                enchant, delay = synapse
                power = self.power * enchant
                if nextneuron.enter_barier < power:
                    signal = Signal(nextneuron, power, delay, self.history)
                    signals.append(signal)
            return signals


class Neuron:
    sign = None
    enter_barier = 0.01
    connected_to = {} # {Neuron: (enchant,delay)}


    def add_connection(self, to, enchant=0.95, delay=5):
        self.connected_to[to] = (enchant, delay)


class Output(Neuron):
    def __init__(self, fun):
        self.fun = fun # function taking one float argument, that is power

    def power(self, pow):
        self.fun(pow)

class AI:
    sm = SignalManager()
    neurons_grid = []

    def __init__(self, *funs, size=[10,10]):
        for y in range(0, size[0]):
            neurons_line = []
            for x in range(0, size[1]):
                neurons_line.append(Neuron())
            self.neurons_grid.append(neurons_line)

        for line_nr in range(0, size[0]-1):
            for neuron in self.neurons_grid[line_nr]:
                for next_neuron in self.neurons_grid[line_nr+1]:
                    neuron.add_connection(next_neuron)

        for fun in funs:
            last_neuron = Output(fun)
            for neuron in self.neurons_grid[len(self.neurons_grid)-1]:
                neuron.add_connection(last_neuron)


    def start(self, number):
        binary = bin(number)[2:]

        for n, neuron in enumerate(self.neurons_grid[0]):
            if len(binary) > n and binary[n] == '1':
                power = 1.0
            else:
                power = 0.5
            signal = Signal(neuron, power)
            self.sm.add(signal)