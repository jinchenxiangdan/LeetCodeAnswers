class Leetcode48 {
    public void rotate(int[][] matrix) {
     
    	//这道题想法就是两次对称  第一次沿 左右对称 第二次再以右上到左下的对角线对称
    	
    	//第一次循环 左右对称换位置 注意不要循环全部 否则刚换好的 又换回去了 所以循环对换一般即可
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j <= (matrix[i].length -1) / 2 ; j++){
                int temp = matrix[i][j]; 
                matrix[i][j] = matrix[i][matrix[i].length - j - 1];
                matrix[i][matrix[i].length - j - 1] = temp;
                
            } 
        }
        
        

        //第二次同理 对角线 对换 注意对换位置循环 每层都是 length - j - 1的 不然会换回去
        for(int i = 0; i <= matrix.length - 1 ; i++){
            for(int j = 0; j <= matrix[i].length - 1 - i ; j++){
                int temp = matrix[i][j]; 
                matrix[i][j] = matrix[matrix.length - j - 1][matrix[i].length - i - 1];
                matrix[matrix.length - j - 1][matrix[i].length - i - 1] = temp;
                
            }
        }
      
    }
}