# Create a Python script that asks the user for a number
# and then prints out a list of all the divisors
# of each number less than the asked number.

# If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.

#%%

number = int(input("Please input a number:"))
divisors = [i for i in range(1, number + 1) if number % i == 0]
# range(1 , number + 1) the + 1 at the end is because the list's final range is excluding that last value
# See example below
print("Divisor(s):")
print(divisors)

#%%
test_range = range(1, 10)
distlist = []
for i in test_range:
    distlist.append(i)
print(distlist)
