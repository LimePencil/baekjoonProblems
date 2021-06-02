package com.LimePencil.Q2292;

import java.io.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(in.readLine());
        int counter = 1;
        int num = 1;
        while(num < N){
            num+=6*counter;
            counter++;
        }
        out.write(String.valueOf(counter));
        out.close();
        in.close();
    }
}