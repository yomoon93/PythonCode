lstArr = [2, 3, 4, 24, 11, 8]
def _move_(lst):
    a=lst.pop()
    lst.insert(0,a)
    return lst
print(_move_(lstArr))

# lstArr = [2, 3, 4, 24, 11, 8]
# a = lstArr.pop(-1)
# print(a)
# lstArr.insert(0,a)
# print(lstArr)
def randomMake(arr,*i):


