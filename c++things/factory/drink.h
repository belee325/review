//
// Created by Bummy on 11/23/2018.
//
#ifndef FACTORY_DRINK_H
#define FACTORY_DRINK_H
#include <iostream>
#include <memory>
using namespace std;

struct Drink{
    virtual ~Drink() = default;
    virtual void prepare(int volume) = 0;

};

struct Tea : Drink {
    void prepare(int volume) override{
        cout << "Take tea bag, boil water, pour" << volume
        <<"ml, add some lemon \n" << endl;
    }
};

struct Coffee : Drink{
    void prepare(int volume) override {
        cout << "Grind beans, boil water, pour" << volume << "ml, add cream" <<endl;
    }
};
#endif //FACTORY_DRINK_H
