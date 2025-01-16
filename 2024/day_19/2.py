from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

def readfile():
    towels, designs = [], []

    with open('input.txt') as f:
        lns = f.read().split('\n')
        towels = [k.strip() for k in lns[0].split(',')]
        for l in lns[1:]:
            if l:
                designs.append(l.strip())

    return towels, designs

def main():
    ts, designs = readfile()
    ts = set(ts)
    res = 0

    dp = {}
    
    def composable(target, substrings):
        if target in dp:
            return dp[target]
        count = 0
        
        if target == '':
            count = 1
        for sub in substrings:
            l = len(sub)
            start = target[:l]
            end = target[l:]

            if start == sub:
                count += composable(end, substrings)
        dp[target] = count

        return count


    for d in designs:
        res += composable(d, ts)
    
    return res

print(main())
