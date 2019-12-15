import java.util.*;

class LeetCode695 {

    /**
    Author: Shawn Jin
    Runtime: 3 ms, faster than 48.14% of Java online submissions for Max Area of Island.
    Memory Usage: 45.7 MB, less than 7.41% of Java online submissions for Max Area of Island.

    loop the grid and using BFS to loop the map. Mark visited during DFS;
    */
    private static int[][] mark;
    public static int maxAreaOfIsland(int[][] grid) {
        // initialize the matrix of mark
        mark = new int[grid.length][grid[0].length];
        printLists(grid);

        // loop
        int max = -1;
        int count = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid.length; j++) {
                if (mark[i][j] == 0 && grid[i][j] == 1) {
                    count += 1;
                    int size = helper(grid, i, j);
                    if (max < size) max = size;


                }

            }
            // System.out.println(" ");
        }
        System.out.println("count: "+ max);


        return max;
    }

    private static int helper(int[][] grid, int i, int j) {
        // base case
        // System.out.println("get in helper ");
        // System.out.printf("x: %d, y: %d\n", i, j);
        // check if is the valid input
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length) {
            return 0;
        }
        // out
        if (mark[i][j] == 1 || grid[i][j] == 0) {
            return 0;
        }

        assert grid[i][j] == 1;
        // mark it as searched
        mark[i][j] = 1;
        return helper(grid, i-1, j) + helper(grid, i, j-1)
            + helper(grid, i+1, j) + helper(grid, i, j+1) + 1;


    }



    public static void main(String[] args) {
        int[][] input = new int[][] {{0,0,1,0,0,0,0,1,0,0,0,0,0},
                                     {0,0,0,0,0,0,0,1,1,1,0,0,0},
                                     {0,1,1,0,1,0,0,0,0,0,1,0,0},
                                     {0,1,0,0,1,1,0,0,1,0,1,0,0},
                                     {0,1,0,0,1,1,0,0,1,1,1,0,0},
                                     {0,0,0,0,0,0,0,0,0,0,1,0,0},
                                     {0,0,0,0,0,0,0,1,1,1,0,0,0},
                                     {0,0,0,0,0,0,0,1,1,0,0,0,0}};

        int[][] input2 = new int[][] {{0,1}};
        System.out.println(maxAreaOfIsland(input2));
    }

    public static void printLists(int[][] input) {
        for (int i = 0; i < input.length; i++) {
            for (int j = 0; j < input[i].length; j++) {
                System.out.print(input[i][j]);
            }
            System.out.println();
        }
    }
}
