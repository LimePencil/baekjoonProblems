package com.LimePencil.Q11653;

import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        int A = Integer.parseInt(in.readLine());
        //int[] nums = Arrays.stream(in.readLine().split(" ")).mapToInt(Integer :: parseInt).toArray();
        ArrayList<Integer> factors = new ArrayList<Integer>();
        while(A%2==0){
            A/=2;
            factors.add(2);
        }
        for(int i = 3;i<=(int)Math.sqrt(A);i+=2){
            while(A%i==0){
                A/=i;
                factors.add(i);
            }
        }
        if(A!=1){
            factors.add(A);
        }
        for(int x:factors){
            out.write(String.valueOf(x)+"\n");
        }
        out.close();
        in.close();
    }

}