class Leetcode29{
    public int divide(int dividend, int divisor) {
        boolean isNeg = false;


        
        if (dividend == Integer.MAX_VALUE && divisor == -1) return Integer.MIN_VALUE;
        if (dividend == Integer.MIN_VALUE && divisor == -1) return  Integer.MAX_VALUE;
        if(divisor == 1) return dividend; 
        if(divisor == -1) return - dividend;
        
        if((dividend < 0 && divisor > 0) || (dividend >  0 && divisor < 0) ) isNeg = true;
        int count = 0;
        long dividend1 = Math.abs((long)dividend);
        long divisor1 = Math.abs((long)divisor);
        while(dividend1 > 0){
            if(dividend1 < divisor1) break;
            dividend1 -= divisor1;
            count ++;
        }
         
        return isNeg == true ? -count : count;
    }
}