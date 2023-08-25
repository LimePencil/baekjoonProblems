#include<iostream> 
#include<string>
using namespace std; 
int main() 
{ 
    string s;
    cin >> s;
    if (s=="M"){
        cout << "MatKor\n";
    }
    else if (s=="W"){
        cout << "WiCys\n";
    }
    else if (s=="C"){
        cout << "CyKor\n";
    }
    else if (s=="A"){
        cout <<"AlKor\n";
    }
    else{
        cout << "$clear\n";
    }


    return 0;
}