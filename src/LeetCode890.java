class LeetCode890 {

    /**
    Author: Shawn Jin
    Runtime: 2 ms, faster than 84.51% of Java online submissions for Find and Replace Pattern.
    Memory Usage: 36.1 MB, less than 98.77% of Java online submissions for Find and Replace Pattern.
    */
    public List<String> findAndReplacePattern(String[] words, String pattern) {
        int[] patternInfo = convertString(pattern);
        List<String> answer = new LinkedList<>();
        for (String word: words) {
            if (Arrays.equals(patternInfo, convertString(word))){
                answer.add(word);
            }
        }
        return answer;
    }
    
    private int[] convertString(String input) {
        Map<Character, Integer> map = new HashMap<>();
        int[] info = new int[input.length()];
        
        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            map.putIfAbsent(c, map.size());
            info[i] = map.get(c);
        }
        
        return info;
    }
}
