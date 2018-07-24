public class LeetCode832 {
//    private int[][] test1 = new int[][]([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]);
    public static void main(String[] arg){
        System.out.println(5/2);

    }

    private int[][] flipAndInvertImage(int[][] A){
        for (int i = 0; i < A.length; i++){
            A[i] = flipImage(A[i]);
        }
        return invertImage(A);
    }

    private int[] flipImage(int[] image){
        int backLocation = 1;
        for (int i = 0; i < image.length/2; i++){
            int temp = image[image.length-backLocation];

            image[image.length-backLocation++] = image[i];
            image[i] = temp;
        }

        return image;
    }

    private int[][] invertImage(int[][] b){
        for (int i = 0; i < b.length; i++){
            for (int j =0; j < b[i].length; j++){
                if (b[i][j] == 0){
                    b[i][j] = 1;
                } else {
                    b[i][j] = 0;
                }
            }
        }
        return b;
    }
}
