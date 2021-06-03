package com.LimePencil.Q3009;

import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        ArrayList<Integer> xCoordinates = new ArrayList<Integer>();
        ArrayList<Integer> yCoordinates = new ArrayList<Integer>();
        for(int i = 0;i<3;i++){
            int[] nums = Arrays.stream(in.readLine().split(" ")).mapToInt(Integer :: parseInt).toArray();
            if(xCoordinates.contains(nums[0])){
                xCoordinates.remove(Integer.valueOf(nums[0]));
            }
            else{
                xCoordinates.add(nums[0]);
            }
            if(yCoordinates.contains(nums[1])){
                yCoordinates.remove(Integer.valueOf(nums[1]));
            }
            else{
                yCoordinates.add(nums[1]);
            }
        } 
        out.write(xCoordinates.get(0) + " " + yCoordinates.get(0));
        out.close();
        in.close();
    }
}