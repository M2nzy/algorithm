import java.util.*;
class Solution {
    public int[] solution(int[] prices) {
        int[] count = new int[prices.length];
        int len = prices.length;
        
        for (int i=0; i<len; i++){
            for(int j=i+1; j<len; j++){
                if(prices[i] == prices[j]){
                    count[i] += 1;
                }
                else if(prices[i] < prices[j]){
                    count[i] +=1;
                    
                }
                else if(prices[i] > prices[j]){
                    count[i] += 1;
                    break;
                }
            }
        }
        
        return count;
    }       
}