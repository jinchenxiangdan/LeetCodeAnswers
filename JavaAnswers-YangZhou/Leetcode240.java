class Leetcode240{
	
	//方法很简单 判定 target大小 因为 col 和 row都是sorted  所以搜索大的话 col -- 小的话 row++
    public boolean searchMatrix(int[][] matrix, int target) {
        if (target < matrix[0][0] || target > matrix[matrix.length - 1][matrix[0].length -1 ])  return false;
        if(matrix == null) return false;
        int  i = 0;
        int j = matrix[0].length - 1;
        while(i < matrix.length && j > -1){
            if(matrix[i][j] == target) return true;
            if(matrix[i][j] < target ) i++ ;
            
            else if(matrix[i][j] > target ) j--;
            
        }
        
        return false;
    }
}