'''
Oh no! Commander Lambda's latest experiment to improve the efficiency of her LAMBCHOP doomsday device has backfired spectacularly. She had been improving the structure of the ion flux converter tree, but something went terribly wrong and the flux chains exploded. Some of the ion flux converters survived the explosion intact, but others had their position labels blasted off. She's having her henchmen rebuild the ion flux converter tree by hand, but you think you can do it much more quickly - quickly enough, perhaps, to earn a promotion!

Flux chains require perfect binary trees, so Lambda's design arranged the ion flux converters to form one. To label them, she performed a post-order traversal of the tree of converters and labeled each converter with the order of that converter in the traversal, starting at 1. For example, a tree of 7 converters would look like the following:

#       7

#   3      6

# 1   2  4   5
Write a function answer(h, q) - where h is the height of the perfect tree of converters and q is a list of positive integers representing different flux converters - which returns a list of integers p where each element in p is the label of the converter that sits on top of the respective converter in q, or -1 if there is no such converter. For example, answer(3, [1, 4, 7]) would return the converters above the converters at indexes 1, 4, and 7 in a perfect binary tree of height 3, which is [3, 6, -1].

The domain of the integer h is 1 <= h <= 30, where h = 1 represents a perfect binary tree containing only the root, h = 2 represents a perfect binary tree with the root and two leaf nodes, h = 3 represents a perfect binary tree with the root, two internal nodes and four leaf nodes (like the example above), and so forth. The lists q and p contain at least one but no more than 10000 distinct integers, all of which will be between 1 and 2^h-1, inclusive.

The test cases provided are:

Inputs:

(int) h = 3
(int list) q = [7, 3, 5, 1]
Output:

(int list) [-1, 7, 6, 3]
Inputs:

(int) h = 5
(int list) q = [19, 14, 28]
Output:

(int list) [21, 15, 29]
I used a rather complex and dumb way to solve the problem. I created two lists, one recording every pair of children in the binary tree, the other one recording all the corresponding parents to these children in corresponding indexes. So my children list for the height 3 binary tree provided above would look like [[3, 6], [1, 2], [4, 5]], and the relevant part of my parent list would look like [7, 3, 6].

To find the parent of the elements given in array q, I just ran a loop to look for the element in the children list and, after finding it, record the corresponding parent since they have the same index.
'''
def myParent(h, _q):
    maxLeaf = (2**h)-1
    if maxLeaf <= _q:
        return -1
    
    else:
        tmp = 0
        flag = True 
        treeSz = maxLeaf
        ans = -1

        while flag:
            if treeSz == 0:
                flag = False
            treeSz = treeSz >> 1
            _left  = tmp + treeSz
            _right = _left + treeSz
            _node  = _right + 1

            if _left == _q or _right == _q:
                ans = _node
                flag = False
            
            elif _q > _left:
                tmp = _left
        return ans

def solution(h,q):
    ap = []
    for i in q:
        ap.append(myParent(h,i))
    print(ap)     

solution(5,[19,14,28])
            
