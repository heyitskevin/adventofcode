# No C++ solution b/c the MD5 library is clunky and I'm lazy

# Steps
# - make hash
# - add hash to list of history
# - if 5 consecutive charas
# - look backwards 1000 for corresponding hash
# - if condition is fulfilled then add corresponding hash to valid keys
# - break when 64 keys
import hashlib
import re

def func():
    salt = "qzyelonm"
    # salt = "abc"
    ix = 0
    keys = []
    seen = []
    five = r"(.)\1{4}"
    three = r"(.)\1{2}"
    threes_lookup = {}
    while len(keys) < 80: # Go extra to catch all
        new_hash = f"{salt}{ix}"
        s = hashlib.md5(str.encode(new_hash)).hexdigest()
        
        m = re.findall(five, s)
        t = re.findall(three, s)
        
        if t:
            threes_lookup[s] = new_hash
        if m:
            for match_seq in m:
                match_cara = match_seq[0]
                look_back = max(ix, 1000)
                if ix > 1000:
                    look_back = ix - 1000
                else:
                    look_back = 0
                for past in seen[look_back:]:
                    mm = re.findall(three, past)
                    if mm and past != s:
                        if mm[0][0] == match_cara:
                            keys.append(past)
        ix += 1
        seen.append(s)
    
    print(sorted(
        [int(threes_lookup[v][len(salt):] )for v in keys]
        )[63])

func()
