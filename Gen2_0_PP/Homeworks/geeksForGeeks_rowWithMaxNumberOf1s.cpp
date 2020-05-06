int rowWithMax1s(bool mat[R][C]) 
{ 
    int max_row_index = 0; 
    int j = first(mat[0], 0, C-1); 
    if (j == -1) 
        j = C - 1; 
    for (int i = 1; i < R; i++) 
    {
        while (j >= 0 && mat[i][j] == 1) 
        { 
            j = j-1;  
            max_row_index = i; 
        } 
    } 
    return max_row_index; 
} 

int first(bool arr[], int low, int high)  
{  
    if(high >= low)  
    {  
        int mid = low + (high - low)/2;  
        if ( ( mid == 0 || arr[mid-1] == 0) && arr[mid] == 1)  
            return mid;  
        else if (arr[mid] == 0)  
            return first(arr, (mid + 1), high);    
        else
            return first(arr, low, (mid -1));  
    }  
    return -1;  
}  

int main()  
{  
    bool mat[R][C] = { {0, 0, 0, 1},  
                    {0, 1, 1, 1},  
                    {1, 1, 1, 1},  
                    {0, 0, 0, 0}};  

    cout << "Index of row with maximum 1s is " << rowWithMax1s(mat);  

    return 0;  
}  

