package com.LimePencil.Q4673;

import java.io.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder ans = new StringBuilder();
        boolean[] nums = new boolean[10000];
        for(int i = 1;i<=10000;i++){
            int next = i+ i/1000%100 + i/100%10 + i/10%10 + i%10;
            if(next<=10000){
                nums[next-1] = true;
            }
        }
        for(int i = 1;i<=10000;i++){
            if(!nums[i-1]){
                ans.append(i +"\n");
            }
        }
        out.write(ans.toString());
        out.close();
        in.close();
    }
}