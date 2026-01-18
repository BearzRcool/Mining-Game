def FindFirstItem(target, list):
    if target in list:
        for i in range(len(list)):
            if target == list[i]:
                return i
            
    return -1
# list = [1,3,7,6,7,3,5,6,1,2,3,5,23,23123,656,12,3,12,31,23,15,123,52,7,45,2,1,32,452,3,4,62,6753,47,345,6,345,62,34,13,543,63,78,468,4,576,4,56,2,24,51,435,2,73,8,635,65,348,1,324,15,23,5,21,34,100]
# print (FindFirstItem(100, list))

list = [None,None,None,None,None,None,None,None,None,None]
list2 = [[],[],[],[],[],[],[],[],[],[]]
def HashFunction(item):
    char_sum = 0
    char_sum2 = 0
    for i in item:
        char_sum += ord(i)
    return char_sum%10
def AddTo(item,list):
    index = HashFunction(item)
    list[index].append(item)
AddTo("bob",list2)
AddTo("obb", list2)
print(HashFunction("bob"))
list3 = list2[HashFunction("bob")]
for i in range(len(list3)):
    if list3[i] == "bob":
        print (i)
print(list2)
'''
^ checking is O(n)
hash funciton is O(1) (faster)
print(ord("")) tells the unicode of a symbol, can use for hash function
hash functions can also be used w/ dicitonaries
hash f take an item from a list or dict and find its unicode value

ord("a") = 97

'''