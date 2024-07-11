FILENAME = "input.txt"

def read_file():
    with open(FILENAME) as f:
        return f.read().strip()
    

def func():
    a = read_file()
    filesize = 272
    while len(a) < filesize:
        b = "".join(["0" if int(c) == 1 else "1" for c in a[::-1] ])
        a = a + "0" + b
    a = a[:filesize]
    while (len(a) % 2) == 0:
        temp = ""
        for ix in range(0,len(a)-1, 2):
            if a[ix] == a[ix+1]:
                temp += "1"
            else:
                temp += "0"
        a = temp
    print(a)

func()