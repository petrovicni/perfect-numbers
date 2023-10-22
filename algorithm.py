# fastest i could come up with using python
import concurrent.futures

biggest = 100**2149  # biggest number python can print out
threads = 500        # max checks at once your pc can handle

def perfectnum(number: int):
    if number % 2:
        return
    else:
        indicator = number // 2
        holder = 0
        while True:

            if int(indicator) == 0:
                if holder == number:
                    open("perfect.txt", "a+").write(f"{number}\n")
                    break
                else:
                    break
            
            else:
                if number % indicator == 0:
                    holder += indicator
                    indicator -= 1
                else:
                    indicator -= 1
                    continue

def threading():
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(perfectnum, i) for i in range(1, biggest)]
        for future in futures:
            future.result()

if __name__ == "__main__":
    threading()
