package com.LimePencil.Q1002;

import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(in.readLine());
        for(int i = 0;i<N;i++){
            int[] nums = Arrays.stream(in.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            double distanceBetween = Math.sqrt(Math.pow(nums[3]-nums[0], 2) + Math.pow(nums[4]-nums[1], 2));
            if(nums[0] == nums[3]&&nums[1] == nums[4]&&nums[2]==nums[5]){
                out.write("-1");
            }
            else if(distanceBetween == (double)(nums[2] + nums[5])||distanceBetween == (double)Math.abs(nums[2] - nums[5])){
                out.write("1");
            }
            else if(distanceBetween > (double)(nums[2] + nums[5])||distanceBetween < (double)Math.abs(nums[2] - nums[5])){
                out.write("0");
            }
            else{
                out.write("2");
            }
            out.newLine();
        }

        out.close();
        in.close();
    }
}
