import java.util.HashMap;
import java.util.Map;

public class LeetCode657 {

    private static Map<String, Integer> directionCount = new HashMap<>();

    public static void main(String[] arg){
        System.out.println(judgeCircle("LL"));
        System.out.println(judgeCircle("UD"));
    }

    private static boolean judgeCircle(String moves) {
        directionCount.put("up&down", 0);
        directionCount.put("left&right", 0);

        for (int i = 0; i < moves.length(); i++){
            switch (moves.charAt(i)){

                case 'U':
                    directionCount.put("up&down",directionCount.get("up&down")+1);
                    break;
                case 'D':
                    directionCount.put("up&down",directionCount.get("up&down")-1);
                    break;
                case 'L':
                    directionCount.put("left&right",directionCount.get("left&right")+1);
                    break;
                case 'R':
                    directionCount.put("left&right",directionCount.get("left&right")-1);
                    break;
                default:
                    // This part is just for format.
                    continue;
            }
        }
        return directionCount.get("up&down") == 0 && directionCount.get("left&right") == 0;
    }


}
