package com.LimePencil.Q2447;

import java.io.*;
public class Main{
    private static boolean[][] grid;
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(in.readLine());
        StringBuilder answer = new StringBuilder();
        grid = new boolean[n][n];
        fractal(0,0, n/3);
        for (boolean[] bs : grid) {
           for(boolean notStar : bs) {
                if(notStar){
                    answer.append(' ');
                }
                else{
                    answer.append("*");
                }
           }
           answer.append("\n");
        }
        out.write(answer.toString());
        out.close();
        in.close();
    }
    private static void fractal(int x,int y,int length){
        if(length == 0){
            return;
        }
        for(int n=0;n < 3; n++){
            for(int m =0; m<3; m++){
                if(n == 1 && m==1){
                    for(int a=x+length;a<x+length*2;a++){
                        for(int b=y+length;b<y+length*2;b++){
                            grid[a][b] = true;
                        }
                    }
                }
                else{
                    fractal(x+(n*length), y+(m*length), length/3);
                }
            }
        }
    }
}