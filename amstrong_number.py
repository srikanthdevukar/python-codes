def armstrong_number(n):    
    num = len(str(n))    
    sum_of_numbers = sum(int(digit) ** num for digit in str(n))        
    return sum_of_numbers == n
armstrong_numbers = []
for i in range(1000,9999):
    if armstrong_number(i):
        armstrong_numbers.append(i)
print(armstrong_numbers)
