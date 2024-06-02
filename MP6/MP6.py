def bruteForce(k, n, m, w):
    if k == 0 or n == 0:
       return 0
    if (m[n-1] > k):
       return bruteForce(k, n-1, m, w)
    else:
       return max(w[n-1] + bruteForce(k-m[n-1], n-1, m, w),
          bruteForce(k, n-1, m, w))
 
 
if __name__ == '__main__': 
    w = [60, 100, 120] 
    m = [10, 20, 30] 
    k = 50
    n = len(w)
    print(bruteForce(k, n, m, w))
    