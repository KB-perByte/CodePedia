class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        return sorted(arr1, key=lambda ele: (ele not in arr2, arr2.index(ele) if ele in arr2 else ele))
