package com.LimePencil.Q2753;

import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int A = in.nextInt();
        if(A%4 == 0 && (!(A%100 == 0)||A%400 == 0)){
            System.out.println("1");
        }
        else{
            System.out.println("0");
        }
        in.close();
    }
}