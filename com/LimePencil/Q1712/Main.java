package com.LimePencil.Q1712;

import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] nums = Arrays.stream(in.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int counter = 0;
        if(nums[2]<=nums[1]){
            counter = -1;
        }
        else{
            counter = (int)((nums[0] +0.1)/(double) (nums[2]-nums[1])+1);
        }
        out.write(String.valueOf(counter));
        out.close();
        in.close();
    }
}