
a = 34 
b = 34


print (id(a), id(b))


[[1,2,3],
 [4,5,6],
 [7,8,9]]



'''
arr = [1,2,5,3,4]

def get_i(idx):
    global arr
    return arr[idx]

def length():
    global arr
    return len(arr)

print(get_i(4))

print(length())






class Solution:
    def findInMountainArray(self, target, mountain_arr):
        #print(target)
        #print(mountain_arr.length())
        return self.binary_search(mountain_arr, target)
         
    def peak_search(self, array):
        start_index = 0
        for x in range(array.length()): 
            end_index = array.length() - 1
        
        while start_index <= end_index:
            mid_index = (start_index + end_index)//2 
            
            mid_element = array.get[mid_index]
            start_element = array[start_index]
            end_element = array[end_index]
            #print("here2", array[mid_index+1])
            if (mid_element > array[mid_index-1]) and (mid_element > array[mid_index+1]):
                return mid_element
            elif (mid_element < array[mid_index+1]) and (mid_element > array[mid_index-1]):
                start_index=mid_index+1
            #elif (mid_element > array[mid_index+1]) and (mid_element < array[mid_index-1]):
            elif mid_element < array[mid_index-1]:
                end_index = mid_index - 1
            
        return False

    def bsearch(self, start,end,array,target):
        start_index = start
        end_index =end
        
        while start_index <= end_index:
            mid_index = (start_index + end_index)//2 
            
            mid_element = array[mid_index]
            start_element = array[start_index]
            end_element = array[end_index]
            
            if target < mid_element:
                end_index = mid_index - 1
            elif target > mid_element:
                start_index = mid_index + 1
            else:
                target = mid_element
                return True,mid_index
            
        return False,False

    def binary_search(self, array,target):
        peakelem = self.peak_search(array)
        peakelemind= array.index(peakelem)
        end_index = len(array) - 1
        search,index = self.bsearch(0,peakelemind,array,target)
        if search == False:
            search,index =  self.bsearch(peakelemind,end_index,array,target)
            if search == True:
                return index
            else:
                return -1
        else:
            return index


ss = Solution()
print(ss.findInMountainArray(3, [0,1,2,4,2,1]))

'''