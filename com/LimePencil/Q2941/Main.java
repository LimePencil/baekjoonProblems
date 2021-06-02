package com.LimePencil.Q2941;

import java.io.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder str = new StringBuilder(in.readLine());
        int counter = 0;
        while(str.length() != 0){
            String temp;
            if(str.length() > 2 && str.substring(0, 3).equals("dz=")){
                counter ++;
                str.delete(0, 3);
            }
            else if(str.length()>1 && ((temp=str.substring(0, 2)).equals("z=")||temp.equals("c=")||temp.equals("c-")||temp.equals("d-")||temp.equals("lj")||temp.equals("nj")||temp.equals("s="))){
                counter ++;
                str.delete(0, 2);

            }
            else{
                counter++;
                str.delete(0, 1);
            }

        }     
        out.write(String.valueOf(counter));
        out.close();
        in.close();
    }
}