#include<stdio.h>
#include<stdlib.h>
int main() {
	int n, m;
	scanf("%d%d",&n, &m);
	int arr1[n][2], arr2[m][2];
	int i;
	for(i = 0 ; i < n ; i++) {
		scanf("%d",&arr1[i][0])
		arr1[i][1] = i;	
	}
	for(i = 0 ; i < m ; i++) {
		scanf("%d",&arr2[i])
		arr2[i][1] = i;
	}
	
	
}
