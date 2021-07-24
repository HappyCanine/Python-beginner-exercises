#Consider the following string: nums = '10,20,30,40,50'
#Create a Python script that creates a list of integers from the string.
#The resulting list will be: [10, 20, 30, 40, 50]

nums = '10,20,30,40,50'
nums_split = nums.split(',') # => ['10', '20', '30', '40', '50']
int_nums = [int(i) for i in nums_split]
int_nums # => [10, 20, 30, 40, 50]
