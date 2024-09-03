import math
def func():
    val = 27
    val = 265149
    rt = math.isqrt(val)
    lower_bound = rt ** 2
    rem_dist = val - lower_bound

    if lower_bound % 2 == 0:
        # we are in bottom half
        arr = [i for i in range(rt, (rt // 2) - 1,  -1)]
        arr += arr[:1:-1]
        arr += arr[1:]
        return arr[rem_dist - 1]
    else:
        # we are in upper half
        arr = [i for i in range(rt, rt //2 , -1)]
        arr += arr[:1:-1]
        arr += arr[1:]
        return arr[rem_dist - 1]
    return -1
    # manhattan dist for each i between isqrt(N) and isqrt(N) + 1
    # is N - isqrt(N)
print(func())