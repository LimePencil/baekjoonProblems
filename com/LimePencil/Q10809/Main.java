package com.LimePencil.Q10809;

import java.io.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        String word = in.readLine();
        StringBuilder ans = new StringBuilder();
        for(int i = 0;i<26;i++){
            ans.append(word.indexOf(Character.toString(97+i)) + " ");
        }
        out.write(ans.toString());
        out.close();
        in.close();
    }
}