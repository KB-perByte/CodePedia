#include<iostream>
#include<cstdio>
#include<algorithm>
#include<iomanip>
#include<cstring>
#include<string>
#include<cmath>
#include<stack>
#include<queue>
#include<vector>
#include<set>
#include<map>
#define ll long long
#define mes(x,y) memset(x,y,sizeof(x))
#define maxn 2147483648+30
using namespace std;
int main(){
	 std::ios::sync_with_stdio(false);
	 ll x,y,i,j,k,a,b,v[100030];
	 while(cin>>x){
	 	a=0;b=0;
	 	for(i=0;i<x;i++){
	 		cin>>v[i];
	 		if(v[i]%2==0)a++;
	 		else b++;
		 }
		 if(a!=0&&b!=0){
		 	sort(v,v+x);
		 }
		  for(i=0;i<x;i++)cout<<v[i]<<" ";cout<<endl;
	 }
}
