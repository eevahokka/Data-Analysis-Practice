### Write a function that, given an array A of N integers, returns the smallest positive integer that does NOT occur in A.
### E.g. if A = [1, 3, 6, 4, 1, 2], the function returns 5
### If A = [1, 2, 3, 4, 5], the function returns 6
### If A = [-10, −1, −3], the function returns 1

### Follow the assumptions:
### - N is an integer within the range [1, ..., 100,000];
### - each element of array A is an integer within the range [−1,000,000, ..., 1,000,000]

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


### What happens:
### Input: [1, 3, 6, 4, 1, 2]
### N = 6
### Initialize found = [0, 0, 0, 0, 0, 0, 0] (7 values)

### Loop through each number:
### 1 → mark found[0] = 1 (i.e. found[1-1])
### 3 → mark found[2] = 1 
### 6 → mark found[5] = 1
### 4 → mark found[3] = 1
### 1 → already marked
### 2 → mark found[1] = 1
### Now found = [1, 1, 1, 1, 0, 1, 0]

### Loop through found:
### Index 0 → 1
### Index 1 → 1
### Index 2 → 1
### Index 3 → 1
### Index 4 → 0 → Return 5 (i.e. i + 1) 
    

