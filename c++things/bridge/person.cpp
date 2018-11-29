//
// Created by Bummy on 11/26/2018.
//

#include "person.h"
#include <iostream>
class Person::PersonImpl{
public:
    void greet(Person* p);
};

void Person::PersonImpl::greet(Person* p){
    cout << p->name << endl;
}

Person::Person() : impl(new PersonImpl) {}

Person::~Person() {
    delete impl;
}

void Person::greet() {
    impl->greet(this);
}