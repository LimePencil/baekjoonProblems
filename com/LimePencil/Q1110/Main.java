package com.LimePencil.Q1110;

import java.io.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = in.readLine();
        int N = Integer.parseInt(str);
        int num = N;
        int counter = 0;
        do {
            if(num/10 == 0){
                num = num*10+num;
            }
            else{
                num = (num%10)*10 + (num/10 + num%10)%10;
            }
            counter ++;
        } while (N != num);
        out.write(String.valueOf(counter));
        out.close();
        in.close();
    }
}