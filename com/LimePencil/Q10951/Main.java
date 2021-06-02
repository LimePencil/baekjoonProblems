package com.LimePencil.Q10951;

import java.io.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder str = new StringBuilder();
        String line;
        while((line = in.readLine()) != null) {
            String[] nums = line.split(" ");
            int A = Integer.parseInt(nums[0]) + Integer.parseInt(nums[1]);
            str.append(A + "\n");
            
        }
        out.write(str.toString());
        out.close();
        in.close();
    }
}