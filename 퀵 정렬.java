import java.util.*;

public class Main{
  public static void quickSort(int[] arr,int start,int end){
    if(start >= end) return;
    int pivot = start;
    int left = start +1;
    int right = end;
    while(left<=right){
      //피벗보다 큰 데이터를 찾을 때 까지
      while (left <= end &&arr[left] <= arr[pivot]) left ++;
      //피벗보다 작은 데이터를 찾을 때 까지
      while (right> start && arr[right]>=arr[pivot]) right --;
      // 엇갈렸다면
      if(left > right){
        int temp = arr[pivot];
        arr[pivot] = arr[right];
        arr[right] = temp;
      }
      // 안 엇갈렸다면
      else{
        int temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
      }
    }
    quickSort(arr,start,right-1);
    quickSort(arr,right+1,end);
  }
  public static void main(String[] main){
    int n = 10;
    int[] arr = {7,5,9,0,3,1,6,2,4,8};

    quickSort(arr,0,n-1);
    
    for(int i=0;i<n;i++){
      System.out.print(arr[i]+" ");
    }
  }
}
