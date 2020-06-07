#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<list>
#include<queue>
#include<cmath>
#include<vector>
using namespace std;
char oper[5];
long long num[5],ans=1000000000000000ll;
long long calu(long long a,long long b,char o){
	if(o=='+')return a+b;
	if(o=='*')return a*b;
}
int main()
{
	scanf("%lld%lld%lld%lld",&num[0],&num[1],&num[2],&num[3]);
	getchar();
	scanf("%c %c %c",&oper[0],&oper[1],&oper[2]);
	int id[5];id[0]=0;id[1]=1;id[2]=2;id[3]=3;
	do
	{
		long long a=calu(num[id[0]],num[id[1]],oper[0]);
		long long b=calu(a,num[id[2]],oper[1]);
		long long temp=calu(b,num[id[3]],oper[2]);
		a=calu(num[id[0]],num[id[1]],oper[0]);
		b=calu(num[id[2]],num[id[3]],oper[1]);
		long long temp1=calu(a,b,oper[2]);
		ans=min(ans,min(temp,temp1));
	}while(next_permutation(id,id+4));
	printf("%lld\n",ans);
	return 0;
}
