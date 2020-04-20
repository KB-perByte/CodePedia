#include<bits/stdc++.h>
using namespace std;
int main()
{
  int t;
  scanf("%d",&t);
  while(t--)
  {
    int activity;long sum=0;
    scanf("%d",&activity);
    char type[20];
    scanf("%s",type);int i=0;
    for(i=0;i<activity;i++)
    {
      char s[20];
      scanf("%s",s);
      char ch=s[8];
      switch(ch)
      {
        case 'W':
        int rank;
        scanf("%d",&rank);
        sum+=300;
        if(rank<20)
        {
          sum+=(20-rank);
        }
        break;

        case 'D':
        int severity;
        scanf("%d",&severity);
        sum+=severity;
        break;

        case 'R':
        sum+=300;
        break;

        default:
        sum+=50;
      }
    }
    if(type[0]=='N')
    {
      printf("%d\n",(sum/400));
    }
    else
    {
      printf("%d\n",(sum/200));
    }

  }
  return 0;
}
