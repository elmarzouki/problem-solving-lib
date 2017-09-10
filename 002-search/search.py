# Binary search: https://en.wikipedia.org/wiki/Binary_search_algorithm
def binarySearch(numbers, item):
    first = 0
    last = len(numbers)-1

    while first <= last:
        midPoint = (first + last)//2
        if numbers[midPoint] == item:
            return True
        else:
            if item < numbers[midPoint]:
                last = midPoint-1
            else:
                first = midPoint+1

    return False

# Example
testList = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testList, 3))
print(binarySearch(testList, 13))