input_list=["Python is a powerful programming language","Python is used for web development","Python has a rich set of libraries"]
word_count={}
word_list=[]
for i in range(len(input_list)):
    word_list.extend(input_list[i].split(" "))
    
for word in word_list:
    word_count[word]=word_list.count(word)
    
print(word_count)