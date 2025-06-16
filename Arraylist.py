#1.Sorting an array in Python
from array import *
a=array('i', [27, 32, 43, 74, 56, 89, 12, 45, 67, 90, 10])
print(sorted(a))

#2. Finding the maximum and minimum elements in an array
print("Maximum element in the array:", max(a))  
print("Minimum element in the array:", min(a))

#3. Reversing an array
print("Reversed array:", a[::-1])       

#4. Merging two arrays
b=array('i', [10, 20, 30, 40, 50])      
merged_array = a + b
print("Merged array:", merged_array)

#5. Finding the sum of all elements in an array
print("Sum of all elements in the array:", sum(a))  

#6. Finding the average of all elements in an array
average = sum(a) / len(a)   
print("Average of all elements in the array:", average)

#7. Finding the index of a specific element in an array
element = 32
def find_index(a, element):
    try:
        index = a.index(element)
        return index
    except ValueError:
        return -1
print(find_index(a,27))

#8. Counting occurrences of a specific element in an array
def count_occurrences(a, element):
    return a.count(element)
print(count_occurrences(a,27))

#9. Removing duplicates from an array
def remove_duplicates(a):
    return array('i', list(set(a))) 

#10. Finding the intersection of two arrays
def intersection(arr1, arr2):
    return array('i', list(set(arr1) & set(arr2)))
print(intersection(a,b))

#11. Finding the union of two arrays
def union(arr1, arr2):
    return array('i', list(set(arr1) | set(arr2)))  
print(union(a, b))

#12. Creating a list of n prime numbers
n = int(input("Enter a number:  "))
count = 0
for i in range(2,n+1):
    count = 0
    for j in range(1,i+1):
        if i%j == 0:
            count+=1
    if count==2:
        print(i)
            
  