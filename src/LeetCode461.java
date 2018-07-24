public class LeetCode461 {
    public static void main(String[] arg){
        change2BinaryDigits(10);
    }

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

        System.out.println(reversed.reverse());

    }
}
