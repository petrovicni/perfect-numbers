def test(x: int):
    if x % 2:
        l = 0
    else:
        r = x // 2
        a = 0
        while True:

            print(f"Schleife ist: {r}")

            if int(r) == 0:
                if a == x:
                    print(f"Die Zahl: {x} ist eine Komplette Zahl!")
                    break
                else:
                    break
            
            else:
                if x % r == 0:
                    print(f"Rest von {x}:{r} = 0")
                    a += r
                    r -= 1
                else:
                    r -= 1
                    continue

test(28) # zahl ersetzen und überprüfen ob komplett
