package com.LimePencil.Q9020;

import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(in.readLine());
        ArrayList<Integer> numList = new ArrayList<Integer>();
        int max = Integer.MIN_VALUE;
        StringBuilder str = new StringBuilder();
        for(int i = 0;i<N;i++){
            int num = Integer.parseInt(in.readLine());
            numList.add(num);
            max = Math.max(max,num);
        }
        boolean[] isNotPrimeNumber = new boolean[max + 1];
        for (int i = 2; i*i <= max; i++) {
            if (isNotPrimeNumber[i] == false) {
                for (int j = i; j *i <= max; j++) {
                    isNotPrimeNumber[i * j] = true;
                }
            }
        }
        for(int x:numList){
            for(int a = x/2;a>=2;a--){
                if(isNotPrimeNumber[a] == false&&isNotPrimeNumber[x-a] == false){
                    str.append(a + " " + (x-a) + "\n");
                    break;
                }
            }
        }
        out.write(str.toString());
        out.close();
        in.close();
    }
}