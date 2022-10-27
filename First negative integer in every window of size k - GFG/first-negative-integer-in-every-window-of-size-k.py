#User function Template for python3
from collections import deque
def printFirstNegativeInteger( A, N, K):
    # code here
    i, j = 0, 0
    result = []
    q = deque()
    while j < N:
        if A[j] < 0:
            q.append(A[j])
        if j - i + 1 < K:
            j += 1
        elif j - i + 1 == K:
            if len(q) == 0:
                result.append(0)
            else:
                result.append(q[0])
            if A[i] < 0:
                q.popleft()
            j += 1
            i += 1
    return result
            
    
    return result
    # for i in range(K):
    #     if A[i] < 0:
    #         q.append(i)
    
    # for i in range(K, N):
        
    #     if len(q) == 0:
    #         result.append(0)
    #     else:
    #         result.append(A[q[0]])
    #     while q and q[0] <= i - K:
    #         q.popleft()
    #     if A[i] < 0:
    #         q.append(i)
    # if len(q) == 0:
    #     result.append(0)
    # else:
    #     result.append(A[q[0]])
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends