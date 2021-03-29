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
    int[] arr = new int[n];
    for(int i=0;i<n;i++){
      arr[i] = sc.nextInt();
    }

    int target = sc.nextInt();
    int[] arr2 = new int[target];
    for(int i =0;i<target;i++){
      arr2[i] = sc.nextInt();
    }
    Arrays.sort(arr);
    
    for(int i =0;i<target;i++){
      int result = binary_search(arr,arr2[i],0,n);
      if(result == -1){
        System.out.print("no ");
      }
      else{
        System.out.print("yes ");
      }
    }
  
  }
}
