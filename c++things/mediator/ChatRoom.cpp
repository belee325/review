//
// Created by Bummy on 12/7/2018.
//

#include "ChatRoom.h"
#include <algorithm>

void ChatRoom::broadcast(const string &origin, const string &message) {
    for(auto p : people){
        if(p->name != origin){
            p->receive(origin, message);
        }
    }
}

void ChatRoom::join(Person *p) {
    string join_msg = p->name + " has joined the room.\n";
    broadcast("room", join_msg);
    p->room = this;
    people.push_back(p);
}

void ChatRoom::message(const string &origin, const string &who, const string &message) {
    auto target = std::find_if(people.begin(), people.end(),
            [&](const Person* p){
        return p->name == who;
    });
    if(target!=people.end()){
        (*target)->receive(origin,message);
    }
}
