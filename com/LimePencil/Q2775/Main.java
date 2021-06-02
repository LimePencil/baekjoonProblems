package com.LimePencil.Q2775;

import java.io.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(in.readLine());
        for(int i = 0;i<N;i++){
            //int[] nums = Arrays.stream(in.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            int k = Integer.parseInt(in.readLine());
            int n = Integer.parseInt(in.readLine());
            int[][] apart = new int[k+1][n+1];
            for(int x = 0;x<k+1;x++){
                for(int y = 1;y<n+1;y++){
                    if(x==0){
                        apart[x][y] = y;
                    }
                    else{
                        apart[x][y] = apart[x-1][y] +apart[x][y-1];
                    }

                }
            }
            out.write(String.valueOf(apart[k][n]));
            out.newLine();
        }
        out.close();
        in.close();
    }
}