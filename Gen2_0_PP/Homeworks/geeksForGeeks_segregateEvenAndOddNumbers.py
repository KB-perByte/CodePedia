#code
#quick sort
def sortEvnOdd(arr, n) :  
    
    j = -1
    for i in range(0, n) : 
        if (arr[i] % 2 == 0) : 
            j = j + 1
            temp = arr[i] 
            arr[i] = arr[j] 
            arr[j] = temp 

inp = int(input())            
while(inp):
    inp-=1
    n = int(input())
    arr = list(map(int,input().split()))
    sortEvnOdd(arr,n)
    print(arr)

# 12 10 9 45 2 10 10 45
[12, 34, 45, 9, 8 90 3 

'''
using namespace std;
int main(){
	int t; cin >> t;
	while(t--){
		int n; cin >> n;
		vector <int> arr(n);
		for(auto &i : arr) cin >> i;

		int l = 0, h = n - 1;
		while(l<=h){
			while(l<=n-1 && !(arr[l]&1))l++;
			while(h>=0 && (arr[h]&1)) h--;	
			if(l<h) swap(arr[l],arr[h]);
		}
		
		sort(arr.begin(),arr.begin()+h+1);
		sort(arr.begin()+h+1,arr.end());
		for(auto i: arr) cout << i << " ";
		cout<<endl;
	}
}
'''


# A Lomuto partition based scheme to 
# segregate even and odd numbers. 

# function to rearrange the 
# array in given way. 
def rearrangeEvenAndOdd(arr, n) : 
	j = -1

	for i in range(0, n) : 
		if (arr[i] % 2 == 0) : 
			j = j + 1

			temp = arr[i] 
			arr[i] = arr[j] 
			arr[j] = temp 

inp = int(input())            
while(inp):
    inp-=1
    n = int(input())
    arr = list(map(int,input().split()))
    rearrangeEvenAndOdd(arr,n)
    print(arr)
