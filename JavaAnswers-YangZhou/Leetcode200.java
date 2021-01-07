
public class Leetcode200 {
	
	
	//这题很简单 DFS 递归搜索  虽然BFS也可以 但相对而言复杂太多 而且容易出错
	// 主题思想就是DFS走过的标记 然后看有多少个是可以连起来算一个island.
    public int numIslands(char[][] grid) {
        int count = 0;
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[i].length; j++){
                if(grid[i][j] == '1'){
                    count ++;
                    int w = j;
                    int h = i;
                    helper(grid, w, h);
                   
                }
            
            }
        }
        return count;
    }
    
    public void helper(char[][]grid, int w, int h){
        
        if(h < 0 || w< 0 || h >= grid.length || h>=grid.length || w>=grid[h].length|| grid[h][w] == '0') return;
        grid[h][w]='0';
        helper(grid, w+1, h);
        helper(grid, w-1, h);
        helper(grid, w, h+1);
        helper(grid, w, h-1);
    }

}
