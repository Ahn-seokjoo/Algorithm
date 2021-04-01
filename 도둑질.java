import java.util.*;

class Solution {
    public int solution(int[] money) {
        int[] dp = new int[money.length];
       
        int answer = 0;
        dp[0] = money[0];
        dp[1] = Math.max(money[0],money[1]);
        
        for(int i=2;i<money.length-1;i++){
            dp[i] = Math.max(dp[i-1],dp[i-2]+money[i]);
        }
        
        answer = dp[money.length-2];
        dp[0] = 0;
        dp[1] = money[1];
        
        for(int i =2;i<money.length;i++){
            dp[i] = Math.max(dp[i-1],dp[i-2]+money[i]);
        }
        answer = Math.max(answer,dp[money.length-1]);
        return answer;
    }
}
# 0번을 쓸 경우 맨끝에 요소를 안쓰고, 0번을 안 쓸 경우 끝까지 for문 돌리기
