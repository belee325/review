//
// Created by Bummy on 12/7/2018.
//

#include "Person.h"
#pragma once

struct ChatRoom {
    //might want to make this guy private
    vector<Person*> people;
    void broadcast(const string& origin, const string& message);
    void join(Person* p);
    void message(const string& origin, const string& who, const string& message);
};

