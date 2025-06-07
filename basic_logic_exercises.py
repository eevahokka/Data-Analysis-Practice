# Python exercises
# June 2025
    

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


#### SET 2 ####

### 1. Write a function that returns the second smallest number in a list.

a = [2, 6, -4, -10, 5, 6, 10]

def second_smallest(array):
    
    # order the elements
    sorted_array = sorted(array)
    
    # return second smallest
    return sorted_array[1]

second_smallest(a)

# without using sort
def secsmall_nosort(array):
    
    # Set variables smallest & seconfsmallest to be very larg
    smallest = float('inf')
    secondsmallest = float('inf')
    
    # for number in array
    for num in array:
        
        # check if it is smaller than smallest and smaller than second smallest, update
        if num < smallest:
            secondsmallest = smallest
            smallest = num
        elif smallest < num < secondsmallest:
            secondsmallest = num
    
    # return    
    return secondsmallest

secsmall_nosort(a)


### 2. Given a list of employees with department IDs, group them into a dictionary 
### by department.

employees = [
    {"name": "Jessica", "dept_id": 3},
    {"name": "Bob", "dept_id": 2},
    {"name": "Mollie", "dept_id": 2},
    {"name": "John", "dept_id": 1}
    ]

dept_groups = {}

# loop over each row in list
for emp in employees:
    
    # first, take out each dept_id and name as objects FROM THE INDEXED ROW
    dept_id = emp["dept_id"]
    name = emp["name"]
    
    # if dept_id not yet in dept_groups, add it in
    if dept_id not in dept_groups:
        dept_groups[dept_id] = []
    
    # add the name regardless
    dept_groups[dept_id].append(name)

print(dept_groups)


### 3. Given a dictionary of employee hours, return the name(s) of the employee(s) 
### with the most hours.

# create dataset - note here, it's just keys and values
hours = {
    "Alice": 35,
    "Bob": 42,
    "Charlie": 42,
    "Diana": 30
}

# find out the max hours worked by checking only the values for keys
max_hours = max(hours.values())

# store names and hours, if fit max_hours, into an empty dictionary
top_employees = []

# loop over each row, i.e. key, in hours to see if fits max_hours
for hour in hours:
    
    # if the indexed key in the dictionary has value fitting max_hours
    if hours[hour] == max_hours:
        # add the key (i.e. name) into top_employees
        top_employees.append(hour)
        

print(top_employees)


### 4. Given a list of integers and a target number, count how many unique pairs 
### of elements sum up to the target.
### Example: List = [1, 5, 7, -1, 5]
### Target = 6 → Answer = 3 ((1, 5), (7, -1), (1st 5, 1st 1))
### Hint: first check for difference and whether that's already been seen; then add element to seen


list1 = [1, 5, 7, -1, 5]
target1 = 6

def unique_pairs(array, target):
    
    # create an empty set to store the numbers in for lookup, and initiate counter
    seen = {}
    counter = 0
    
    # for each element in the array
    for element in array:
        
        # calculate the difference with target, to get the missing pair
        difference = target - element
        
        # then see if the difference is in seen
        if difference in seen:
            
            # add the value indexed by difference to counter
            counter += seen[difference]
            
        # if the element itself is in seen
        if element in seen:
            
            # update its count in the dictionary
            seen[element] += 1
        
        # otherwise, add element to dictionary with value 1
        else:
            seen[element] = 1
                
    return counter

unique_pairs(list1, target1)


### 3. Rotate Array
### Given a list and an integer k, return the list rotated to the right by k steps.
### Example: [1, 2, 3, 4, 5], k = 2 → [4, 5, 1, 2, 3]
### pos:     [0, 1, 2, 3, 4]          [0, -4, -3, -2, -1]

list2 = [1, 2, 3, 4, 5, 6, 7, 8]
k = 11

def rotator(array, k):
    
    # initiate new array
    new_array = []
    
    # edge case: make sure N is not 0 so you're not dividing by it
    N = len(array)
    if N == 0:
        return N
    
    # edge case: if k is larger than length of array, divide by length 
    if k > N:
        k = k % N
    
    # make a new array by adding two slices of original together
    new_array = array[-k:] + array[:-k]
    # above:    from 4 to 5  from 0 to 3

    # return new array
    return new_array

rotator(list2, k)


### 6. Find Peak Element
### Given a list of integers, find any "peak" element — an element that is 
### greater than both its neighbors.
### (You may assume the list has at least 3 elements and ignore the ends.)
### Example: [1, 3, 20, 4, 1] → return 20

list3 = [1, 3, 20, 2, 5, 1]

def peaky(list):
    
    # find length of list, set object for peak
    N = len(list)
    peaky = []
    
    # for each element on list, dont include first or last so comparison possible
    for i in range(1, N-1):
        
        # compare with one before and one after
        if (list[i-1] < list[i]) & (list[i+1] < list[i]):
            
            # place into peaky
            peaky.append(list[i])
            
    return peaky

