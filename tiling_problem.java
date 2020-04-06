/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
    /*static int count_tiles(int n){
        if(n==1 || n==2)
            return n;
        else    
            return (count_tiles(n-1)+count_tiles(n-2));
    }*/
	public static void main (String[] args) {
		//code
		Scanner sc = new Scanner(System.in);
		long dp[] = new long[71];
		dp[0] = 0;
		dp[1] = 1;
		dp[2] = 2;
		for(int i = 3;i<71;i++)
		{
		    dp[i] = dp[i-2]+dp[i-1];
		}
		int t = sc.nextInt();
		for(int z=0;z<t;z++){
		    int n = sc.nextInt();
		    //int res = count_tiles(n);
		    System.out.println(dp[n]);
		}
	}
}