"""Give an input and multiply it."""

fav_num = input("Input your favorite number: ")
fav_num = int(fav_num)
least_fav_num = input("Input your least favorite number: ")
least_fav_num = int(least_fav_num)

if least_fav_num == 0:
    print("Error: Please pick a number other than 0")
else:
    ratio = fav_num / least_fav_num
    print("The number fav:least fav number ratio is: " + str(ratio))
