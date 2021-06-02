package com.LimePencil.Q2869;

import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] nums = Arrays.stream(in.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int oneDay = (nums[0]-nums[1]);
        int counter = (int) Math.ceil((nums[2]-nums[0])/(double)oneDay+1);
        out.write(String.valueOf(counter));
        out.close();
        in.close();
    }
}