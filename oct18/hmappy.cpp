#include <iostream>
#include <array>
#include <algorithm>
#include <iterator>
using namespace std;
int main() {
	int n, m;
	cin >> n >> m;
	//int a[n], b[n], c[n];
	//int a[n][4];
	array<int, 2> a[2] = {;
	int i;
	for(i = 0 ; i < n ; i++) 
		cin >> a[i][0];
	for(i = 0 ; i < n ; i++) 
		cin >> a[i][1];
		a[i][2] = a[i][0] * a[i][1];
	sort(a, a + n);
	for(i = 0 ; i < n ; i++) {
		cout << a[i][0] << "\t" << a[i][1] << "\t" << a[i][2] << "\n";
	} 	
}
