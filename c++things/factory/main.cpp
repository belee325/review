#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include "HotDrinkFactory.h"
using namespace std;
//using namespace boost;

//where its relevant - if we wanted to create both cartesian coords and polar coord points
//

enum class PointType{
    cartesian,
    polar
};

class Point{

public:
    float x,y;
    Point(float x,float y) : x(x), y(y) {}
    //these are factory methods - we can put these into a factory itself
    static Point NewCartesian(float x, float y){
        return {x,y};
    }
    static Point NewPolar(float r, float theta){
        return {r*cos(theta), r*sin(theta)};
    }


    friend ostream &operator<<(ostream &os, const Point &point) {
        os << "x: " << point.x << " y: " << point.y;
        return os;
    }
};

struct PointFactory{
    //we cant do the below since the constructor for Point is private. making this a friend class violates OCP
    //or we can make constructor public
    //or we can make this factory an inner factory
    static Point NewCartesian(float x, float y){
        return {x,y};
    }
    static Point NewPolar(float r, float theta){
        return {r*cos(theta), r*sin(theta)};
    }

};

struct Person
{
    int id;
    string name;
    Person(int id,string name) : id(id), name(name) {}

    friend ostream &operator<<(ostream &os, const Person &person) {
        os << "id: " << person.id << " name: " << person.name;
        return os;
    }
};

class PersonFactory
{
    int unique_id;
public:
    PersonFactory(){
        unique_id = 0;
    };
    Person create_person(const string& name)
    {
        Person p{unique_id, name};
        unique_id++;
        return p;
    }
};

int main() {
//    auto p = Point::NewPolar(5.0, 45);
//    std::cout << "Hello, World!" << std::endl;
//    cout<<p<<endl;
//    TeaFactory tf;
//    unique_ptr<Drink> a  = tf.make();
//    a->prepare(200);
    HotDrinkFactory df;
    auto c = df.make_drink("Tea");
    c->prepare(100);
    auto d = df.make_drink("Coffee");
    PersonFactory p;
    auto e = p.create_person("Me");
    cout << e;

    return 0;
}