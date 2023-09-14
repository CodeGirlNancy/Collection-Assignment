#Change 80 with 89 in the list
student_marks=[60, 80, 90, 98]
student_marks[1]=89
print(student_marks)

#add a new item 55(append a new list)
student_marks=[60, 80, 90, 98]
student_marks.append(55)
print(student_marks)

#find the size of the list having appended 55
print(len(student_marks))

#write a python programme to sum all the items in the list
total=sum(student_marks)
print(total) 

#python function that takes two lists and returns, if they have atleast a common member
list1 = input("Enter items:")
list2 = input("Enter items:")
if "common number"in list1 and list2:
    print("True, there is a common number in list1 and list2")
    
else:
    print("False, common number dont exist")
