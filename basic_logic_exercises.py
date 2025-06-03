# Python exercises
# 3 June 2025
    

# 1. First Duplicate
# Problem: Given an array A of integers, return the first number that appears more than once. 
# If no number appears more than once, return -1.

# Example:
# A = [2, 1, 3, 5, 3, 2] → Output: 3
# A = [1, 2, 3, 4] → Output: -1

A =  [1, 2, 3, 4, 4, 2]

def dupli(array):
    storage = []
    for a in array:
        if a in storage:
            return a
        else:
            storage.append(a)
            
    return -1


dupli(A)



# 2. Missing Number in Sequence
# Problem:
# Given an array of size N containing numbers from 1 to N+1 with one number missing, 
# return the missing number.

# Example:
# A = [2, 3, 1, 5] → Output: 4


array = [2, 1, 4, 5]

def miss(array):
    # record the length of array to know what your range should be
    N = len(array)
    
    # create an empty array to store seen values, +2 bc you need to include last value + missing
    seen = [0] * (N+2)
    
    # for each element a in array...
    for a in array:
        
        # check if element a is in between 1 and N+2; if so, record 1 
        if 1 <= a <= N+2:
            seen[a] = 1
        # if not, record 0 - also, when a as an index is not included, i.e. is missing!
        else:
            seen[a] = 0
    
    # for each element in seen, if the value is 0, return the index = missing number
    for i in range(1, N+2):
        if seen[i] == 0:
            return i


miss(array)


# 3. Find All Missing Positive Integers
# Problem:
# Given an unsorted array, find all positive integers that are missing in the range 1..N.

# Example:
# A = [4, 3, 2, 7, 8, 2, 3, 1] → Output: [5, 6]

array2 = [4, 3, 2, 7, 8, 2, 3, 1, 9, 11]

def miss_pos(array):
    
    # Sort the array to find min and max values
    sorted_array = sorted(array)
    
    # Find how many values you should have if none were missing
    shouldve = list(range(min(sorted_array), max(sorted_array) + 1, 1))
    
    # record the length of the array to know what your range should be
    S = len(shouldve)
    
    # Create an empty array for all numbers you should have here
    seen = [0] * (S + 1)
    
    # Create an array for missing positive integers
    miss_pos = []
    
    # For each element a in array...
    for a in array:
       
        # check if element a is in between 1 and S+1; if so, record 1
        if 1 <= a <= S + 1:
            seen[a] = 1
        
        else:
            seen[a] = 0
      
    # For each iteration         
    for i in range(1, S+1):
        if seen[i] == 0:
           miss_pos.append(i)
           
    return miss_pos

miss_pos(array2)


# 4. Count Distinct Integers
# Problem:
# Return the number of distinct integers in the array.

# Example:
# A = [2, 1, 1, 2, 3, 1] → Output: 3


array3 = [2, 1, 3, 4, 1]

def dist_int(array):
    
    N = len(array)
    
    # create an empty vector for distinct integers    
    dist = []
    
    # For each element a in array (except last one not needed)...
    for a in range(N-1):
        
        count = 0
        # compare it to each element after (a+1) in the array
        for j in range(a+1, N):
            
            # if an element is similar to another one,add 1 to counter, otherwise 0
            if array[a] == array[j]:
                count += 1
            else:
                count = 0
        
        # if counter totals 0, integer distinct!
        if count == 0:
            dist.append(array[a])

    return dist

dist_int(array3)


###
5. Check if Array is a Permutation
Problem:
Check if array A contains all numbers from 1 to N exactly once.

Example:

A = [4, 1, 3, 2] → Output: True  
A = [4, 1, 3] → Output: False

###

array4 = [4, 1, 2, 3, 5, 5]

