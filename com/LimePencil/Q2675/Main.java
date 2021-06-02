package com.LimePencil.Q2675;

import java.io.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));

        try {
            String line = "";
            StringBuilder ans = new StringBuilder();
            while((line = in.readLine()) != null){
                String[] words = line.split(" ");
                 if(words.length > 1){
                    for(int i = 0;i<words[1].length();i++){
                        ans.append(words[1].substring(i,i+1).repeat(Integer.parseInt(words[0])));
                    }
                    ans.append("\n");
                }
            }
            out.write(ans.toString());
            in.close();
        } finally {
            out.close();
        }
    }
}