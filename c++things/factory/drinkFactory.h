//
// Created by Bummy on 11/23/2018.
//
#include "drink.h"
#ifndef FACTORY_DRINKFACTORY_H
#define FACTORY_DRINKFACTORY_H
struct drinkFactory{ // abstract factory
    virtual unique_ptr<Drink> make() const = 0;
};

struct TeaFactory:drinkFactory{
    unique_ptr<Drink> make() const override {
        return make_unique<Tea>();
    }
};

struct CoffeeFactory:drinkFactory{
    unique_ptr<Drink> make() const override {
        return make_unique<Coffee>();
    }
};
#endif //FACTORY_DRINKFACTORY_H
