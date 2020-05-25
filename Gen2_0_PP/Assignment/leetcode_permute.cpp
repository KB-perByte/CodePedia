class Solution {
public:
    
    static void rev(vector<int> &nums,int i,int j){
        while(i < j){
            swap(nums[i],nums[j]);
            i++;j--;
        }
    }
    
    static void LR(vector<int> &nums,int i,int j){
        rev(nums,i,j-1);
        rev(nums,i,j);
    }
    
    static void RR(vector<int> &nums,int i,int j){
        rev(nums,i+1,j);
        rev(nums,i,j);
    }
    
    static void func(vector<int>& nums,int i,vector<vector<int> > &ans){
        if(i == nums.size()-1){
            ans.push_back(nums);
        }
        
        for(int j = i; j < nums.size(); j++){
            LR(nums,i,j);
            func(nums,i+1,ans);
            RR(nums,i,j);
            
        }
    }
    
    vector<vector<int>> permute(vector<int>& nums) {
        
        vector<vector<int> > ans;
        //vector<int> temp;
        func(nums,0,ans);
        return ans;
        
    }
};