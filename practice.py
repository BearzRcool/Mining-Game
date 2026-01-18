def FindFirstItem(target, list):
    if target in list:
        for i in range(len(list)):
            if target == list[i]:
                return i
            
    return -1

list = [1,3,7,6,7,3,5,6,1,2,3,5,23,23123,656,12,3,12,31,23,15,123,52,7,45,2,1,32,452,3,4,62,6753,47,345,6,345,62,34,13,543,63,78,468,4,576,4,56,2,24,51,435,2,73,8,635,65,348,1,324,15,23,5,21,34,100]
print (FindFirstItem(100, list))