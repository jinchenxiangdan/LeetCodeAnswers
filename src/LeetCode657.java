class LeetCode657 {
    /**
    Author: Shawn Jin
    Runtime: 7 ms, faster than 68.17% of Java online submissions for Robot Return to Origin.
    Memory Usage: 37.7 MB, less than 99.56% of Java online submissions for Robot Return to Origin.
    */
    public boolean judgeCircle(String moves) {
        int x = 0, y = 0;
        for (int i = 0; i < moves.length(); i++) {
            switch(moves.charAt(i)) {
                case 'U':
                    y++;
                    break;
                case 'D':
                    y--;
                    break;
                case 'L':
                    x--;
                    break;
                case 'R':
                    x++;
                    break;
            }
            
        }
        return (x == 0 && y == 0);
    }
}
