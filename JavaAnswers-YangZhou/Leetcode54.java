class Leetcode54{
	//这道题没啥好说的 我的方法可能有点笨 我的想法就是 他反正是顺时针旋转 那么我就直接以这个顺序往list 添加东西 然后把list外层已经走过的
	//给他去掉 把新的里面没遍历过的list给他送进去递归方式继续遍历
	
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> res = new ArrayList<>();
        helper(matrix, res);
        return res;
        
    } 
        
    public void helper(int[][] matrix, List<Integer> res){
        if(matrix.length == 0 || matrix[0].length == 0) return;
            
        if (matrix.length == 1){
            if(matrix[0].length ==1 ){
                res.add(matrix[0][0]); 
                return;
            } else {
                for(int j = 0; j < matrix[0].length; j++)
                    res.add(matrix[0][j]);
                return;
            }
        }
           
        if(matrix[0].length == 1){
            for(int i = 0; i < matrix.length; i++)
                    res.add(matrix[i][0]);
            return;
        }
        
        if(matrix.length == 2){
            for(int j = 0; j < matrix[0].length; j++)
                res.add(matrix[0][j]);
            for(int j = matrix[0].length - 1; j >= 0; j--)
                res.add(matrix[1][j]);
            return;
        }
        
        if(matrix[0].length == 2){
            res.add(matrix[0][0]);
     
            for(int i = 0; i < matrix.length; i++)
                res.add(matrix[i][1]);
            for(int i = matrix.length - 1; i >= 1; i--)
                res.add(matrix[i][0]);
            return;
        }
        
        
        for(int j = 0; j < matrix[0].length; j++)
                    res.add(matrix[0][j]);
        
        for(int i = 1; i < matrix.length; i++)
                    res.add(matrix[i][matrix[i].length - 1]);
    
        for(int j = matrix[0].length - 2; j >= 0; j--)
                    res.add(matrix[matrix.length-1][j]);
        
        for(int i = matrix.length -2; i>= 1; i--)
                    res.add(matrix[i][0]);
        
        
        int[][] temp = new int[matrix.length-2][matrix[0].length-2];
        for(int i = 1; i < matrix.length - 1; i++){
            for(int j = 1; j < matrix[i].length - 1; j++)
            {
                temp[i-1][j-1] = matrix[i][j];
            }
        }
        
        
        helper(temp, res);
    }
}