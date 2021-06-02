package com.LimePencil.Q10757;

import java.io.*;
import java.math.BigInteger;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] num = in.readLine().split(" ");
        out.write(new BigInteger(num[0]).add(new BigInteger(num[1])).toString());
        out.close();
        in.close();
    }
}