def perm(array):
    
    ## If array contains all numbers from 1 to N....
    #all_num = []
    
    # Sort the array to find min and max values
    sorted_array = sorted(array)
    
    # Find how many values you should have if none were missing
    shouldve = list(range(min(sorted_array), max(sorted_array) + 1, 1))
    
    # record the length of the array to know what your range should be
    S = len(shouldve)
    
    # Create an empty array for all numbers you should have here
    seen = [0] * (S + 1)
    
    # Create an array for missing positive integers
    miss_pos = []
    
    # For each element a in array...
    for a in array:
       
        # check if element a is in between 1 and S+1; if so, record 1
        if 1 <= a <= S + 1:
            seen[a] = 1
        
        else:
            seen[a] = 0
      
    # For each iteration         
    for i in range(1, S+1):
        if seen[i] == 0:
           return False
        else:
           pass
    
    
    ## ... exactly once
    # determine array length
    N = len(array)
    
    # For each element a in array (except last one not needed)...
    for a in range(N-1):
        
        count = 0
        # compare it to each element after (a+1) in the array
        for j in range(a+1, N):
            
            # if an element is similar to another one,add 1 to counter, otherwise 0
            if array[a] == array[j]:
                count += 1
            else:
                count = 0
        
        # if counter totals 0, integer distinct!
        if count != 0:
            return False
        else:
            pass
    
    return True


perm(array4)


# 6. Longest Consecutive Sequence
# Problem:
# Given an unsorted array, find the length of the longest sequence of consecutive numbers.

# Example:
# A = [100, 4, 200, 1, 3, 2] → Output: 4 (because 1,2,3,4)


array5 = [100, 4, 200, 1, 2, 3, 5]

def conseq(array):
    
    N = len(array)
    
    # sort the array
    sorted_array = sorted(array)
    
    # running counters for maximum sequence of consecutive numbers
    max_count = 0
    
    # start the counter
    counter = 0
    
    # for each element a in array...
    for a in range(0, N-1):
        
        # comparing it to the next element, if the difference is 1
        if sorted_array[a+1] - sorted_array[a] == 1:
            
            # then add to counter
            counter += 1
        
    # update max counter after each run
    if counter > max_count:
        max_count = counter
    
    # if max_count has consecutive numbers
    if max_count > 0:
        # add +1 to it to correct for total consecutive numbers instead of number of comparisons made
        max_count += 1
    
    return max_count

conseq(array5)


# 7.  Smallest positive integer
# Problem
# Write a function that, given an array A of N integers, returns the smallest positive integer that does NOT occur in A.

# Example:
# if A = [1, 3, 6, 4, 1, 2], the function returns 5
# If A = [1, 2, 3, 4, 5], the function returns 6
# If A = [-10, −1, −3], the function returns 1


def solution(A):
  N = len(A)
  # Create an array of zeros where to store checks between A and N
  found = [0] * (N + 1)

  # Loop over each element in A
  for a in A:
    # If an element is between 1 (smallest positive number) and N
    if 1 <= a <= N:
      # Mark 1 into the respective index (a - 1) of found (note: indexing starts with 0, hence -1)
      found[a - 1] = 1

  # Loop over each value in N
  for i in range(N):
    # Check whether the value of N in found-array is 0, i.e. not in A
    if found[i] == 0:
      # In which case, return the value as index + 1 to get the smallest positive integer
      return i + 1

  # If each value of N is in A, then the smallest positive integer is N + 1
  return N + 1


# Explanation:
# Input: [1, 3, 6, 4, 1, 2]
# N = 6
# Initialize found = [0, 0, 0, 0, 0, 0, 0] (7 values)

# Loop through each number:
# 1 → mark found[0] = 1 (i.e. found[1-1])
# 3 → mark found[2] = 1 
# 6 → mark found[5] = 1
# 4 → mark found[3] = 1
# 1 → already marked
# 2 → mark found[1] = 1
# Now found = [1, 1, 1, 1, 0, 1, 0]

# Loop through found:
# Index 0 → 1
# Index 1 → 1
# Index 2 → 1
# Index 3 → 1
# Index 4 → 0 → Return 5 (i.e. i + 1) 
