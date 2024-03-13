def prime_nums():
    flag=True
    for num in range(2,21):
        flag=True
        for i in range(2,num):
            if(num%i==0):
                flag=False
        if(flag):
            yield num

for number in prime_nums():
    print(number)    