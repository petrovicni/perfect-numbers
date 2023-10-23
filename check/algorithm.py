# i am saving the process to a txt file, so everything can be proven and all steps checked
def checkPerfectNumber(number: int):
    if number % 2: # checks if the number is even or odd, since perfect numbers cant be odd
        open("process.txt", "a+").write("perfect number can not be odd")
        return False
    else:
        open("process.txt", "a+").write(f"number {number} halved, since everything above the half would not be an integer\n")
        indicator = number // 2 # indicator (variable the number is devided with), created by deviding with two, since everything above can not be an integer
        holder = 0 # for appending the indicators which work have an integer as result, when being devided withthe number
        while True:

            if int(indicator) == 0: # checks if indicator has reached 0
                if holder == number: # checks if the number equals all the appended values in the holder variable
                    open("process.txt", "a+").write(f"number is equal to the sum of its proper divisors (perfect)")
                    return True
                else:
                    open("process.txt", "a+").write(f"number is not equal to the sum of its proper divisors (not perfect) | number: {number} | sum: {holder}")
                    return False
            
            else:
                if number % indicator == 0: # checks if number devided by indicator is an integer
                    result = number // indicator # calculates the result of number/indicator
                    holder += indicator # appends value, since it is an integer
                    open("process.txt", "a+").write(f"{number} : {indicator} = {result} | holder variable appended: {indicator} | current value: {holder}\n")
                else:
                    result = round((number / indicator), 2) # result rounded to save space in the text file
                    open("process.txt", "a+").write(f"{number} : {indicator} = {result} | result is not an integer\n")
                
                indicator -= 1 # indicator decreased by one

if __name__ == "__main__":
    number = int(input("number to check: ")) # user can input number to check
    open("process.txt", "w") # clear old process.txt
    if checkPerfectNumber(number): # runs func and checks if number is perfect
        print("checked number is perfect number!")
    else:
        print("checked number is not perfect number")
