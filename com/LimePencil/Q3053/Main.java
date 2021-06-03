package com.LimePencil.Q3053;

import java.io.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        int rad = Integer.parseInt(in.readLine());
        out.write(Math.PI*rad*rad+"\n"+rad*rad*2+"\n");
        out.close();
        in.close();
    }
}