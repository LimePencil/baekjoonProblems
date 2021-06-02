package com.LimePencil.Q10952;

import java.io.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder str = new StringBuilder();
        while(true) {
            String[] nums = in.readLine().split(" ");
            int A = Integer.parseInt(nums[0]) + Integer.parseInt(nums[1]);
            if(A == 0){
                break;
            }
            str.append(A + "\n");
            
        }
        out.write(str.toString());
        out.close();
        in.close();
    }
}