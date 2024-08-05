import java.util.*;
class Solution {
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        
        boolean[][] visited = new boolean[n][m];
        Queue<int[]> q = new ArrayDeque<>();
        
        q.add(new int[]{0,0,1});
        visited[0][0] = true;
        
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        
        while(!q.isEmpty()){
            int[] cur = q.remove();
            int x = cur[0], y = cur[1], dist = cur[2];
            visited[x][y] = true;
            if((x==n-1)&& (y == m-1)){
                return dist;
            }
            
            for(int i = 0; i<4; i++){
                int nx = dx[i] + x;
                int ny = dy[i]+y;
                
                if (0<= nx && nx < n && 0 <= ny && ny < m){
                    if ((maps[nx][ny] == 1) && (visited[nx][ny] == false)){
                        visited[nx][ny] = true;
                        q.add(new int[]{nx, ny, dist+1});
                    }
                }
                
            }
        }
        
        
        return -1;
    }
    
}