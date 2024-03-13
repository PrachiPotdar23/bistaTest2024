list1=[1,2,3]
list2=[4,5,6]

result=[(num1,num2) for num1 in list1 for num2 in list2 if((num1+num2)%2==0)]
print(result)