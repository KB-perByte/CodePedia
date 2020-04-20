#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
    int T;
    cin>>T;
    while(T--){
        string str;
        cin>>str;
        string right, left;
        if(str.length()%2 == 0){
            right = str.substr(0,str.length()/2);
            left = str.substr(str.length()/2);
        }    
        else {
            right = str.substr(0,str.length()/2);
            left = str.substr((str.length()+1)/2);
        }
        sort(right.begin(),right.end());
        sort(left.begin(),left.end());
        if(right == left)
            cout<<"YES"<<endl;
        else
            cout<<"NO"<<endl;
    }
	return 0;
}
