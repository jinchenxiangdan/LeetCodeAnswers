/**
Runtime: 1 ms, faster than 100.00% of Java online submissions for Sort Array By Parity.
Memory Usage: 39.4 MB, less than 96.27% of Java online submissions for Sort Array By Parity.
*/
class LeetCode905 {
    public int[] sortArrayByParity(int[] A) {
    int[] answer = new int[A.length];
    int e = 0, o = A.length-1;
    for (int i = 0; i < A.length; i++) {
        // if even numbers 
        if (A[i] % 2 == 0) {
            answer[e] = A[i];
            e++;
        } else {    // odd numbers
            answer[o] = A[i];
            o--;
        }
    }
    return answer;
    }
}
