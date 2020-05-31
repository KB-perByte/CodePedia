#include<bits/stdc++.h>
using namespace std;
bool isValid(vector<vector<int>> &arr,int i,int j,vector<vector<bool>> &visited)
{
    if(i>=0 && j>=0 && i<arr.size() && j<arr.size()) //inside array
    {
        if(arr[i][j]==1)    //valid
        {
            if(visited[i][j]==0) 
            {
                return true;
            }
        }
    }
    return false;
}
void maze(vector<vector<int>> &arr,int i,int j,string temp,vector<vector<bool>> &visited)
{
    if(i== arr.size()-1 && j == arr.size()-1)
    {
        cout<<temp<<" ";
        return;
    }
    visited[i][j]=true;
    if(isValid(arr,i+1,j,visited))
        maze(arr,i+1,j,temp+"D",visited);
    if(isValid(arr,i,j+1,visited))
        maze(arr,i,j+1,temp+"R",visited);
    if(isValid(arr,i-1,j,visited))
        maze(arr,i-1,j,temp+"U",visited);
    if(isValid(arr,i,j-1,visited))
        maze(arr,i,j-1,temp+"L",visited);
    visited[i][j]=false;
}
int main() {
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        vector<vector<int> > arr( n , vector<int> (n));
        vector<vector<bool> > visited( n , vector<bool> (n, false)); 
        for(int i=0;i<n;i++)
        {  
            for(int j=0;j<n;j++)
            {
               cin>>arr[i][j];  
            }
        }
        maze(arr,0,0,"",visited);
        cout<<endl;
    }
    return 0;
}