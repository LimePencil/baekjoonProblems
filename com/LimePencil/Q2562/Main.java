package com.LimePencil.Q2562;

import java.io.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        int maxNum = Integer.MIN_VALUE;
        int maxPos = 0;
        for(int i = 0;i<9;i++){
            int a = Integer.parseInt(in.readLine());
            if(a>maxNum){
                maxNum = a;
                maxPos = i+1;
            }
        }
        out.write(maxNum + "\n" + maxPos);
        out.close();
        in.close();
    }
}