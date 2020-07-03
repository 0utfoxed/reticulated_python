# The 'continue' keyword, used within a loop, skips the remaining code in the loop block, instead proceeding on to the next iteration. In the following example, 'continue' is leveraged to print only the positive numbers stored in a list.

big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

for i in big_number_list:
	if i < 0:
		continue
	print(i)
