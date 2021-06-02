package com.LimePencil.Q3052;

import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        Set<Integer> set = new HashSet<Integer>();
        for(int i = 0;i<10;i++){
            set.add(Integer.parseInt(in.readLine())%42);
        }
        out.write(String.valueOf(set.size()));
        out.close();
        in.close();
    }
}