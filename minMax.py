def getMin(mylist, i, minVal):
  if i < len(mylist):
    if minVal > mylist[i]:
      return getMin(mylist, i+1, mylist[i])
    else:
      return getMin(mylist, i+1, minVal)
  else:
    return minVal
  
def getMax(mylist, i, maxVal):
  if i < len(mylist):
    if maxVal < mylist[i]:
      return getMax(mylist, i+1, mylist[i])
    else:
      return getMax(mylist, i+1, maxVal)
  else:
    return maxVal
  
mylist = [21, 7, 40, 29, 11, 5, 90, 78, 64, 15, 88]
maxVal = getMax(mylist, 0, 0)
minVal = getMin(mylist, 0, maxVal)
print(mylist)
print("최소값:",minVal,", 최대값:", maxVal)