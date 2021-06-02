package com.LimePencil.Q4344;

import java.io.*;
import java.text.DecimalFormat;
import java.util.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(in.readLine());
        StringBuilder ans = new StringBuilder();
        DecimalFormat df = new DecimalFormat("0.000");
        for(int i = 0;i<N;i++){
            int[] nums = Arrays.stream(in.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            int sum = 0;
            for(int j=1;j<=nums[0];j++){
                sum+= nums[j];
            }
            double avg = sum/(double)nums[0];
            int count = 0;
            for(int j=1;j<=nums[0];j++){
                if(nums[j] > avg){
                    count++;
                }
            }
            ans.append(df.format(count/(double)nums[0]*100) +"%" + "\n");
        }
        out.write(ans.toString());
        out.close();
        in.close();
    }
}