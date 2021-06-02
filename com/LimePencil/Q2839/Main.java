package com.LimePencil.Q2839;

import java.io.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(in.readLine());
        int maxThree = N/3;
        int min = Integer.MAX_VALUE;
        for(int i =0;i<=maxThree;i++){
            if((N-i*3)%5 == 0){
                min = Math.min(min, (N-i*3)/5+i);
            }
        }
        if(min == Integer.MAX_VALUE){
            min = -1;
        }
        out.write(String.valueOf(min));
        out.close();
        in.close();
    }
}