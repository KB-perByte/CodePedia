
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

typedef vector<int> vec;
typedef long long ll;
typedef vector<ll> vel;

int main() {
	int t;
	cin >> t;
	while (t--) {
		int num;
		cin >> num;
		vel a(num + 1, 0);
		vec s(num);
		vec e(num);
		for (int i = 0; i < num; i++) {
			cin >> a[i + 1];
			a[i + 1] += a[i];
		}
		for (int i = 1; i <= num; i++) {
			int v = a[i] - a[i - 1];
			s[i-1] = lower_bound(a.begin(), a.end(), a[i - 1] - v) - a.begin() - 1;
			e[i-1] = upper_bound(a.begin(), a.end(), a[i] + v) - a.begin();
		}
		sort(s.begin(), s.end());
		sort(e.begin(), e.end());
		int c = 0;
		int i = 0;
		int j = 0;
		while (i < num && s[i] <= 0) {
			c++;
			i++;
		}
		for (int k = 0; k < num; k++) {
			while (i < num && s[i] == k) { c++; i++; }
			while (j < num && e[j] == k) { c--; j++; }
			cout << c - 1;
			if (k < num - 1) cout << " ";
		}
		cout << endl;
	}
}