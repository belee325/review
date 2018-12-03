#include <iostream>
#include <string>
#include <vector>

using namespace std;
//treat individual and aggregate objects uniformly

//the interface below allows us to use circles and groups in the same manner
struct GraphicObject{
    virtual void draw() = 0;
};

struct Circle:GraphicObject{
    void draw(){
        cout << "circle" << endl;
    }
};

struct Group : GraphicObject{
    string name;
    vector<GraphicObject*> objs;
    Group(const string &name) : name{name}{};
    void draw() override{
        cout << "Group " << name << " contains:" << endl;
        for(auto& o: objs){
            o->draw();
        }
    }
};
template <typename Self>
struct SomeNeurons{
    template <typename T>
    void connect_to(T& other){
        for(auto& from: *static_cast<Self*>(this)){
            for(auto& to: other){
                from.out.push_back(&to);
                to.in.push_back(&from);
            }
        }
    }
};
//this is bad but w/e
struct Neuron : SomeNeurons<Neuron>{
    vector<Neuron*> in, out;
    unsigned int id;

    Neuron() {
        static unsigned int id{1};
        this->id = id++;
    }
    Neuron* begin(){
        return this;
    }

    Neuron* end(){
        return this+1;
    }

    friend ostream &operator<<(ostream &os, const Neuron &obj) {
        for(auto n: obj.in){
            os << n->id << "\t-->\t[" << obj.id << "]" << endl;
        }

        for(auto n: obj.out){
            os << "[" << obj.id<< "]\t-->\t" << n->id << endl;
        }
        return os;
    }
};

struct NeuronLayer:vector<Neuron>, SomeNeurons<NeuronLayer>{

    NeuronLayer(int count){
        while(count-- > 0){
            emplace_back(Neuron());
        }
    }

    friend ostream &operator<<(ostream &os, const NeuronLayer &obj) {
        for(auto n:obj){
            os << n;
        }
        return os;
    }
};

int main() {
//    Group root("root");
//    Circle c1, c2;
//    root.objs.push_back(&c1);
//    root.objs.push_back(&c2);
//    Group subgroup("subgroup");
//    root.objs.push_back(&subgroup);
//    subgroup.objs.push_back(&c1);

//    root.draw();
    Neuron n1,n2;
    //n1.connect_to(n2);
    //cout << n1 << n2 <<endl;
//lets say we wanted to connect layers as well
//then we could have layer-layer, layer-neuron, neuron-layer, neuron-neuron types of connections
//we want a single interface so we dont have to worry about these states
    NeuronLayer nl{5};
    n1.connect_to(nl);
    nl.connect_to(n2);
    std::cout << "Hello, World!" << std::endl;
    cout << n1 <<  n2 << endl;
    return 0;
}