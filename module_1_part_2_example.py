"""Give an input and multiply it."""

fav_num = input("Input your favorite number: ")
fav_num = int(fav_num)
least_fav_num = input("Input your least favorite number: ")
least_fav_num = int(least_fav_num)

ratio = fav_num / least_fav_num
print("The number fav:least fav number ratio is: " + str(ratio))
