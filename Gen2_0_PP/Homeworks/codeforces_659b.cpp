#include <bits/stdc++.h>
using namespace std;

const int maxn = 1e5 + 5;

struct Node{
    string s;
    int sc;
    };
    
Node node[maxn];
int num[maxn];

vector<Node>v[maxn];

bool comparator(Node start, Node end)
{
    return start.sc > end.sc;
}

int main(void)
{
    int n, m;
    cin>>n>>m;
    string s;
    int id, score;
    for(int i = 0; i <n; i++){
        cin>>s>>id>>score;
        node[i] = (Node){s, score};
        v[id].push_back(node[i]);
        num[id]++;
    }
    for(int i = 1; i <= m; i++){
        sort(v[i].begin(), v[i].end(), comparator);
        if(v[i].size() > 2 && v[i][2].sc == v[i][1].sc) cout<<"?"<<endl;
        else cout<<v[i][0].s<<' '<<v[i][1].s<<endl;
    }
    return 0;
}