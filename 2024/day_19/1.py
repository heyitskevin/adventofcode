from collections import defaultdict

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
        if target == '':
            return True
        if target in dp and dp[target] is not None:
            return dp[target]
        dp[target] = False

        for sub in substrings:
            l =len(sub)
            start = target[:l]
            rest = target[l:]
            if start == sub and composable(rest, substrings):
                dp[target] = True
        
        return dp[target]



    for d in designs:
        if composable(d, ts):
            res += 1

    return res

print(main())