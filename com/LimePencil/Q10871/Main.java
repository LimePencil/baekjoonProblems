package com.LimePencil.Q10871;

import java.io.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String[] given = in.readLine().split(" ");
        int N = Integer.parseInt(given[0]);
        String[] nums = in.readLine().split(" ");
        int X = Integer.parseInt(given[1]);
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder str = new StringBuilder();
        for (int i = 0; i < N; i++) {
            int A = Integer.parseInt(nums[i]);
            if(X>A){
                str.append(A + " ");
            }
        }
        out.write(str.toString());
        out.close();
        in.close();
    }
}