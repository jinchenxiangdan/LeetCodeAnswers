/**

Runtime: 0 ms, faster than 100.00% of Java online submissions for N-Repeated Element in Size 2N Array.
Memory Usage: 38.1 MB, less than 99.68% of Java online submissions for N-Repeated Element in Size 2N Array.
*/
class LeetCode961{
    public int repeatedNTimes(int[] A) {
        // precondition: unique elements and range is [0, 10000]
        int[] count = new int[10000];
        for (int a : A)
            if (count[a]++ == 1)
                return a;
        return -1;
        
    }
}
