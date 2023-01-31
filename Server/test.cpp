#include<bits/stdc++.h>
using namespace std;
const int N = 102;
const int W = 1e5 + 5;

long long int weight[102];
long long int value[102];
long long dp[N][W];

// long long int knapsak(int n, int cap){

//     // cout<<n<<" : "<< cap<<endl;

//     if(n == 0) return 0;
//     if(dp[n][cap] != -1) return dp[n][cap];

//     long long int v1, v2;
//     if(weight[n]<=cap) v1 = value[n] + knapsak(n-1, cap-weight[n]);
//     else v1 = 0;

//     v2 = knapsak(n-1, cap);

//     dp[n][cap] = max(v1, v2);

//     return dp[n][cap]; 
    
// }

int main(){
    int n, cap;
    cin>>n>>cap;

    for(int i=1; i<=n; i++){
        int w, v;
        cin>>w>>v;

        weight[i] = w;
        value[i] = v;
    }
    // for(int i=1; i<=n; i++) cout<<weight[i]<<" : "<<value[i]<<endl;


    // base case
    for(int i=0; i<=cap; i++) dp[0][i] = 0;

    //recursive call

    for(int i=1; i<=n; i++){
        for(int j=0; j<=cap; j++){

            long long int v1, v2;
            if(weight[i]<=j) v1 = value[i] + dp[i-1][j-weight[i]];
            else v1 = 0;

            v2 = dp[i-1][j];

            dp[i][j] = max(v1, v2);


        }
    }
    cout<<dp[n][cap]<<endl;
    return 0;
}