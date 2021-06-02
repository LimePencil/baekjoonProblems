package com.LimePencil.Q2439;

import java.io.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int A = Integer.parseInt(in.readLine());
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int i = 1; i <= A; i++) {
            String blank = " ".repeat(A-i);
            String str = "*".repeat(i);
            out.write(blank + str);
            out.newLine();
        }
        out.close();
        in.close();
    }
}