FILENAME = 'example.txt'

class PulseModule:
    def __init__(self, name, input_modules, output_modules):
        self.name = name
        self.input_modules = input_modules
        self.output_modules = output_modules
        self.state = None
    
    def report_state(self):
        return self.state
    
    def process_pulse(self, incoming_pulse): # Do something w/ self.current_pulse
        return 'DEAD'

    def emit_low_pulse(self):
        return 'low'

    def emit_high_pulse(self):
        return 'high'


class FlipFlop(PulseModule):
    def __init__(self, name, input_modules, output_modules):
        super().__init__(name, input_modules, output_modules)
        self.state = 'off'

    def process_pulse(self, incoming_pulse):
        if incoming_pulse == 'low': # flip flop
            if self.state == 'off':
                self.state = 'on'
                return self.emit_high_pulse()
            elif self.state == 'on':
                self.state = 'off'
                return self.emit_low_pulse()
        else: # No Pulse
            return 'DEAD'
        raise Exception('something fucky happened')

class Conjunction(PulseModule):
    def __init__(self, name, input_modules, output_modules):
        super().__init__(name, input_modules, output_modules)
        self.memory = {k.name: 'low' for k in input_modules} # Access of name subject to revision
    
    def process_pulse(self, incoming_node_name, incoming_pulse):
        self.memory[incoming_node_name] = incoming_pulse
        all_high = all(
            v == 'high' for k, v in self.memory.items()
        )
        if all_high:
            return self.emit_low_pulse()
        else:
            return self.emit_high_pulse()
        raise Exception('something fucky happened')

def build_module_from_data(prefix, name, input_modules, output_modules):
    if prefix == '%':
        return FlipFlop(name, input_modules, output_modules)
    elif prefix == '&':
        return Conjunction(name, input_modules, output_modules)
    else:
        return PulseModule(name, input_modules, output_modules)

def read_file():
    with open(FILENAME) as f:
        lines = [ln for ln in f.read().split('\n')]
        r = []
        for l in lines:
            a, b = l.strip().split('->')
            r.append((a.strip(), b.strip().split(',')))
        return r

    
def func():
    d = read_file()
    print(d)

func()