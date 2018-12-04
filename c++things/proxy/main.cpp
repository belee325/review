#include <iostream>
#include <string>

using namespace std;

//proxies are interfaces for accessing a particular resource
//property proxy below
template <typename T>
struct Property{
    T value;
    Property(T value){
        *this = value;
    }

    operator T(){
        return value;
    }

    T operator=(T new_value){
        cout << "assignment\n";
        value = new_value;
        return value;
    }
};

struct Creature{
    Property<int> agility{10};
    Property<int> strength{15};
};
//virtual proxy

struct Image{
    virtual void draw() = 0;
};

struct Bitmap : Image{
    Bitmap(const string& filename){
        cout << "loading bmp from " << filename << endl;
    }
    //in this case, we would like to avoid calling void when a bitmap obj hasnt been created
    void draw() override{
        cout << "drawing bmp\n";
    }
};
//virtual proxy can help
//below we have a ptr to a Bitmap obj initialized to null
//then we override the draw method to make sure that we initialzed the bitmap before we call
struct LazyBitmap : Image{
private:
    string filename;
    Bitmap* bmp {nullptr};
public:
    LazyBitmap(const string &filename) : filename(filename) {}
    void draw() override{
        if(!bmp){
            bmp = new Bitmap(filename);
        }
        bmp->draw();
    }
};
//communication proxy



int main() {
    Creature c;
    c.agility = 15;
    c.strength = 5;
    std::cout << "Hello, World!" << std::endl;
    return 0;
}