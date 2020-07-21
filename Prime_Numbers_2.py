#Print the prime numbers which are between 1 to entered limit number (n).

n = int(input("Please enter a number : "))
numbers = list(range(1,n+1))
prime_list = []
for j in numbers :
    count = 0
    for i in range(1, n+1) :
        if  not (j % i) :
            count += 1
    if not((j == 0) or (j == 1) or (count >= 3)) :
        prime_list.append(j)
print(prime_list)
