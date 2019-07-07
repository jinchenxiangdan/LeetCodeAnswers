class LeetCode728 {
    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> list = new ArrayList<>();
        for (int i = left; i <= right; i++) {
            if (checkNumber(i)) {
                list.add(i);
            }
        }
        return list;
    }
    /**
     * A better way
     * after convert to int, the just % 10 each time (in this way, we can only get the last digit)
     *
     */
    private boolean checkNumber(int num) {

        int cur = num;
        while (cur != 0) {
            int digit = cur % 10;
            if (digit == 0 || num % digit != 0) {
                return false;
            }
            cur /= 10;
        }
        return true;
    }

    /**
     * Normal thought solution. 
     * Used ASCII table to convert char, then do the math and check
     * Runtime: 2 ms, faster than 70.57% of Java online submissions for Self Dividing Numbers.
     * Memory Usage: 35.4 MB, less than 5.03% of Java online submissions for Self Dividing Numbers.
     */
    /**
    private boolean checkNumber(int num) {
        String stringInfo = String.valueOf(input);
        
        for (int i = 0; i < stringInfo.length(); i++) {
            int val = (int)stringInfo.charAt(i) - 48;
            if (val == 0) return false;
            if (input % val != 0) {
                return false;
            }
        }
        return true;
    }
    */
}
