package com.LimePencil.Q1065;

import java.io.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(in.readLine());
        int counter = 0;
        for(int i = 1;i<=N;i++){
            if(i<100){
                counter++;
            }
            else if(i == 1000){

            }
            else if(i/100 - i/10%10 == i/10%10 - i%10){
                counter++;
            }

        }
        out.write(String.valueOf(counter));
        out.close();
        in.close();
    }
}