def two_sum(lst, k):
    for i in range(len(lst)):
        for j in range(len(lst)):
             if i !=j and lst[i] + lst[j] == k:
                return True 

    return False 

print two_sum([10, 15, 3, 7], 17)