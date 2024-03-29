package com.LimePencil.Q4948;

import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        String input = "";
        ArrayList<Integer> numList = new ArrayList<Integer>();
        int max = Integer.MIN_VALUE;
        StringBuilder str = new StringBuilder();
        while(!(input = in.readLine()).equals("0")){
            int num = Integer.parseInt(input);
            numList.add(num);
            max = Math.max(max,num);
        }
        boolean[] isNotPrimeNumber = new boolean[max*2 + 1];
        for (int i = 2; i*i <= max*2; i++) {
            if (isNotPrimeNumber[i] == false) {
                for (int j = i; j *i <= max*2; j++) {
                    isNotPrimeNumber[i * j] = true;
                }
            }
        }
        for(int x:numList){
            int counter = 0;
            for(int a = x+1;a<=x*2;a++){
                if(isNotPrimeNumber[a] == false){
                    counter++;
                }
            }
            str.append(String.valueOf(counter) + "\n");
        }
        out.write(str.toString());
        out.close();
        in.close();
    }
}