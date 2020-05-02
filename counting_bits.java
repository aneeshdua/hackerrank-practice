class Solution {
    public int[] countBits(int num) {
        if(num==0){
            int temp[] = {0};
                return temp;
        }    
        else if(num==1){
            int temp[] = {0,1};    
            return temp;
        }    
       int power=0;
        int res[] = new int[num+1];
        res[0]=0;
        res[1]=1;
        int curr_pow = 1;
        int index = 1;
        for(int i=1;i<=num;i++){
            if(i==curr_pow){
                res[i] = 1;
                power++;
                index=1;
                curr_pow = curr_pow*2;
                //continue;
            }
            else{
                res[i] = 1+res[index];
                index++;
            }
            
        }
        return res;
        /*
        //****ALTERNATE SOLUTION***********
        int[] result = new int[num+1];
        int p = 1; //p tracks the index for number x
        int pow = 1;
        for(int i=1; i<=num; i++){
          if(i==pow){
            result[i] = 1;
            pow <<= 1;
            System.out.println(pow);
            p = 1;
        }else{
            result[i] = result[p]+1;
            p++;
        }
     }
     return result;*/
    }
}