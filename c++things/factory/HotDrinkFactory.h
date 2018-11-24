//
// Created by Bummy on 11/24/2018.
//
#include "drinkFactory.h"
#include <map>
#include <memory>
using namespace std;
#ifndef FACTORY_HOTDRINKFACTORY_H
#define FACTORY_HOTDRINKFACTORY_H
class HotDrinkFactory{
    map<string, unique_ptr<drinkFactory>> hot_factories;
public:
    HotDrinkFactory(){
        hot_factories["Coffee"] = make_unique<CoffeeFactory>();
        hot_factories["Tea"] = make_unique<TeaFactory>();
    }
    unique_ptr<Drink> make_drink(const string& name){
        auto drink = hot_factories[name]->make();
        drink->prepare(200);
        return drink;
    }

};

#endif //FACTORY_HOTDRINKFACTORY_H
