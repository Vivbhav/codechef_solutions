#include<stdio.h>
#include<math.h>
int main() {
	int t;
	scanf("%d",&t);
	int n, q, rem;
	double power;
	long int ans;
	int num1 = 0, num2 = 0;
	while(t--) {
		scanf("%d",&n);
		q = n / 26;
		rem = n - q * 26;
		power = pow((double)2, (double)q);
		ans = (long int)power;
		if(rem == 0) {
			ans /= 2;
			printf("%d %d %ld\n", num1, num2, ans);
		}
		if((rem > 0) && (rem <= 2))
			printf("%ld 0 0\n", ans);
		else if(rem <= 10) 
			printf("0 %ld 0\n", ans);
		else 
			printf("0 0 %ld\n", ans);
	}
}
