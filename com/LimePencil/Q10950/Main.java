package com.LimePencil.Q10950;

import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int A = in.nextInt();
        for(int i = 0;i<A;i++){
            int b = in.nextInt();
            int c = in.nextInt();
            System.out.println(b+c);
        }
        in.close();
    }
}