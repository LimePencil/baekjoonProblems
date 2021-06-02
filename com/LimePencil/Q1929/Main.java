package com.LimePencil.Q1929;

import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] nums = Arrays.stream(in.readLine().split(" ")).mapToInt(Integer :: parseInt).toArray();
        StringBuilder str = new StringBuilder();
        boolean[] isPrimeNumber = new boolean[nums[1] + 1];
        for (int i = 2; i <= nums[1]; i++) {
            if (!isPrimeNumber[i]) {
                if(i>=nums[0]){
                    str.append(i + "\n");
                }
                for (int j = i; (long)j * (long)i <= nums[1]; j++) {
                    isPrimeNumber[i * j] = true;
                }
            }
        }
        out.write(str.toString());
        out.close();
        in.close();
    }
}