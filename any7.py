def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    # YOUR CODE HERE 
    # for in loop over nums 
    for num in nums:
        # if num == 7 
        if num == 7:
            # return True 
            return True 
    # return false here 
    else:
        return False

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

