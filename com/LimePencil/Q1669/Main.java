import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws NumberFormatException, IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] nums = Arrays.stream(in.readLine().split(" ")).mapToInt(Integer :: parseInt).toArray();
        if (nums[0]==nums[1]){
            out.write(String.valueOf(0));
        }
        else{
            int min = (int) Math.floor(Math.sqrt(nums[1]-nums[0]));
            int more = (int) Math.ceil((nums[1]-nums[0] - min*min)/(double)min);
            out.write(String.valueOf(min*(2)-1+more));
        }
        out.newLine();
        out.close();
        in.close();
    }
}