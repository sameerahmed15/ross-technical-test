# Sorting Algorithm (partial flips)
This code includes two functions that can be used to sort a list of integers from smallest to highest using partial flips.

## Strategy
Flip from the maximum number index. Bring max num to index 0.\
Then flip from last element so that the max is at the end of list.
Decrement max and last everytime they are used as index for flipping.\
Let's test this on the list [3,2,4,1].
* Flip the sub-array from index 2: [4, 2, 3, 1]
* Flip the sub-array from index 3: [1, 3, 2, 4]
* Flip the sub-array from index 1: [3, 1, 2, 4]
* Flip the sub-array from index 2: [2, 1, 3, 4]
* Flip the sub-array from index 1: [1, 2, 3, 4]


## partial_flip function
This function takes an array of integers and an index value from where the array will be reversed. It then reverses the sub-array starting from the given index and returns the modified array.

## sorting function
This function takes an array of integers and sorts it from smallest to highest using partial flips. It first finds the maximum value in the array and shifts it to the beginning of the array. It then shifts the maximum value to the end of the unsorted portion of the array. It repeats this process until the array is sorted.

## Usage
To use the sorting function, pass a list of integers as an argument. The function will return a list of indices representing the partial flips needed to sort the list.

Example usage:
```python
sorting([3,2,4,1])
# Output: [3,4,2,3,1,2]
```