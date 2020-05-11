def countKdivPairs(A, n, K): 
    freq = [0] * K 
    for i in range(n): 
        freq[A[i] % K]+= 1
    sum = freq[0] * (freq[0] - 1) / 2; 
    
    i = 1
    
    while(i <= K//2 and i != (K - i) ): 
        sum += freq[i] * freq[K-i] 
        i+= 1

    if( K % 2 == 0 ): 
        sum += (freq[K//2] * (freq[K//2]-1)/2); 

    return int(sum) 

A = [2, 2, 1, 7, 5, 3] 
n = len(A) 
K = 4
print(countKdivPairs(A, n, K)) 