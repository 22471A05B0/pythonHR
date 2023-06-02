import numpy as np
arr = np.array([input().split() for _ in range(int(input().split()[0]))], int)
print(np.mean(arr,axis=1), np.var(arr,axis=0), round(np.std(arr),11), sep='\n')
