public class LeetCode461 {
    public static void main(String[] arg){
        change2BinaryDigits(73);
//        Math.abs()
        System.out.println(1^4);
    }

    // the easiest method
    private static int hammingDistance(int x, int y){
        if ((x ^ y) == 0){
            return 0;
        }
        // number / 2 is to remove the lowest number in binary number (same rules in decimal base)
        return (x ^y) % 2 + hammingDistance(x/2, y/2);
    }

    // this method could change the 10-dig number to binary digits
    private static void change2BinaryDigits(int number){
        assert number >= 0;
        String answer = "";
        if (number != 0){
            while (!(number / 2 == 0)){

                answer += number % 2;
                number = number / 2;
            }
            answer += number%2;     // this item should always be 1
        }
//        answer += "1";
        StringBuilder reversed = new StringBuilder();
        reversed.append(answer);

        System.out.println(reversed.reverse().length());
//        reversed.length();

    }
}
