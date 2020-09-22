1st = [10, 15, 3, 7]
k = 17
def two_sum(1st, k):
    for i in range(len(1st)):
        for j in range(len(1st)):
             if i !=j and 1st[i] + 1st[j] == k:
                return True 

    return False 