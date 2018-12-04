#include <iostream>
#include <string>
#include <sstream>
#include <functional>
using namespace std;
//decorators -  easily extending a functionality of an obj

struct Shape{
    virtual string str() const = 0;
};

struct Circle : Shape{
    float radius;
    Circle() {}

    Circle(float radius) : radius(radius) {}

    void resize(float factor){
        radius *= factor;
    }

    string str() const override {
        ostringstream oss;
        oss << "A circle of radius " << radius;
        return oss.str();
    }
};

struct Square:Shape{
    float side;
    Square(){}
    Square(float side) : side(side) {}
    string str() const override{
        ostringstream oss;
        oss << "A square of side " << side;
        return oss.str();
    }
};

//the struct below is a dynamic decorator

struct ColoredShape:Shape{
    Shape& shape;
    string color;

    ColoredShape(Shape &shape, const string &color) : shape(shape), color(color) {}

    string str() const override {
        ostringstream oss;
        oss << shape.str() << " has the color " << color;
        return oss.str();
    }
};

struct TransparentShape : Shape{
    Shape& shape;
    uint8_t transparency;

    TransparentShape(Shape &shape, uint8_t transparency) : shape(shape), transparency(transparency) {}

    string str() const override {
        ostringstream oss;
        oss<< shape.str() << " has " << static_cast<float>(transparency)/ 255.f * 100.f << "% transparency";
        return oss.str();
    }
};
//static decorator
//we gain access to whatever base class methods the decorator inheirted from
template <typename T>
struct ColoredShape2 : T{
    static_assert(is_base_of<Shape, T> :: value, "template arg must by a shape");

    string color;
    ColoredShape2(){}
    template<typename...Args>
    ColoredShape2(const string& color, Args ...args):T(std::forward<Args>(args)...),color{color} {}
    string str() const override{
        ostringstream oss;
        oss << T::str() << " has the color " << color;
        return oss.str();
    }
};

//functional decorator

struct Logger{
    function<void()> func;
    string name;

    Logger(const function<void()> &func, const string &name) : func(func), name(name) {}

    void operator()()const{
        cout << "entering " << name << endl;
        func();
        cout << "exiting " << name << endl;
    }

};

template<typename Func>
struct Logger2{
    Func func;
    string name;

    Logger2(const Func &func, const string &name) : func(func), name(name) {}

    void operator()()const{
        cout << "entering " << name << endl;
        func();
        cout << "exiting " << name << endl;
    }

};
template<typename Func> auto make_logger2(Func func, const string& name){
    return Logger2<Func>{func,name};
}

double add(double a, double b){
    cout << a << "+" << b << " = " << (a+b)<<endl;
    return a+b;
}

template<typename> struct Logger3;
template<typename R, typename ...Args>
struct Logger3<R(Args...)>{
    function<R(Args...)> func;
    string name;

    Logger3(const function<R(Args...)> &func, const string &name) : func(func), name(name) {}
    R operator() (Args...args){
        cout << "entering " << name << endl;
        R result = func(args...);
        cout << "exiting " << name << endl;
        return result;
    }
};
template <typename R, typename ...Args >
auto make_logger3(R (*func)(Args...), const string& name){
    return Logger3<R(Args...)>(
            function<R(Args...)>(func),
            name
            );
}

int main() {
    Square square{5};
    ColoredShape red_square{square ,"red"};
    TransparentShape t_square{red_square, 51};
    ColoredShape2<Circle> green_cirle{"green", 5};
    green_cirle.resize(2);
    cout << green_cirle.str() << endl;
    std::cout << square.str() << endl << red_square.str() << std::endl << t_square.str() << endl;
    Logger([](){cout << "Hello function wrapper"<<endl;}, "Hellofunction") ();
    auto log = make_logger2([](){cout << "Hello function wrapper using template"<<endl;}, "Hellofunction2");
    log();
    auto logged_add = make_logger3(add, "Add");
    auto result = logged_add(2,3);
    cout << result<<endl;
    return 0;
}