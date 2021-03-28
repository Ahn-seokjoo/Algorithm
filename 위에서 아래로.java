import java.util.*;

public class Main{
  public static void main(String[] args){
    int n,m;
    
    Scanner sc = new Scanner(System.in);
    n = sc.nextInt();
    Integer[] array= new Integer[n];

    for(int i=0;i<n;i++){
      array[i] = sc.nextInt();
    }
    // 기본 정렬 라이브러리 이용하여 내림차순 정렬 
    Arrays.sort(array,Collections.reverseOrder());

    for(int i =0;i<n;i++){
      System.out.print(array[i]+" ");
    }
  }
}
