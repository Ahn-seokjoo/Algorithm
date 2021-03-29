import java.util.*;

public class Main{
  public static int binary_search(int[] array,int target,int start,int end){
    if(start>end){
      return -1;
    }
    int mid = (start+end) / 2;
    if(target == array[mid]){
      return mid;
    }
    else if(target < array[mid]){
      return binary_search(array, target, start, mid-1);
    }
    else{
      return binary_search(array, target, mid+1, end);
    }
  }
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();
    int target = sc.nextInt();
    int[] arr = new int[n];

    for(int i=0;i<n;i++){
      arr[i] = sc.nextInt();
    }
    int result = binary_search(arr,target,0,n);
    if(result == -1){
      System.out.println("원소가 존재하지 않습니다");
    }
    else{
      System.out.println(result+1);
    }
  }
}
