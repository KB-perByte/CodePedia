#include <cstdio>
#include <vector>

int main(){
    //printf("Enter the no of thiefs, and location of police: ");
    int n, a; scanf("%d %d\n", &n, &a);
    std::vector<int> v(n + 1);
    for(int i = 1; i <= n; i++){scanf("%d ", &v[i]);}

    int ans(v[a]);
    for(int i = 1; i <= n; i++){
        if(a - i < 1  && a + i > n){break;}
        else if(a - i >= 1 && a + i <= n && v[a - i] == v[a + i]){ans += 2 * v[a - i];}
        else if(a - i >= 1 && a + i > n){ans += v[a - i];}
        else if(a - i < 1  && a + i <= n){ans += v[a + i];}
    }

    printf("%d\n", ans);

    return 0;
}