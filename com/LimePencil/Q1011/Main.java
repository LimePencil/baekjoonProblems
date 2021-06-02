package com.LimePencil.Q1011;

import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(in.readLine());
        for(int i = 0;i<N;i++){
            int[] nums = Arrays.stream(in.readLine().split(" ")).mapToInt(Integer :: parseInt).toArray();
            int min = (int) Math.floor(Math.sqrt(nums[1]-nums[0]));
            int more = (int) Math.ceil((nums[1]-nums[0] - min*min)/(double)min);
            out.write(String.valueOf(min*(2)-1+more));
            out.newLine();
        }
        out.close();
        in.close();
    }
}