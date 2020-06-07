#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <iostream>
#include<queue>
using namespace std; 
 
int vis[100005];
int main()
{ 
	int i,j;
	int n;
	int x,y;
	cin>>n;
memset(vis,-1,sizeof(vis));
 for (i=1;i<=n;i++)
 {
	 int ans=0;
	 scanf("%d%d",&x,&y);
	 int len=sqrt((double)x);
	 for (j=1;j<=len;j++)
	 {
		if (x%j) continue;
		if (i-y>vis[j])  ans++; 
		  vis[j]=i;
		if (j*j==x) continue;
		if (i-y>vis[x/j]) ans++;
		vis[x/j]=i;
	 }
	 printf("%d\n",ans); 
 }
	return 0;
	
} 

