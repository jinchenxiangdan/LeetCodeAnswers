
public class Leetcode50 {

	
	//m^n = m^(n/2)* m^(n/2)（偶数情况） 如果 n是单数 那就是 m ^ (n/2) * m ^(n/2) * m   递归乘下去 直到n是1的时候返回m的结果
	
	public double myPow(double x, int n) {
		if (n >= 0)
			return helper(x, n);
		else
			return 1 / helper(x, -n);

	}

	double helper(double x, int n) {
		if (n == 0)
			return 1.0;
		else if (n == 1)
			return x;

		double y = helper(x, n / 2);
		if (n % 2 == 0)
			return y * y;
		else
			return y * y * x;

	}
}
