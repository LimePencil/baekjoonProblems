package com.LimePencil.Q1018;

import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] nums = Arrays.stream(in.readLine().split(" ")).mapToInt(Integer :: parseInt).toArray();
        boolean[][] chess = new boolean[nums[0]][nums[1]];
        for(int i = 0; i< nums[0]; i++){
            String line = in.readLine();
            char[] letters = line.toCharArray();
            for (int j =0; j < nums[1]; j++) {
                char c = letters[j];
                if(c == 'W'){
                    chess[i][j] = true;
                }

            }
        }
        int min = Integer.MAX_VALUE;
        for(int i  = 0; i<nums[0]-7;i++){
            for(int j = 0;j<nums[1]-7;j++){
                int startWhite = 0;
                boolean currentPoint = true;
                for(int k = 0;k < 8;k++){
                    for(int m =0;m < 8;m++){
                        boolean c = chess[k+i][m+j];    
                        if(currentPoint != c){
                            startWhite ++;
                        }
                        currentPoint = !currentPoint;
                    }
                    currentPoint = !currentPoint;
                }
                int currMin = Math.min(64-startWhite,startWhite);
                min = Math.min(min,currMin);
            }
        }
        out.write(String.valueOf(min));
        out.close();
        in.close();
    }
}