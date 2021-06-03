package com.LimePencil.Q4153;

import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] temp; 
        int[] zero ={0,0,0};
        StringBuilder str = new StringBuilder();
        while(!Arrays.equals(temp = Arrays.stream(in.readLine().split(" ")).mapToInt(Integer :: parseInt).toArray(),zero)){
            Arrays.sort(temp);
            if(temp[0]*temp[0] + temp[1]*temp[1] == temp[2]*temp[2]){
                str.append("right\n");
            } else{
                str.append("wrong\n");
            }
        }
        out.write(str.toString());
        out.close();
        in.close();
    }
}