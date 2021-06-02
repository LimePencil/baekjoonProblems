package com.LimePencil.Q2742;

import java.io.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int A = Integer.parseInt(in.readLine());
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int i = A; i >0; i--) {
            out.write(String.valueOf(i));
            out.newLine();
        }
        out.close();
        in.close();
    }
}