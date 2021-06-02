package com.LimePencil.Q11720;

import java.io.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(in.readLine());
        String num = in.readLine();
        int sum = 0;
        for(int i = 0;i<N;i++){
            sum += Character.getNumericValue(num.charAt(i));
        }
        out.write(String.valueOf(sum));
        out.close();
        in.close();
    }
}