#include <stdio.h>

int main(void)
{
	int a,sum=0,b,x,t;
	scanf("%d", &a);
	t = a;
	while (a > 0) {
		scanf("%d", &b);
		sum += b;
		a--;
	}
	
	x = sum - t+ 1;
	printf("%d", x);
}