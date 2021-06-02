package com.LimePencil.Q1546;

import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(in.readLine());
        double sum = 0;
        int[] nums = Arrays.stream(in.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int maxNum = Integer.MIN_VALUE;;
        for(int i = 0;i<N;i++){
            int a = nums[i];
            if(a>maxNum){
                maxNum = a;
            }
        }
        for(int i=0;i<N;i++){
            sum += nums[i]/(double)maxNum*100;
        }
        out.write(Double.toString(sum/N));
        out.close();
        in.close();
    }
}