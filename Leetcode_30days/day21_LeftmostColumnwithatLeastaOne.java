/**
 * // This is the BinaryMatrix's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface BinaryMatrix {
 *     public int get(int x, int y) {}
 *     public List<Integer> dimensions {}
 * };
 */

class Solution {
    public int leftMostColumnWithOne(BinaryMatrix binaryMatrix) {
        List<Integer> dimension=binaryMatrix.dimensions();
        int n=dimension.get(0);
        int m=dimension.get(1);
       
        int i=0,j=m-1,leftMostOne=-1;
        
        while(i<n && j>=0)
        {
            int result=binaryMatrix.get(i,j);
            if(result==0)
              i++;
            else{
                leftMostOne=j;
                j--;
             }
        } 
        return leftMostOne;
    }
}