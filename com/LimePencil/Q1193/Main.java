package com.LimePencil.Q1193;

import java.io.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(in.readLine());
        int counter = 1;
        int num = 0;
        while(num+counter < N){
            num+=counter;
            counter++;
        }
        counter++;
        int numerator = (counter %2 == 0)?counter-(N-num):N-num;

        out.write(numerator + "/" + (counter-numerator));
        out.close();
        in.close();
    }
}