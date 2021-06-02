package com.LimePencil.Q1152;

import java.io.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] ans = in.readLine().trim().split(" ");
        if(ans[0] != ""){
            out.write(String.valueOf(ans.length));
        }
        else{
            out.write(String.valueOf(0));
        }

        out.close();
        in.close();
    }
}