#include <iostream>
#include <algorithm>
#include <fstream>
#include <tuple>
#include <sstream>
#include <memory>
#include <map>
#include <cmath>
#include <cstdint>
#include <functional>
#include <boost/signals2.hpp>
#include "Person.h"
#include "ChatRoom.h"
using namespace std;

//facilitates communication between different components
//components may go in and out of a system at anytime - so it makes no sense for them to have direct refs to one another
//we can have them all refer to some central component that facilitates communication

//event broker
struct EventData{
    virtual void print() const = 0;
};

struct PlayerScoredData : EventData{
    string player_name{};
    int goals_scored_so_far{};

    PlayerScoredData(const string &player_name, int goals_scored_so_far) : player_name(player_name),
                                                                           goals_scored_so_far(goals_scored_so_far) {}

    void print() const override {
        cout << player_name << " has scored! (their " << goals_scored_so_far << " goal!)\n";
    }
};

struct Game{
    boost::signals2::signal<void(EventData*)> events;
};


struct Player{
    string name;
    int goals_scored{0};
    Game& game;
    void score(){
        goals_scored++;
        PlayerScoredData ps {name, goals_scored};
        game.events(&ps);
    }
    Player(const string &name, Game &game) : name(name), game(game) {}
};

struct Coach{
    Game& game;

    Coach(Game &game) : game(game) {
        game.events.connect([](EventData* e){
           PlayerScoredData* ps  = dynamic_cast<PlayerScoredData*>(e);
           if(ps && ps->goals_scored_so_far<3){
               cout << "Coach says well done " << ps->player_name << "!\n";
           }
        });
    }
};



int main() {
    //in the case below, the chat room acts as a mediator between all the persons in the chat.
//    ChatRoom room;
//    Person john {"john"};
//    Person jane {"jane"};
//    room.join(&john);
//    room.join(&jane);
//    john.say("sup");
//    jane.say("hi john");
//    Person simon{"simon"};
//    room.join(&simon);
//    simon.say("hi everyone");
//    jane.pm("simon", "glad you found us simon");
//    std::cout << "Hello, World!" << std::endl;
    Game game;
    Player player{"sam", game};
    Coach coach{game};

    player.score();
    player.score();
    player.score();
    return 0;
}