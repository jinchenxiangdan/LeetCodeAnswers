/**
Author: Shawn Jin

Runtime: 7 ms, faster than 96.49% of Java online submissions for Unique Email Addresses.
Memory Usage: 38 MB, less than 99.04% of Java online submissions for Unique Email Addresses.

*/
class LeetCode929 {
  public int numUniqueEmails(String[] emails) {
        Set<String> set = new HashSet<>();
        for (String email: emails) {
            set.add(getEmail(email));
        }
        return set.size();
    }
    
    
    public String getEmail(String inputEmail) {

        StringBuilder output = new StringBuilder();
        boolean inEnd = false, ignore = false;
        for (int i = 0; i < inputEmail.length(); i++) {
            char c = inputEmail.charAt(i);
            if (!inEnd) {
                if (c != '@' && ignore) {
                    continue;
                } else if (c == '+' ) {
                    ignore = true;
                } else if (c == '.') {
                    continue;
                } else if (c == '@') {
                    inEnd = true;
                    ignore = false;
                    output.append(c);
                } else {
                    output.append(c);
                }
            } else {
                output.append(c);
            }   
        }
        return output.toString();
    }
}
