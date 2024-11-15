
import sys

nums = []

for line in sys.stdin:
    nums.append(int(line.strip()))

for num in nums:
    i = 2
    while i <= num:
        if num % i == 0:
            num = num / i
            print(f"{i} ", end='')
            i = 2
        else:
            i += 1     

    print("")