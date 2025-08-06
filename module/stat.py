def mean(number):
    """
    This function returns the mean of numbers
    """
    return sum(number)/len(number)

def median(numbers):
    """
    This fucntion returns the median of all
    given numbers. Sort the list if not sorted
    """
    numbers.sort()
    if len(numbers)%2 == 0:
        num1 = numbers[len(numbers) //2]
        num2 = numbers[len(numbers)//2-1]

        mymedian = ( num1 + num2 )/ 2
    else :
        mymedian = numbers[len(numbers) // 2]
    
    return mymedian
    
