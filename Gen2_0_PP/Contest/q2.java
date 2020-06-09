import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner inp= new Scanner(System.in);
        int n=inp.nextInt();
        int k=inp.nextInt();
        int csum=0;
        int s=0;
        int arr[]=new int[n];
        for(int i=0;i<n;i++)
        {
            arr[i]=inp.nextInt();
        }
        for(int i=0;i<n;i++)
        {
            if(arr[i]==k)
                csum++;
        }
        for(int i=0;i<n;i++)
        {
            for(int j=i;j<n-1;j++)
        {
                if((i+1)==(j+1))
                {
                if(arr[i]+arr[j+1]==k)
                    s++; }
            }
        }
        System.out.println(csum+s);
        }
}

