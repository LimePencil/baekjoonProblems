#include <iostream>
using namespace std;
int main(){
    int max;
    int mel;
    int a,b,c,d,e,f;
    cin>>a>>b>>c;
    cin>>d>>e>>f;
    max=a*3+b*20+c*120;
    mel=d*3+e*20+f*120;
    if (max>mel){
        cout<<"Max"<<endl;
    }
    else if (max==mel){
        cout<<"Draw"<<endl;
    }
    else{
        cout<<"Mel"<<endl;
    }
    return 0;
}