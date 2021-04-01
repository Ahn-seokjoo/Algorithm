import java.util.*;
class Solution {
    public int solution(int[][] triangle) {
        int l =triangle.length;
        int[][] dp = new int[l][];
        
        for(int i =0;i<l;i++){
            dp[i] = new int[i+1];
        }
        
        for(int j=0;j<l;j++){
            for(int i =0;i<=j;i++){
                if(j==0){
                    dp[j][i] = triangle[0][0];
                }
                else if(i == 0){
                    dp[j][i] = dp[j-1][i] + triangle[j][i];
                }
                else if(i==j){
                    dp[j][i] = triangle[j][i] + dp[j-1][i-1];
                }
                else{
                    dp[j][i] = Math.max(dp[j-1][i-1],dp[j-1][i])+triangle[j][i];
                }
            }
        }
        int max = dp[l-1][0];
        for(int k =1;k<l;k++){
            if(dp[l-1][k] >= max){
                max = dp[l-1][k];
            }
        }
        return max;
    }
}
