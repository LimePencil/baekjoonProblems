package com.LimePencil.Q2884;

import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int A = in.nextInt();
        int B = in.nextInt();
        if(A> 0){
            if(B>0){
                System.out.println("1");
            }
            else{
                System.out.println("4");
            }
        }
        else{
            if(B>0){
                System.out.println("2");
            }
            else{
                System.out.println("3");
            }
        }
        in.close();
    }
}