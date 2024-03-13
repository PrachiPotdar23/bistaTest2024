
def is_prime(num):
    flag=True
    for i in range(2,num):
        if(num%i==0):
            flag=False
            
    if(flag):
        return num
            

list_prime=[num for num in range(2,100) if(is_prime(num))]
print(list_prime)