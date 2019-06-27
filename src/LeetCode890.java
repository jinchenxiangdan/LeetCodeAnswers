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
    
    
    /**
    Author:  Github user: narendrakumar
    Runtime: 1 ms, faster than 96.35% of Java online submissions for Find and Replace Pattern.
    Memory Usage: 36.3 MB, less than 98.70% of Java online submissions for Find and Replace Pattern.
    */
    private boolean util(String a, String b) {
        HashMap<Character, Integer> map1 = new HashMap<>();
        HashMap<Character, Integer> map2 = new HashMap<>();
        for(int i=0; i<a.length(); i++) {
            if(map1.put(a.charAt(i), i) != map2.put(b.charAt(i), i)) return false;    
        }
        return true;
    }
    
    public List<String> findAndReplacePattern(String[] words, String pattern) {
        List<String> result = new ArrayList<>();
        for(String word: words) {
            if(word.length() != pattern.length()) continue;
            if(util(pattern,word)){
                result.add(word);
            }
        }
        return result;
    }

}
