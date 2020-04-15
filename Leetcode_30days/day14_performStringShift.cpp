/*

You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift). 
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.
Return the final string after all operations.

*/


class Solution {
public:
    string stringShift(string s, vector<vector<int>>& shift) {
        int finalShift =0;
        
        for(int i=0;i<shift.size(); i++){
            int direction = shift[i][0];
            int amount = shift[i][1];
            if(direction == 0)
                finalShift -=amount;
            else
                finalShift +=amount;
        }
        string front, back;
        if(finalShift<0){
            finalShift = abs(finalShift)%s.size();
            front = s.substr(finalShift);
            back = s.substr(0,finalShift);
        }   
        else if(finalShift>0){
            finalShift = finalShift% s.size();
            front = s.substr(s.size()- finalShift, finalShift);
            back = s.substr(0, s.size()- finalShift);
        }
        else return s;
        return front + back;
    }
};