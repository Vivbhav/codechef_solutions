#include<stdio.h>
int main() {
	int t;
	scanf("%d",&t);
	long int p1, p2, k;
	long int total;
	long int q, rem;
	while(t--) {
		scanf("%ld%ld%ld", &p1, &p2, &k);
		total = p1 + p2;
		q = total / (2 * k);
		rem = total - q * 2 * k;
		if(rem >= 0 && rem <= k - 1) 
			printf("CHEF\n");
		else 
			printf("COOK\n");
	}
}
