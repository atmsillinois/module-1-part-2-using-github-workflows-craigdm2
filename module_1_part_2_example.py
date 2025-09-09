"""Calculate and display the ratio between favorite and least favorite numbers.

This script asks the user for their favorite and least favorite numbers,
then calculates and prints the ratio between them. Division by zero is
handled with an error message.
"""

fav_num = input("Input your favorite number: ")
fav_num = float(fav_num)

least_fav_num = input("Input your least favorite number: ")
least_fav_num = float(least_fav_num)

while least_fav_num == 0:
    print("Error: Please pick a number other than 0")
    least_fav_num = input("Input your least favorite number: ")
    least_fav_num = float(least_fav_num)

ratio = fav_num / least_fav_num
print("The number fav:least fav number ratio is: " + str(ratio))
