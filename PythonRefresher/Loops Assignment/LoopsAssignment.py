"""
Given the variable my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
- Create a while loop that prints all elements of the my_list variable 3 times.
- When printing the elements use a for loop to print the elements
- However, if the element of the for loop is equal to Monday, continue without printing
"""


my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

x = 0
while x < 3:
    x += 1
    for i in my_list:
        if i == "Monday":
            print("------")
            continue
        print(i)

















