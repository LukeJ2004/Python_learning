# My name is Lukhanyiso Jikela
# In this program we are looking at how
# and why loops are so useful

# This program utilises a for loop
# for determining how many valid postive numbers 
# were entered by the user in order
# to get a total of 100

count = 0
running_total = 0
while True:
    user_input = input("Enter a positive integer:\n")
    user_input = int(user_input)
    if user_input < 0: 
        print("The number you have entered is incorrect. You have no more attempts.")
        break
    if user_input == 0: 
        print("You have made the incorrect selection. Please try again.")
        continue
    if user_input > 0 : 
        running_total+=user_input
        count+=1
    if running_total > 100: 
        print("The total sum is:", running_total)
        print("The total number of digits used is:", count)
        break
