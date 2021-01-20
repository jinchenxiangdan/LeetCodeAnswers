class Leetcode819{
    public String mostCommonWord(String paragraph, String[] banned) {
        String res = "";
        int count = 0;
        Map<String, Integer> map = new HashMap<>();
        String temp = "";
        List<String >list = Arrays.asList(banned);
        for(int i = 0; i< paragraph.length(); i++){
            char flag = paragraph.charAt(i);
            if (Character.isLetter(flag) == true){
                temp +=  Character.isLowerCase(flag)  ? flag : Character.toLowerCase(flag)  ;
                 
      
                
            }  if(((Character.isLetter(flag) == false && Character.isLetter(paragraph.charAt(i-1))))|| i == paragraph.length() - 1){
            
          
                
                map.put(temp, map.getOrDefault(temp, 0) + 1);
                
                if(map.getOrDefault(temp, 0) > count && !list.contains(temp)){
                    count = map.getOrDefault(temp, 0);
                    res = temp;
                }
                
            temp = "" ;
                
            }
          
        }
        
        return res;

        
        
             
    }
        
        
}