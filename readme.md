# Perfect Numbers

In [number theory](https://en.wikipedia.org/wiki/Number_theory), a perfect number is a [positive integer](https://en.wikipedia.org/wiki/Natural_number) that is equal to the sum of its positive [divisors](https://en.wikipedia.org/wiki/Divisor), excluding the number itself. For instance, 6 has divisors 1, 2 and 3 (excluding itself), and 1 + 2 + 3 = 6, so 6 is a perfect number. 

Definition used from [Wikipedia](https://en.wikipedia.org/wiki/Perfect_number) (24/10/23)

#### First 5 Perfect Numbers:
| Position | 1    | 2    | 3    | 4    | 5    |
| :---:   | :---: | :---: | :---: | :---: | :---: |
| Number | 6   | 28   | 496 | 8128 | 33550336 |

#

I first found out about this pattern in computer science class, when my teacher challenged me to find the second perfect number and only told me how and why the 6 was one. I found it using an algorithm similar to the one in the ```prove-perfect directory``` and eventually ended up researching and analyzing perfect numbers, without any kind of pre-knowledge or information.

## My Calculations:

These are the final results of my calculations:

```py
n = 3 # can be any odd number
m = int(n*0.5)
r = (2**n)-(2**m)
```
Result (r) can only be perfect under two conditions:

```py
c1 = n-m        # result must be prime
c2 = 2**(n-m)-1 # result must be prime
```

Here is an example:

```py
n = 3
m = int(n*0.5) = 1

c1 = 3-1 = 2      # is prime
c2 = (2**3)-1 = 7 # is prime

r = (2**3)-(2**1) = 6
```

The number 6 is the first perfect number. I used the number 3 for n, since ```3-1``` equals 2, which is the first prime number.

The calculation works if both conditions are met, but actually the second condition would be enough, if it turned out true. There are cases where ```n-m``` is prime, but the second condition isn't met, such as this one:

```py
n = 21
m = int(n*0.5) = 10

c1 = 21-10 = 11       # is prime
c2 = (2**11)-1 = 2047 # is not prime
```

Since 2047 is not a prime number, the result won't be a perfect number.

Eventually, I came up with a python algorithm, which can (in theory) find all possible perfect numbers. I've included the first condition, because it saves time if it is immediately not met. 

Here is my algorithm:

```py
def ifPrime():
    # fast algorithm for checking if a number is prime
    return True # or False

def perfectNumber(n):
    m = int(n * 0.5)
    if isPrime(n-m) and isPrime(2**(n-m) - 1): # checks both conditions
        result = (2**n) - (2**m)
        return True, result
    else:
        return False

i = 3 # starts with 3 since, as mentioned earlier, this gives you the first perfect number (6)
while True:
    result = perfectNumber(i)
    if result:
        print(result)
    i += 2 # always adds 2, so the numbers stay odd
```

The fastest checking of prime numbers can be achieved with the [Miller-Rabin Test](https://crypto.stanford.edu/pbc/notes/numbertheory/millerrabin.html#:~:text=The%20Miller%2DRabin%20Test,a%20square%20root%20of%201.), which I tested with my algorithm. This resulted in me getting the first 20 perfect numbers in under a second. It is important to notice that the test is not 100% accurate, so please research the topic for further information. I implemented the test to my perfect number algorithm and uploaded it to the ```miller-prime directory```.

#
