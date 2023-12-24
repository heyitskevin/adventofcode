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

import copy

    
def eval_subtree(mods, sub_root):
    new_mod = {}
    # build subtree
    root = copy.deepcopy(sub_root)
    q = [root]
    while q:
        root = q.pop(0)
        if root in new_mod or root == 'rx':
            continue
        new_mod[root] = copy.deepcopy(mods[root])
        
        for c in new_mod[root].output_modules:
            q.append(c)

    def check_all_off(subtree):
        nodes = []
        for k, v in subtree.items():
            nodes.append(v)
        for n in nodes:
            if isinstance(n, FlipFlop) and n.state == 'on':
                return False
        return True
    # Loop and eval
    button_presses = 0
    root = new_mod.pop(sub_root)
    while True:
        if button_presses > 1 and check_all_off(new_mod):
            print('buttons', button_presses, sub_root)
            return button_presses
        q = [(root, 'low', Broadcaster('broadcaster', [root]))]
        button_presses += 1
        while q:
            node, signal, parent = q.pop(0)
            children = [new_mod.get(n, None) for n in node.output_modules]
            new_signal = node.process_pulse(parent.name, signal)
            for c in children:
                if new_signal and c:
                    q.append((c, new_signal, node))
    


# SOLUTION WAS IDENTIFIED BY FINDING THE SIZE OF THE LOOP AND INTROSPECTION OF THE GRAPH
# WE THEN REALIZE THAT THE FLIP FLOPS ARE BASICALLY BINARY 
# WE ALSO REALIZE THAT THE BROADCASTER BROADCASTS TO 4 INDEPENDENT GROUPS
# EACH GROUP THEN HAS FLIPFLOPS THAT BACK PROPOGATE TO THE NODE THAT INVERTS TO RX
# USING 1 AS A FLIP FLOP THAT'S ON AND A 0 FOR OFF WE GET A BINARY NUMBER B
# REALIZE THAT B IS THE NUMBER OF BUTTON PRESSES
# REALIZE THAT B+1 RESETS EVERYTHING
# GET LCM OF ALL B
# BAD HANDWRITING LEADS TO 2 HOURS OF GRIEF
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
    # PRESS UNTIL RX IS GIVEN A LOW SIGNAL
    # BRUTE FORCE NOT VIABLE
    button_presses = 0
    for _ in range(button_presses):
        q = [(bc, 'low', PulseModule('button', ['broadcaster']))] # (Current node, incoming signal, ancestor node)
        while q:
            node, signal, parent = q.pop(0)
            children = [mods.get(n, None) for n in node.output_modules]
            new_signal = node.process_pulse(parent.name, signal)
            for c in children:
                if new_signal and c:
                    q.append((c, new_signal, node))
    # Subtree eval
    for f in bc.output_modules:
        eval_subtree(mods, f)

    
        
print(func())

# 225514321828633 SOLN
