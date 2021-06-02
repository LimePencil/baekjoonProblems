package com.LimePencil.Q2581;

import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        int A = Integer.parseInt(in.readLine());
        int B = Integer.parseInt(in.readLine());
        //int[] nums = Arrays.stream(in.readLine().split(" ")).mapToInt(Integer :: parseInt).toArray();
        boolean[] primes = isPrime(B);
        int counter = 0;
        boolean firstPrime = false;
        int first = -1;
        for(int i = A;i<=B;i++){
            if(primes[i-1] == true){
                counter += i;
                if(!firstPrime){
                    firstPrime = true;
                    first = i;
                }
            }
        }
        if(firstPrime){
            out.write(String.valueOf(counter));
            out.newLine();
            out.write(String.valueOf(first));
        }
        else{
            out.write(String.valueOf(first));
        }
        out.close();
        in.close();
    }
    public static boolean[] isPrime(int max){
        boolean[] prime = new boolean[max];
        ArrayList<Integer> primeNum = new ArrayList<Integer>();
        for(int i = 2;i<=max;i++){
            boolean yes = true;
            for(int x:primeNum){
                if(i%x == 0){
                    yes = false;
                    break;
                }
            }
            prime[i-1] = yes;
            if(yes){
                primeNum.add(i);
            }
        }
        return prime;
    }
}