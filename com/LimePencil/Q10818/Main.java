package com.LimePencil.Q10818;

import java.io.*;
import java.util.Arrays;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        Integer.parseInt(in.readLine());
        int[] nums = Arrays.stream(in.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        Arrays.sort(nums);
        out.write(nums[0] + " " + nums[nums.length-1]);
        out.close();
        in.close();
    }
}