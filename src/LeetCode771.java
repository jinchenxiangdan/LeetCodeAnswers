public class LeetCode771 {

    private static int NUM_JEW = 0;
    public static void main(String[] arg){
// case 1:
        String J = "aA";
        String S = "aAAbbbb";
// case 2:
        String test2 = "z";
        String test3 = "ZZ";

        System.out.println(numJewelsInStones(test2, test3));
    }

    //  the first answer
    private static int numJewelsInStones(String J, String S) {

        for (int i = 0; i < J.length(); i++){
            char jew = J.charAt(i);

            for (int j =0; j < S.length(); j++){
                char myJew = S.charAt(j);
                if (jew == myJew){
                    NUM_JEW++;
                }
            }
        }
        return NUM_JEW;
    }


}
