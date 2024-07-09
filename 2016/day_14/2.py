# No C++ solution b/c the MD5 library is clunky and I'm lazy
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
        for _ in range(2016):
            s = hashlib.md5(str.encode(s, "utf-8")).hexdigest()
        m = re.findall(five, s)
        t = re.findall(three, s)
        
        if t:
            threes_lookup[s] = new_hash
        if m:
            for match_seq in m:
                match_cara = match_seq[0]
                if ix > 1000:
                    look_back = ix - 1000
                else:
                    look_back = 0
                for past in seen[look_back:]:
                    mm = re.findall(three, past)
                    if mm and past != s:
                        if mm[0][0] == match_cara:
                            # print(past, s, ix, threes_lookup[past])
                            keys.append(past)
        ix += 1
        seen.append(s)
    
    print(sorted(set( # Some hashes come up twice so we need to dedupe
        [int(threes_lookup[v][len(salt):] )for v in keys])
        )[63])

func()
