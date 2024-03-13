def is_prime(num):
    flag=True
    for i in range(2,num):
        if(num%i==0):
            flag=False
            
    if(flag):
        print(num)
            

list1=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list2=list(filter(is_prime,list1))
print(list2)

