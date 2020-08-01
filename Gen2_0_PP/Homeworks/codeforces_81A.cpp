#include <iostream>
#include <string>
#include <stack>
using namespace std;
 
 
int main()
{
    string s;
    cin>>s;
    stack<char> sta;
    for(int i=0;i<s.length();i++)
    {
        if(sta.empty())
        {
            sta.push(s.at(i));
            continue;
        }
        char ch = sta.top();
        if(s.at(i)!=ch)
        {
            sta.push(s.at(i));
        }else
        {
            sta.pop();
        }
    }
    stack<char> sta1;
    while(!sta.empty())
    {
        sta1.push(sta.top());
        sta.pop();
    }
    while(!sta1.empty())
    {
        cout<<sta1.top();
        sta1.pop();
    }
 
    return 0;
}
