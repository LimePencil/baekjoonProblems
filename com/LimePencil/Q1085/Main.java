package com.LimePencil.Q1085;

import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] nums = Arrays.stream(in.readLine().split(" ")).mapToInt(Integer :: parseInt).toArray();
        int min = Math.min(Math.min(nums[2]-nums[0],nums[0]),Math.min(nums[3]-nums[1],nums[1]));    
        out.write(String.valueOf(min));
        out.close();
        in.close();
    }
}