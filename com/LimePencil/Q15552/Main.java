package com.LimePencil.Q15552;

import java.io.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int A = Integer.parseInt(in.readLine());
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int i = 0; i < A; i++) {
            String line = in.readLine();
            String[] nums = line.split(" ");
            out.write(String.valueOf((Integer.parseInt(nums[0])+Integer.parseInt(nums[1]))));
            out.newLine();
        }
        out.close();
        in.close();
    }
}