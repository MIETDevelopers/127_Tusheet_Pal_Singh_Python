#rotate a list in a list at a particular index
my_list = [[1,2,3,], [5,2,6]]
arrayRotate = int(input(("Enter the list index: ")))
reverseList = list(reversed(my_list[arrayRotate]))


for i in range(0, len(my_list)):
    if arrayRotate== i:
        reverseList = list(reversed(my_list[arrayRotate]))
        print(reverseList)
    else:
        print(my_list[i])
