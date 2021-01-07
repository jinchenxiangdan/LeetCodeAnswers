class Leet84{
	
	//这题是我差不多两年前刚开始刷题的时候写的 我清楚记得这是我第一次刷hard的题目 现在看来写法有点蠢 不过想法很容易理解 直接循环判定
	//选出最大面积 
	
    public int largestRectangleArea(int[] heights) {
        int width = 1;
        int area = 0;
        int max = 0;
        for(int i = 0; i < heights.length; i++){
            if(i != heights.length - 1){
                for(int j = i+1; j < heights.length; j++){
                    if(heights[j] < heights[i])
                        break;
                    else
                        width++;
                }
            }
                
            
            if(i != 0){
                for(int k = i-1;  k >= 0; k--){
                    if(heights[k] < heights[i])
                        break;
                    else
                        width++;
                
                }               
                
            }

            
            area = width * heights[i];
            
            if (area > max)
                max = area;
            
            width = 1;
        }
        
        return max;
    }
} 