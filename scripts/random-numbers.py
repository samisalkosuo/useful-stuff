import random

def scaleArray(arr,newMin=0,newMax=1):
    scaledArray = []
#    print(arr)
    MIN = min(arr)
    MAX = max(arr)
    for n in arr:
        N = (newMax - newMin) * (n - MIN)/(MAX - MIN) + newMin
        scaledArray.append(N)
    return scaledArray

randomNumbers = []
for i in range(2000):
    n = random.gauss()
    randomNumbers.append(n)
    #print(n)
randomNumbers.sort()
#print(randomNumbers)
#print(scaleArray(randomNumbers,8,15))
print(int(random.gauss(3,2) + 1 ))
# 8 - 16 hours
# 8 * 60 min = 480min
