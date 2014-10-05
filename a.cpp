#include <algorithm>
#include <stack>
#include <bitset>
#include <cassert>
#include <map>
#include <string>
#include <iostream>
#include <queue>
#include <set>
#include <vector>
#include <cmath>
#include <limits>

using namespace std;

typedef long long ll;
typedef vector<int> vi;

#define sz(x) int((x).size())
#define FOR(i,a,b) for(int (i) = (a); (i) < (b); ++(i))
#define REP(i,n) for(int (i) = 0; (i) < (n); ++(i))
#define pb push_back
#define all(c) (c).begin(), (c).end()
#define square(a) (a)*(a)
#define mp(a,b) make_pair((a),(b))

const int oo = numeric_limits<int>::max();

int data[100][100], dp[100][100];
int calc(int i, int j) {
    if (i == 0 && j == 0)
        return data[i][j];
    if (i == 0)
        return data[i][j] + calc(i, j-1);
    if (j == 0)
        return data[i][j] + calc(i-1, j);
    if (dp[i][j] != -1)
        return dp[i][j];
    return dp[i][j] = min(calc(i-1, j), calc(i, j-1)) + data[i][j];
}

int main() {
    int n;
    cin >> n;
    REP(i, n) {
        REP(j, n) {
            dp[i][j] = -1;
            cin >> data[i][j];
        }
    }
    cout <<  calc(n-1,n-1) << endl;
    return 0;
    REP(i, n) {
        int add = 0;
        REP(j, n) {
            //int add = 0;
            if (i != 0)
                add = data[i-1][j];
            if (j != 0)
                add = min(add, data[i][j-1]);
            data[i][j] += add;
        }
    }
    cout << data[n-1][n-1] << endl;
}

