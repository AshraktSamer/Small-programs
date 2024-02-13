
myDic={}  #creat dici
n = int(input("please enter the number of students : "))     # take num of students
for stud in range(n):
   name , *line = input().split()  #split line to take first string = name ,, and rest of line in list = line
   score =list(map(float,line))    # convert line into list of floats
   myDic[name] = score             # save in dici key=name , value = score 

for name , score in myDic.items():
    print("name of student is :" , name , "and their scores are" , score)
# just a loop to show the dici

# here i take the name a input
searched_name= input("please enter student name you want to calcualte average of its score")
list1= list(myDic[searched_name]) # i creat w new list have the copy of value to the name(key) from dictionry
add=sum(list1) # as it easier to do math oper on list than dici
average=add/len(list1)
print('%.2f'% average)