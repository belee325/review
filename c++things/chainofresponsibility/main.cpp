#include <iostream>
#include <string>
#include <vector>
#include <boost/signals2.hpp>
using namespace std;
using namespace boost::signals2;
//click a graphical elem on a form - who handles the click??
//the button can handle it, the underlying group box can handle it, or the underlying window can handle it
//a chain of components who all get a chance to process a command or a query
//optionally having default processing implementation and an ability to terminate the processing chain
struct Query{
    string creature_name;
    enum Argument{attack, defense} argument;
    int result;
    Query(const string& creature_name, Argument argument, int result) : creature_name{creature_name},
                                                                        argument(argument), result(result) {};

};


struct Game{
    //mediator
    boost::signals2::signal<void(Query&)> queries;
};


//the example below is a classic and rather artificial chain of responsibility
struct Creature{
    Game& game;
    string name;
    int attack, defense;

    Creature(Game &game, const string &name, int attack, int defense) : game(game), name(name), attack(attack),
                                                                        defense(defense) {}

    friend ostream &operator<<(ostream &os, const Creature &creature) {
        os << "name: " << creature.name << " attack: " << creature.get_attack() << " defense: " << creature.defense;
        return os;
    }

    int get_attack() const{
        Query q{name, Query::Argument::attack, attack};
        game.queries(q);
    }
};

class CreatureModifier{
public:
    CreatureModifier* next{nullptr};
    CreatureModifier(Creature &creature, Game &game) : creature(creature), game(game) {}
    void add(CreatureModifier *cm){
        if(next){
            next->add(cm);
        }
        else{
            next = cm;
        }
    }
    virtual ~CreatureModifier() = default;
    virtual void handle(){
        if(next){
            next->handle();
        }
    }
protected:
    Creature& creature;
    Game& game;
};

class DoubleAttackModifier: public CreatureModifier{
    connection conn;
public:
    DoubleAttackModifier(Creature& creature, Game& game) : CreatureModifier(creature, game) {
        conn = game.queries.connect([&](Query& q){
            if(q.creature_name == creature.name && q.argument == Query::Argument::attack){
                q.result*=2;
            }
        });
    }
    ~DoubleAttackModifier() {conn.disconnect();}
    void handle() override{
        creature.attack *= 2;
        CreatureModifier::handle();
    }
};

class IncreaseDefenseModifier : public CreatureModifier{
public:
    IncreaseDefenseModifier(Creature &creature, Game& game) : CreatureModifier(creature, game) {}
    void handle() override{
        if(creature.attack <= 2){
            creature.defense++;
            CreatureModifier::handle();
        }
    }
};
//if we wanted to stop the propogation of the bonuses, we can just stop the base call of the handle method
class NoBonusModifier:public  CreatureModifier{
public:
    NoBonusModifier(Creature &creature, Game& game) : CreatureModifier(creature, game) {}

    void handle() override {
    }
};

//event broker

int main() {
    Game game;
    Creature goblin{game, "Goblin", 1, 1};

    cout << goblin << endl;
    {
        DoubleAttackModifier temp_boost{goblin, game};
        cout << goblin << endl;
    }

    cout << goblin << endl;

//    CreatureModifier root{goblin,game};
//   // root.add(new NoBonusModifier{goblin});
//    root.add(new DoubleAttackModifier{goblin,game});
//    cout << goblin <<endl;
//    root.add(new IncreaseDefenseModifier{goblin,game});
//    root.handle();
//    cout << goblin <<endl;
    std::cout << "Hello, World!" << std::endl;
    return 0;
}