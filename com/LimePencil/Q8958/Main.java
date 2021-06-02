package com.LimePencil.Q8958;

import java.io.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(in.readLine());
        StringBuilder ans = new StringBuilder();
        for(int i = 0;i<N;i++){
            String str = in.readLine();
            int prevPoint = 0;
            int sum = 0;
            for(int j=0;j<str.length();j++){
                if(str.charAt(j) == 'O'){
                    prevPoint++;
                    sum +=prevPoint;
                }
                else{
                    prevPoint = 0;
                }
                
            }
            ans.append(sum + "\n");
        }
        out.write(ans.toString());
        out.close();
        in.close();
    }
}