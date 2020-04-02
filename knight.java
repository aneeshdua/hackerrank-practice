public class knight {
    static int N=8;
    
    static boolean solve(int x, int y, int movei, int sol[][],int x_move[], int y_move[]){
        int k, next_x, next_y;
        if(movei == N*N){
            return true;
        }
        for(k=0;k<N;k++){
            next_x = x+x_move[k];
            next_y = y+y_move[k];
            if(next_x >=0 && next_x <N && next_y >=0 && next_y <N && sol[next_x][next_y]==-1){
                sol[next_x][next_y]=movei;
                if(solve(next_x, next_y, movei+1, sol, x_move,y_move))
                    return true;
                else
                    sol[next_x][next_y] = -1;
            }
        }
        return false;
    }
    public static void main(String args[]) {
      int x_move[] = {2,-2,1,1,-1,-1,2,-2};
      int y_move[] = {1,1,-2,2,2,-2,-1,-1};
      int sol[][] = new int[8][8];
      for (int x = 0; x < N; x++) 
            for (int y = 0; y < N; y++) 
                sol[x][y] = -1;
      sol[0][0]=0;
      if(!solve(0,0,1,sol,x_move,y_move)){
          System.out.println("No soln");
      }
      else{
          for (int x = 0; x < N; x++) 
            for (int y = 0; y < N; y++) 
                System.out.print(sol[x][y]);
            System.out.println();
      }
    }
}