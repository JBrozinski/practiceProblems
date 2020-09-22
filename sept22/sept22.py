#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

def two_sum(lst, k):
    for i in range(len(lst)):
        for j in range(len(lst)):
             if i !=j and lst[i] + lst[j] == k:
                return True 

    return False 

print two_sum([10, 15, 3, 7], 17)