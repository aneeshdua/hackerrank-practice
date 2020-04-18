/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
    
   	public static void main (String[] args) {
		//code
		Scanner sc= new Scanner(System.in);
		int t = sc.nextInt();
		for(int z=0;z<t;z++){
		    int n = sc.nextInt();
		    int amount = sc.nextInt();
		    int arr[] = new int[n];
		    for(int i=0;i<n;i++)
		    {
		        arr[i] = sc.nextInt();
		    }
		    //Arrays.sort(arr);
		    int dp[] = new int[amount+1];
		    Arrays.fill(dp,Integer.MAX_VALUE);
		    dp[0]=0;
		    for(int i=0;i<=amount;i++){
		        for(int j=0; j<n; j++){
		            //System.out.println(dp[i]);
		           if(i>=arr[j]){
		                if(dp[i-arr[j]]!=Integer.MAX_VALUE)
		                    dp[i] = Math.min(dp[i], 1+dp[i-arr[j]]);
		            }
		            //dp[j] += dp[j-arr[i]]; 
		            //System.out.println(dp[i]);
		        }
		    }
		    if(dp[amount]==Integer.MAX_VALUE)
		        System.out.println(-1);
		    else
		        System.out.println(dp[amount]);
		         
		}
	}
}