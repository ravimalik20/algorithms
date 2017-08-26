#include<stdio.h>
#include<stdint.h>
#include<math.h>

uint64_t mul(uint64_t x, uint64_t y, uint64_t n);
uint64_t numDigits(uint64_t x);

uint64_t main()
{
	uint64_t x=1234, y=5678, n=numDigits(x);

	printf("%ld %ld\n", x*y, mul(x, y, n));
}

uint64_t mul(uint64_t x, uint64_t y, uint64_t n)
{
	if (x/100 == 0 && y/100 == 0)
		return x*y;

	uint64_t a, b, c, d, ac, bd, ad_bc;

	a = x / (uint64_t)pow(10, n/2);
	b = x % (uint64_t)pow(10, n/2);
	c = y / (uint64_t)pow(10, n/2);
	d = y % (uint64_t)pow(10, n/2);

	ac = mul(a, c, n/2);
	bd = mul(b, d, n/2);
	ad_bc = (mul(a+b, c+d, n/2)) - ac - bd;

	return pow(10, n) * ac + pow(10, n/2) * ad_bc + bd;
}

uint64_t numDigits(uint64_t x)
{
	uint64_t count = 0;

	while (x = x/10)
		count++;

	return count+1;
}
