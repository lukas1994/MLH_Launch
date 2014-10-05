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
    int l,k,m,a[1000],b[1000],c[1000];
    cin >> l >> k >> m;
    REP(i, l)
        cin >> a[i];
    REP(i, k)
        cin >> b[i];
    REP(i, m)
        cin >> c[i];

    map<int, long long> mm;

    int maxi = 0, maxv = 0;
    REP(i, l) {
        REP(j, k) {
            REP(q,m) {
                int sum = a[i]+b[j]+c[q];
                if (mm.count(sum) > 0)
                    mm[sum]++;
                else
                    mm[sum] = 1;
                if (maxv < mm[sum]) {
                    maxv = mm[sum];
                    maxi = sum;
                }
            }
        }
    }
    cout << maxi << endl;

}
