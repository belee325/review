//
// Created by Bummy on 12/7/2018.
//

#include "Person.h"
#include "ChatRoom.h"
Person::Person(const string &name) : name(name) {}

void Person::say(const string &message) const {
    room->broadcast(this->name, message);
}

void Person::pm(const string &who, const string &message) const {
    room->message(this->name, who,message);
}

bool Person::operator==(const Person &rhs) const {
    return name == rhs.name;
}

bool Person::operator!=(const Person &rhs) const {
    return !(rhs == *this);
}

void Person::receive(const string &origin, const string &message) {
    string formatted_message {origin + ": \"" + message + "\""};
    cout << "[" << name << "'s chat session]" << formatted_message << endl;
    chat_log.push_back(formatted_message);
}