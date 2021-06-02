package com.LimePencil.Q2577;

import java.io.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        String num = String.valueOf(Integer.parseInt(in.readLine())*Integer.parseInt(in.readLine())*Integer.parseInt(in.readLine()));
        int[] digits = new int[10];
        StringBuilder str = new StringBuilder();
        for(int i =0;i<num.length();i++){
            digits[Character.getNumericValue(num.charAt(i))]++;
        }
        for(int i = 0;i<10;i++){
            str.append(digits[i] + "\n");
        }
        out.write(str.toString());
        out.close();
        in.close();
    }
}