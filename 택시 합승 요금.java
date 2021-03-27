import java.lang.*;
class Solution {
    public int solution(int n, int s, int a, int b, int[][] fares) {
        int INF = 4000001;
        
        int[][] graph = new int[n+1][n+1];
        for(int i=1;i<n+1;i++){
            for(int j=1;j<n+1;j++){
                graph[i][j] = INF;
            }
        }
        for(int i=1;i<n+1;i++){
            for(int j=1;j<n+1;j++){
                if (i == j){
                    graph[i][j] = 0;
                }
            }
        }
        for(int i=0;i<fares.length;i++){
            graph[fares[i][0]][fares[i][1]] = fares[i][2];
            graph[fares[i][1]][fares[i][0]] = fares[i][2];
        }
        
        for(int k=1;k<n+1;k++){
            for(int i=1;i<n+1;i++){
                for(int j=1;j<n+1;j++){
                    graph[i][j] = Math.min(graph[i][j],graph[i][k]+graph[k][j]);
                }
            }
        }
        int answer = INF;
        for(int i=1;i<n+1;i++){
            answer = Math.min(answer,graph[s][i]+graph[i][a]+graph[i][b]);
        }
        
        return answer;
    }
}
