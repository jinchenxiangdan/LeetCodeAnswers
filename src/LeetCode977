/**
This is optimal answer I know, this is the answer of LeetCode user: wangzi6147

Runtime: 1 ms, faster than 100.00% of Java online submissions for Squares of a Sorted Array.
Memory Usage: 40.8 MB, less than 97.10% of Java online submissions for Squares of a Sorted Array.
*/
class LeetCode977 {
    public int[] sortedSquares(int[] A) {
        int n = A.length;
        int[] result = new int[n];
        int i = 0, j = n - 1;
        for (int p = n - 1; p >= 0; p--) {
            if (Math.abs(A[i]) > Math.abs(A[j])) {
                result[p] = A[i] * A[i];
                i++;
            } else {
                result[p] = A[j] * A[j];
                j--;
            }
        }
        return result;
    }
}
