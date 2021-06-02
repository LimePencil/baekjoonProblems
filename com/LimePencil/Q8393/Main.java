package com.LimePencil.Q8393;

import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int A = in.nextInt();
        System.out.println((A*(1+A))/2);
        in.close();
    }
}