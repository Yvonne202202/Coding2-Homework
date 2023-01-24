//
//  main.cpp
//  week1
//
//  Created by 王钰 on 17/01/2023.
//

#include <iostream>
#include <math.h>
#include "some_objects.hpp"
using namespace std;

myClass yvonnes;
float myValue = 0;

int main(int argc, const char * argv[]) {
    for(int i=0; i<10; i++){
        myValue = i * yvonnes.myFounc(10, 3.1415);
        cout<<myValue<<endl;
    }
    return 0;
}
