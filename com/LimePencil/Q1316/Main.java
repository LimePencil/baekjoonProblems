package com.LimePencil.Q1316;

import java.io.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(in.readLine());
        int counter = 0;
        for(int j = 0;j<N;j++){
            String str = in.readLine(); 
            boolean[] letter = new boolean[26];
            char prev = '?';
            for(char x:str.toCharArray()){
                if(prev != x&&letter[(int) x - 97]){
                    counter--;
                    break;
                }
                else if(prev != x&&!letter[(int) x - 97]){
                    letter[(int) x - 97] = true;
                }
                prev = x;
            }
            counter++;
        }
        out.write(String.valueOf(counter));
        out.close();
        in.close();
    }
}