package com.LimePencil.Q2739;

import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int A = in.nextInt();
        for(int i = 1;i<=9;i++){
            System.out.println(A + " * " + i + " = " + (A*i));
        }
        in.close();
    }
}