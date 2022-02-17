#Exam Tasks

#Paper1

import ctypes 


class Array:
    def __init__(self,size):
        self._size = size
        PyArrayType = ctypes.py_object*size
        self._elements = PyArrayType()
        self.clear(None)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        assert index>=0,"index subscripting out of range"
        return self._elements[index]

    def __setitem__(self,index,value):
        assert index>=0 and index < len(self) ,"index subscripting out of range"
        self._elements[index]=value

    def clear(self,value):
        for i in range(self._size):
            self._elements[i] = value

    def __iter__(self):
        return _ArrayIterator(self._elements)

class _ArrayIterator:
    def __init__(self, elements):
        self.elements = elements
        self.cur = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur<len(self.elements):
            value = self.elements[self.cur]
            self.cur = self.cur+1
            return value
        else:
            raise StopIteration

arr = Array(5)
arr[0] = 1
arr[1] = 3
arr[2] = 4
for i in arr:
    print(i)
        

def BinarySearch(nums,key):
    lefti = 0
    righti = len(nums)
    while righti >= lefti:
        middlei = (lefti+righti)//2
        if nums[middlei] == key:
            return middlei
        elif nums[middlei]>key:
            righti = middlei-1
        elif nums[middlei] < key:
            lefti = middlei+1
    
    return None

l1 = [1,2,3,4,5,6]
a = BinarySearch(l1,4)
print(a)


def BubbleSort(list1):
    for i in range(len(list1)-1):
        for j in range(0,len(list1)-i-1):
            if list1[j]> list1[j+1]:
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
    return list1
a= BubbleSort([2,3,1,5,4,6])
print(a)



        

        