peaky(list3)


### 7. String Compression
### Compress a string using the counts of repeated characters.
### Example: "aaabbccccd" → "a3b2c4d1"
### Note, not needed here: methods to break characters from string into list
### [*stringy]; chars = [char for char in string]

stringy = "aaabbccccdd"

def strcomp(string):
    
    # initiate new string
    new_string = ""
    
    # initiate counter
    count = 1
    
    # for each character in the string
    for char in range(1, len(string)):
        
        # compare if letter the same as previous
        if string[char] == string[char-1]:
            
            # add to counter
            count += 1
        
        # otherwise, add character and count to new string and reset count to 1
        else:
            new_string += string[char-1] + str(count)
            count = 1

    # add last character and it's count
    new_string += string[char-1] + str(count)
    
    return new_string

strcomp(stringy)



### 8. Validate Brackets
### Given a string of brackets ()[]{}, determine if the input is balanced 
### (all opened brackets are closed properly).
### Example: "{[()]}" → valid; "{[(])}" → invalid
### pos:      0 1 2 3 4 5
###           0-5-4-3-2-1

brac1 = "{[()]}"
brac2 = "{[(])}"


def validation(string):
    
    # create a comparison dictionary and empty one for closing bracket storing
    comparison = {"}": "{", "]": "[", ")": "("}
    store = []
    
    # loop over each character
    for char in string:
        
        # if character is an OPENING bracket 
        if char in comparison.values():
        
            # add it in to the empty dictionary
            store.append(char)
            
        # else if it is a CLOSING bracket
        elif char in comparison:

            # and if not in the store, 
            # or the last opening character [-1] added is not matching with the current closing character
            if not store or store[-1] != comparison[char]:  
            
                # return with message "invalid"
                return "invalid"
            
            # otherwise, pop it out
            else:
                store.pop()
            
    return "valid"

validation(brac2)


### 9. First Non-Repeating Character
### Given a string, return the first character that doesn’t repeat. 
### If all characters repeat, return None.
### Example: Input: "aabbccdeff"; Output: "d"

stringy2 = "aaabbccdeff"

def non_repeat(string):
    
    # create an empty dictionary for lookup, initiate counter
    seen = {}
    counter = 1
    N = len(string)
    
    # for each character in the string
    for char in range(1, N):
    
        # check if it's NOT the same as previous
        if string[char] != string[char-1]:
        
            # add the counter into seen (you don't need to store the character), then reset counter
            seen[string[char-1]] = counter
            counter = 1
            
        # else, add +1 into counter
        else:
            counter += 1

    # add the last character in
    seen[string[char-1]] = counter
    
    # loop over each character in the STRING
    for char in string:
        
        # if the character has a value of 1 (use get to find it in dict)
        if seen.get(char) == 1:
            # return the character - first one only returned
            return char

non_repeat(stringy2)


### 10. 2. Count Digits
### Write a function that returns the number of digits in an integer (do not use len(str(n))).
### Example: Input: 10456; Output: 5

input1 = -1047

def digit_count(input):
    
    # take absolute value to handle negatives
    input = abs(input)
    
    # initiate counter
    counter = 0
    
    #
    if input == 0:
        return 1
    
    # while the input is greater than 0
    while input > 0:
        
        # divide the input by 10 (as each digit is some multiple of 10)
        input = input//10
        # and add 1 to counter
        counter += 1
    
    return counter

digit_count(input1)


### 11. Histogram Dictionary
## Write a function that takes a list of words and returns a dictionary with the frequency of each word.
### Example: Input: ["apple", "banana", "apple", "orange", "banana", "apple"]
### Output: {'apple': 3, 'banana': 2, 'orange': 1}

input2 = ["apple", "banana", "apple", "orange", "banana", "orange", "apple"]

def hist_dict(input):
    
    # initialize empty dictionary and counter
    dict = {}
    counter = 0
    
    # for word in input:
    for word in input:
        
        # if the word is NOT in dictionary
        if word not in dict:
        
            # add the word in, set counter to 1, and add the counter
            dict[word] = []
            counter = 1
            dict[word] = counter
            
        # if it is, update the counter
        else:
            dict[word] +=1
        
    return dict

hist_dict(input2)


### 12. Reverse Words in Sentence
### Given a sentence, reverse the order of the words.
### Example: Input: "the quick brown fox"; Output: "fox brown quick the"

input3 = "the quick brown fox"

def revstr(string):
    
    # split the sentence into elements
    string = string.split(" ")

    # reversed the words --> you don't need to save first an empty list
    new_string = string[::-1]

    # turn into one string
    new_string = ' '.join(new_string)
    
    # return into one string
    return new_string

revstr(input3)


