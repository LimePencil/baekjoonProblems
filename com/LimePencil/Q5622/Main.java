package com.LimePencil.Q5622;

import java.io.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = in.readLine();
        int counter = 0;
        for(char x:str.toCharArray()){
            if(x<=67){
                counter+=3;
            }
            else if(x<=70){
                counter+=4;
            }
            else if(x<=73){
                counter+=5;
            }
            else if(x<=76){
                counter+=6;
            }
            else if(x<=79){
                counter+=7;
            }
            else if(x<=83){
                counter+=8;
            }
            else if(x<=86){
                counter+=9;
            }
            else if(x<=90){
                counter+=10;
            }
        }
        out.write(String.valueOf(counter));
        out.close();
        in.close();
    }
}