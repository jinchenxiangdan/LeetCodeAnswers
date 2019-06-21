class LeetCode4 {

    /**
    Author: Shawn Jin (normal solution)
    
    Runtime: 3 ms, faster than 50.17% of Java online submissions for Median of Two Sorted Arrays.
    Memory Usage: 46.8 MB, less than 90.80% of Java online submissions for Median of Two Sorted Arrays.
    */
    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] answer = new int[nums1.length + nums2.length];
        // int length = nums1.length < nums2.length ? nums1.length : nums2.length;
        int nums1Pos = 0, nums2Pos = 0;
        for (int i = 0; i < nums1.length+nums2.length; i++) {
            if (nums1Pos >= nums1.length) {
                answer[i] = nums2[nums2Pos];
                nums2Pos++;
            } else if (nums2Pos >= nums2.length) {
                answer[i] = nums1[nums1Pos];
                nums1Pos++;
            } else {
                // nums1Pos and nums2Pos are all in range
                if (nums1[nums1Pos] < nums2[nums2Pos]) {
                    answer[i] = nums1[nums1Pos];
                    nums1Pos++;
                } else {
                    answer[i] = nums2[nums2Pos];
                    nums2Pos++;

                }
            }       
        }
        // find median

        // if even number 
        if ((nums1.length+nums2.length) % 2 == 0) {
            return (answer[answer.length/2-1] + answer[answer.length/2])/2.0;
        } else {
            // if odd number 
            return (double)answer[answer.length/2];
        }
    }

}
