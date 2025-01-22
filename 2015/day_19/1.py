import re

REPLACEMENTS = 'replacements.txt'
MEDICINE = 'medicine.txt'

def read_requirements():
    with open(REPLACEMENTS) as f_r:
        r = f_r.read().split('\n')
        d = []
        for ln in r:
            k, v = ln.split('=>')
            d.append((k.strip(), v.strip()))
    return d

def read_medicine():
    with open(MEDICINE) as f_m:
        return f_m.read().strip()
    

def func():
    reqs = read_requirements()
    meds = read_medicine()

    new_meds = set()
    # Do exactly one replacement on every possible location
    for k, v in reqs: 
        base_string = meds
        
        occurrences = [(m.start(), m.end()) for m in re.finditer(k, base_string)]
        for s, e in occurrences:
            new_string = base_string[:s] + v + base_string[e:]
            new_meds.add(new_string)
    print(len(new_meds))
func()