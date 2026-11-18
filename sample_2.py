# wap to check whether the given number is prime or not

def prime_num(num):
    if num<=1:
        return "not prime"
    for i in range(2,num):
        if num %i ==0:
            return "not prime"
    return "prime" 
number=int(input("Enter a number:"))
result=prime_num(number)
print(result)   
