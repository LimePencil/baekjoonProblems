package com.LimePencil.Q1157;

import java.io.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        String word = in.readLine().toUpperCase();
        int[] arr = new int[26];
        for(int i = 0;i<word.length();i++){
            arr[(int)(word.charAt(i))-65]++;
        }
        int maxNum = Integer.MIN_VALUE;
        int maxIndex = 0;
        boolean duplicate = false;
        for(int i =0;i<26;i++){
            if(maxNum < arr[i]){
                maxIndex = i;
                maxNum = arr[i];
                duplicate = false;
            }
            else if(maxNum == arr[i]){
                duplicate = true;
            }
        }
        if(duplicate){
            out.write(Character.toString('?'));
        }
        else{
            out.write(Character.toString((char) (maxIndex+65)));
        }
        out.close();
        in.close();
    }
}