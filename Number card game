#include <bits/stdc++.h>

using namespace std;

int n,m;
int result;

int main(){
/* 
    int n,m,result=0;
    cin >> n >>m ;
    
    vector<int> v;
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            int x;
            cin >>x;
            v.push_back(x);
        }
    }
    sort(v.begin(),v.end());
    
    for(int i=0;i<n;i++){
        result = v[n];
    }
    cout <<endl;
    cout <<result;
    */ 
    //내가 만든 것
    cin >>n >>m ;
    for(int i=0;i<n;i++){
        int min_value=10001;
        for(int j=0;j<m;j++){
            int x;
            cin >>x;
            min_value=min(min_value, x);
        }
        result = max(result , min_value);
    }
    cout <<result<<'\n';
}
//이중 for문 사용법과, min, max 함수 사용법 숙지했는지 묻는 문제
//추가로 min value 와 max 함수의 위치를 통해 계속해서 찾음 어떤 값이 작고 큰지





