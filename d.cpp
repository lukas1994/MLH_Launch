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

int main() {
    int n, f[51], c;
    cin >> n;
    REP(i, n) {
        cin >> f[i];
    }
    cin >> c;
    long long cnt = 0;
    REP(i, n) {
        if (f[i] % c != 0)
            cnt++;
        cnt += f[i]/c;
    }
    cout << cnt*c << endl;
}

