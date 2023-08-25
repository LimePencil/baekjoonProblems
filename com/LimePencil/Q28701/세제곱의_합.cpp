#include <iostream>
#include <cmath>
using namespace std;

int main(void) {
    int n;
    cin >> n;
    int sum=0;
    for (int i = 1; i <= n; i++) {
        sum+=i;
    }
    cout << sum<<endl;
    
    cout << sum*sum<<endl;
    sum=0;
    for (int i = 1; i <= n; i++) {
        sum+=i*i*i;
    }
    cout << sum<<endl;
    
    return 0;
}