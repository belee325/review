//
// Created by Bummy on 11/26/2018.
//

#ifndef BRIDGE_PERSON_H
#define BRIDGE_PERSON_H
#include <string>
using namespace std;
class Person {
public:
    string name;
    class PersonImpl;
    //in this case, the bridge is the impl class
    //here we want to avoid exposing the details of the implementation
    PersonImpl* impl;

    Person();
    ~Person();

    void greet();
};


#endif //BRIDGE_PERSON_H
