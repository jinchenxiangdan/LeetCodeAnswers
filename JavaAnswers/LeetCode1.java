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

	/**
	 * This method is the best solution, running in O(n) times
	 * @param  nums   [description]
	 * @param  target [description]
	 * @return        [description]
	 */
	public static int[] twoSum2(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }
        for (int i = 0; i < nums.length; i++) {
            int difference = target - nums[i];
            if (map.containsKey(difference) && map.get(difference) != i) {
                return new int[] { i, map.get(difference)};
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
