#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
#Example: maximum([]) should return False

#Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
#Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

#Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
#Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]


def biggie_size(big_list):
    for i in range(len(big_list)):
        if big_list[i] > 0:
            big_list[i] = "big"
    return big_list

print (biggie_size([2,-4,5,6]))

def count_positives(lst):
    last = 0
    for i in lst:
        if i > 0:
            last += 1
    lst [-1] = last
    return lst

print (count_positives([1,2,3,5]))

        

print (biggie_size([2,-4,5,6]))

def sum_total(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

print (sum_total([2,3,4]))

def average(lst):
    total = 0
    for i in lst:
        total += i 
    return float(total)/ float(len(lst))

print (average([1,3,4,5]))

def length(lst):
    count = 0
    for i in lst:
        count += 1
    return count

print (length([]))

def minimum(lst):
    if len(lst) == 0:
        return False

    min = lst[0]
    for i in lst:
        if i < min:
            min = i
    return min

print (minimum([2,3]))

def maximum(lst):
    if len(lst) == 0:
        return False
    
    max = lst[0]
    for i in lst:
        if i > max:
            max = i 
    return max

print (maximum([3, 4, 13, 15]))
        
def ultimate_analysis(lst):
    result = {
        'sum_total' : None,
        'average' : None,
        'minimum' : None,
        'maximum' : None,
        'length' : 0
    }
    
    if len(lst) == 0: 
        return result
    else:
        result['sum_total'] = 0
        result['minimum'] = 0
        result['maximum'] = 0
    
    for val in lst:
        if val > result['maximum']:
            result['maximum'] = val
        elif val < result['minimum']:
            result['minimum'] = val

        result['sum_total'] += val
        result['length'] += 1

    result['average'] = result['sum_total']/ len(lst)

    return result

print(ultimate_analysis([37, 2, 1, -9]))   

def reverse_list (nums_list):
    list_len = len(nums_list)
    for idx in range(list_len/2):
        temp = nums_list[list_len-1-idx]
        nums_list[list_len-1-idx] = nums_list[idx]
        nums_list[idx] = temp
    return nums_list


print(reverse_list([3,1,6,10,-5,6]))

    

