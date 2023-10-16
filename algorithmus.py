def komplettezahl(x: int):
    if x % 2:
        l = 0
    else:
        r = x // 2
        a = 0
        while True:

            if int(r) == 0:
                if a == x:
                    print(x)
                    break
                else:
                    break
            
            else:
                if x % r == 0:
                    a += r
                    r -= 1
                else:
                    r -= 1
                    continue

def main():
    i = 0
    while True:
        komplettezahl(i)
        i += 1

main()
