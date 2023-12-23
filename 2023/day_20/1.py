FILENAME = 'input.txt'

from collections import defaultdict

class PulseModule:
    def __init__(self, name, output_modules):
        self.name = name
        self.output_modules = output_modules
        self.state = None
    
    def report_state(self):
        return self.state
    
    def process_pulse(self, parent_node_name, incoming_pulse): # Do something w/ self.current_pulse
        return []

    def emit_low_pulse(self):
        return 'low'

    def emit_high_pulse(self):
        return 'high'


class FlipFlop(PulseModule):
    def __init__(self, name, output_modules):
        super().__init__(name, output_modules)
        self.state = 'off'

    def process_pulse(self, parent_node_name, incoming_pulse):
        if incoming_pulse == 'low': # flip flop
            if self.state == 'off':
                self.state = 'on'
                return self.emit_high_pulse()
            elif self.state == 'on':
                self.state = 'off'
                return self.emit_low_pulse()
        else: # No Pulse
            return []
        raise Exception('something fucky happened')

class Conjunction(PulseModule):
    def __init__(self, name, output_modules):
        super().__init__(name, output_modules)
        self.memory = {}
    
    def process_pulse(self, parent_node_name, incoming_pulse):
        self.memory[parent_node_name] = incoming_pulse
        
        all_high = all(
            v == 'high' for k, v in self.memory.items()
        )
        if all_high:
            return self.emit_low_pulse()
        else:
            return self.emit_high_pulse()
        raise Exception('something fucky happened')
    
    def initialize_update_memory(self, parent_node_name):
        # Only run to initialize
        self.memory[parent_node_name] = 'low'

class Broadcaster(PulseModule):
    def __init__(self, name, output_modules):
        super().__init__(name, output_modules)
    
    def process_pulse(self, parent_node_name, incoming_pulse):
        return self.emit_low_pulse()

def build_module_from_data(name, output_modules):
    if '%' in name:
        return FlipFlop(name, output_modules)
    elif '&' in name:
        return Conjunction(name, output_modules)
    elif name == 'broadcaster':
        return Broadcaster(name, output_modules)
    else:
        return PulseModule(name, output_modules)
    
def map_modules(mod_dict):
    broadcaster = mod_dict.pop('broadcaster')
    assert isinstance(broadcaster, Broadcaster)


    for om in broadcaster.output_modules:
        print(om)

def read_file():
    with open(FILENAME) as f:
        lines = [ln for ln in f.read().split('\n')]
        r = []
        for l in lines:
            a, b = l.strip().split('->')
            r.append((a.strip(), b.strip().split(', ')))
        return r


def func():
    d = read_file()
    mods = {}
    for m in d:
        a_mod = build_module_from_data(*m)
        if m[0][0] in ['%', '&']:
            mods[m[0][1:]] = a_mod # The module object that corresponds to the given name
        else:
            mods[m[0]] = a_mod

    for k, v in mods.items():
        children = v.output_modules
        for c in children:
            if c in mods.keys() and isinstance(mods[c], Conjunction):
                mods[c].initialize_update_memory(v.name)
    
    bc = mods.pop('broadcaster')
    assert isinstance(bc, Broadcaster)
    # QUEUE BASED SOLUTION
    lo = 0 
    hi = 0
    button_presses = 1000
    for press in range(button_presses):
        q = [(bc, 'low', PulseModule('button', ['broadcaster']))] # (Current node, incoming signal, ancestor node)
        while q:
            node, signal, parent = q.pop(0)
            children = [mods.get(n, None) for n in node.output_modules]
            new_signal = node.process_pulse(parent.name, signal)

            for c in children:
                if new_signal and c:
                    q.append((c, new_signal, node))
                if new_signal == 'low':
                    lo += 1
                elif new_signal == 'high':
                    hi += 1
    lo += button_presses
    print(lo, hi, lo*hi)
        
func()

# 825167435 soln