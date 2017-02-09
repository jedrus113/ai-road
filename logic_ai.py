class SignalManager:
    signals = set()

    @staticmethod
    def add(signal):
        SignalManager.signals.add(signal)

    @staticmethod
    def pulse():
        old_signals = SignalManager.signals
        SignalManager.signals = set()
        for sig in old_signals:
            sig.pulse()

        if not SignalManager.signals:
            return False
        return True

class Neuron:
    def __init__(self):
        self.sign = None
        self.enter_barier = 0.01
        self.connected_to = {}  # {Neuron: enchant}
        self.power = 0.0

    def sum_power(self, power):
        if self.power < 1.0:
            if self.power + power > 1.0:
                self.power = 1.0
            else:
                self.power += power

    def add_connection(self, to, enchant=0.90):
        self.connected_to[to] = enchant

    def pulse(self):
        for nextneuron, enchant in self.connected_to.items():
            power = self.power * enchant
            if nextneuron.enter_barier < power:
                nextneuron.sum_power(power)
                SignalManager.add(nextneuron)
        self.power = 0.0


class Output(Neuron):
    def __init__(self, fun):
        super(Output, self).__init__()
        self.fun = fun # function taking arguments: Float Power, and Array SignalHistory

    def pulse(self):
        self.fun(self.power)

class AI:
    sm = SignalManager()
    neurons_grid = []

    def __init__(self, size=[10,10]):
        for y in range(0, size[0]):
            neurons_line = []
            for x in range(0, size[1]):
                neuron = Neuron()
                neurons_line.append(neuron)
                if y:
                    for old_neuron in self.neurons_grid[len(self.neurons_grid)-1]:
                        old_neuron.add_connection(neuron)
            self.neurons_grid.append(neurons_line)

    def setup(self, *funs):
        for fun in funs:
            last_neuron = Output(fun)
            for neuron in self.neurons_grid[len(self.neurons_grid)-1]:
                neuron.add_connection(last_neuron)

    def start(self, number):
        binary = bin(number)[2:] #binary number from int

        for n, neuron in enumerate(self.neurons_grid[0]):
            if len(binary) > n and binary[n] == '1':
                power = 1.0
            else:
                power = 0.5
            neuron.sum_power(power)
            self.sm.add(neuron)

    def step(self):
        return self.sm.pulse()