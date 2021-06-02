package com.LimePencil.Q11654;

import java.io.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        char N = (in.readLine()).charAt(0);
        out.write(String.valueOf((int) N));
        out.close();
        in.close();
    }
}