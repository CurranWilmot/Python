#1

def count_down(num):
    count_list = [] #initializes an empty list
    for i in range(num, -1, -1):
        count_list.append(i) #adds a number one less than the previous until reaching 0
    return count_list

print(count_down(5))

#2

def print_and_return(nums):
    print(nums[0])
    return nums[1]

numbers = [3, 4]
print(print_and_return(numbers))

#3

def first_plus_length(nums):
    return nums[0] + len(nums)

print(first_plus_length(numbers))

#4

burrito = [3, 2, 4, 6, 1, 1, 5, 1]
def values_greater_than_second(nums):
    nums2 = []
    for i in nums:
        if i > nums[1]: #runs through values of list, checks if they are
            nums2.append(i)#less than the second term in the list
    if len(nums2) < 2:#if they are, then they are not added to new list
        return False
    else:
        print(len(nums2))
        return nums2

print(values_greater_than_second(burrito))


#5

def this_lenth_that_value(size, value):
    values = []
    for i in range(0, size): #runs a loop from 0 to size, and creates a value
        values.append(value)#equal to value on each index
    return values

print(this_lenth_that_value(3, 4))
