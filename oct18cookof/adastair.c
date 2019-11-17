#include<stdio.h>
int main() {
	int t;
	scanf("%d",&t);
	int n, k;
	int arr[128];
	int i;
	int count;
	while(t--) {
		count = 0;
		scanf("%d%d",&n, &k);
		for(i = 0 ; i < n ; i++) {
			scanf("%d",&arr[i]);
		}
		count += arr[0] / k;
		for(i = 1 ; i < n ; i++) {
			count += (arr[i] - arr[i - 1]) / k;
		}	
		printf("%d\n",count);
	}
}
