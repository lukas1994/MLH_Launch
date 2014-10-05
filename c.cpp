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


int len(int n) {
    int cnt = 0;
    while (n > 0) {
        n /= 10;
        cnt++;
    }
    return cnt;
}
int main() {
    int k, l = 1;
    cin >> k;

    if (k == 1 || k == 2) {
        cout << k << endl;
        return 0;
    }
    int i;

    for (i = 1; k > 0; i++) {
        if (i % 4 == 0) {
            if (k - len(i) <= 0)
                break;
            k -= len(i);
        }
        else {
            if (k - len(i) - 1 <= 0)
                break;
            k -= len(i)+1;
        }
    }
    i--;
    if (i % 2 == 1) {
        i = 10*i+2;
    }
    if (i % 2 == 0) {
        i = 10*i;
    }
    int left = len(i)-k;
    while (left > 0) {
        i /= 10;
        left--;
    }
    
    cout << i << endl;



}
