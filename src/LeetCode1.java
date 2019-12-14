/**
 * Author: Shawn Jin
 * The input is not ascending
 */
class LeetCode1 {
	// 
	public static int[] twoSum(int[] nums, int target) {
        // used the way like insertion sort. 
        for (int i = 0; i < nums.length-1; i++) {
            for (int j = i+1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[] {i,j};
                }
            }
        }
        throw new IllegalArgumentException();
	}





	public static void main(String[] args) {
		int[] li = new int[]{3,2,4};
		printList(twoSum(li, 6));

	}

	private static void printList(int[] input) {
		for (int i = 0; i < input.length; i++) {
			System.out.print(input[i]);	
		}
		
	}

}
