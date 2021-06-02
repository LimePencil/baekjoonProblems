package com.LimePencil.Q2908;

import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder str = new StringBuilder(in.readLine());
        str.reverse();
        int[] nums = Arrays.stream(str.toString().split(" ")).mapToInt(Integer::parseInt).toArray();
        out.write(String.valueOf(Math.max(nums[0],nums[1])));
        out.close();
        in.close();
    }
}