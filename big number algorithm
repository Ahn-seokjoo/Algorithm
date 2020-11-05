#include <bits/stdc++.h>
using namespace std;
vector<int> v;
int main()
{
    int n, m, k;
    
    cin >> n >>m >> k;
    for(int i=0;i<n;i++){
        int x;
        cin >>x;
        v.push_back(x);
    }
   sort(v.begin(),v.end()); // 정렬
   int first = v[n-1]; //6
   int second = v[n-2]; //5 
   
   int cnt = (m/(k+1)) * k; //가장큰수 더하는 횟수 찾기
   cnt += m%(k+1);
   //핵심 코드 > 큰수가 더해지는 횟수를 찾는 식 . 
   int result = 0;
   result += cnt * first; //가장 큰수 반복된 횟수 x 큰수
   result += (m-cnt) * second; // 나머지 횟수 x 두번째 수
   
   cout <<result <<endl;
   return 0;
    // n = 배열크기, m = 더하는 횟수, 
    // k = 연속해서 최대로 더할수 있는 수    
}
//그리디 알고리즘 사용법과 벡터사용법, 정렬사용법 숙지했는지 

