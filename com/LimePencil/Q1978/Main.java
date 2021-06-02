package com.LimePencil.Q1978;

import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        Integer.parseInt(in.readLine());
        int[] nums = Arrays.stream(in.readLine().split(" ")).mapToInt(Integer :: parseInt).toArray();
        Arrays.sort(nums);
        boolean[] primes = isPrime(nums[nums.length-1]);
        int counter = 0;
        for(int i:nums){
            if(primes[i-1] == true){
                counter++;
            }
        }
        out.write(String.valueOf(counter));
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