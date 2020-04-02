import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the surfaceArea function below.
    static int surfaceArea(int[][] A, int H, int W) {
        int i,j;
        int ans=2*W*H;
        //width
        for(i=0;i<H;i++){
            ans+=A[i][0];
            for(j=1;j<W;j++){
                ans += Math.abs(A[i][j] - A[i][j-1]);
            }
            ans+=A[i][W-1];
        }
        //height
        System.out.println(ans);
        for(i=0;i<W;i++){
            ans+=A[0][i];
            for(j=1;j<H;j++){
                //System.out.println(Math.max(0, (A[j][i] - A[j-1][i])));
                ans += Math.abs(A[j][i] - A[j-1][i]);
            }
            ans+=A[H-1][i];
        }
        return ans;

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] HW = scanner.nextLine().split(" ");

        int H = Integer.parseInt(HW[0]);

        int W = Integer.parseInt(HW[1]);

        int[][] A = new int[H][W];

        for (int i = 0; i < H; i++) {
            String[] ARowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < W; j++) {
                int AItem = Integer.parseInt(ARowItems[j]);
                A[i][j] = AItem;
            }
        }

        int result = surfaceArea(A,H,W);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
