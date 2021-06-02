package com.LimePencil.Q10250;

import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(in.readLine());
        for(int i = 0;i<N;i++){
            int[] nums = Arrays.stream(in.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            int number_from_left = nums[2]/nums[0]+1;
            int number_from_bottom = nums[2]%nums[0];
            if(number_from_bottom == 0){
                number_from_bottom = nums[0];
                number_from_left--;
            }
            out.write(String.valueOf(number_from_bottom*(100)+number_from_left));
            out.newLine();
        }
        out.close();
        in.close();
    }
}