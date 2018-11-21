#include <iostream>
#include <cstdio>
#include <cstring>
#include <fstream>
#include <boost/lexical_cast.hpp>

using namespace std;
using namespace boost;

//exploring SOLID design principles


///////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Single responsibility


struct Journal {
    string title;
    vector<string> entries;

    Journal(const string &title) : title{title} {}

    void add_entry(const string &entry) {
        static int count = 1;
        entries.push_back("Entry " + lexical_cast<string>(count++) + ":" + entry);
    }

    //This isnt the best since we are giving Journal class an extra responsiblity - we could make another class that
    //handles the saving function and just pass in the journal class as a parameter
    void save(const string &file_name) {
        ofstream os(file_name);
        for (auto &e: entries) {
            os << e << endl;
        }
        os.close();
    }
};

struct PersistenceManager {
    //cutting some corners here since we made journal members public instead of private
    //should make getters or make friend method of Journal
    void save(const Journal &j, const string &file_name) {
        ofstream os(file_name);
        for (auto &e: j.entries) {
            os << e << endl;
        }
        os.close();
    }
};
///////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Open closed - the point being we dont want to jump into code thats already finished,
//but still leave it open for extension

enum class Color {
    red, green, blue
};
enum class Size {
    small, medium, large
};

struct Product {
    string name;
    Color color;
    Size size;
};


//we have the filter that looks at colors, but what if we wanted to add more filters looking at size??
struct ProductFilter {
    vector<Product *> by_color(vector<Product *> items, Color color) {
        vector<Product *> result;
        for (auto &i : items) {
            if (i->color == color) {
                result.push_back(i);
            }
        }
        return result;
    }
};

template<typename T>
struct Specification {
    virtual bool is_satisfied(T *item) = 0;
};

template<typename T>
struct Filter {
    virtual vector<T *> filter(vector<T *> items, Specification<T> &spec) = 0;
};

// we use the specification pattern
struct BetterFilter : Filter<Product> {
    vector<Product *> filter(vector<Product *> items, Specification<Product> &spec) override {
        vector<Product *> result;
        for (auto &item:items) {
            if (spec.is_satisfied(item)) {
                result.push_back(item);
            }
        }
        return result;
    }
};

struct ColorSpecification : Specification<Product> {
    Color color;

    ColorSpecification(Color color) : color(color) {}

    bool is_satisfied(Product *item) override {
        return item->color == color;
    }
};

struct SizeSpecification : Specification<Product> {
    Size size;

    SizeSpecification(Size size) : size(size) {}

    bool is_satisfied(Product *item) override {
        return item->size == size;
    }
};

template <typename T> struct AndSpecification : Specification<T>{
    Specification<T>& first;
    Specification<T>& second;

    AndSpecification(Specification<T> &first, Specification<T> &second) : first(first), second(second) {}

    bool is_satisfied(T *item) override {
        return first.is_satisfied(item) and second.is_satisfied(item);
    }

};
///////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Liskov substitution - sub classes should be immediately subsitutable with the base class
class Rectangle{
protected:
    int width, height;
public:
    Rectangle(int width, int height) : width(width), height(height) {}

    int getWidth() const {
        return width;
    }

    void setWidth(int width) {
        Rectangle::width = width;
    }

    int getHeight() const {
        return height;
    }

    void setHeight(int height) {
        Rectangle::height = height;
    }
    int area() const {return width * height};
};
//What would break it is if we overrode getters for a derived class - say a sqaure then we would get the wrong
//results for the area method

///////////////////////////////////////////////////////////////////////////////////////////////////////////////
//interface segregation

struct Document{

};

struct IMachine{
    virtual void print(Document& doc) = 0;
    virtual void scan(Document& doc) = 0;
    virtual void fax(Document& doc) = 0;
};

struct IPrinter{
    virtual void print(Document& doc) = 0;
};

struct IScanner{
    virtual void scan(Document& doc) = 0;
};

struct IFax{
    virtual void fax(Document& doc) = 0;
};


struct Scanner: IScanner{
    //scanner only expects to scan things, what to do about the other two methods?
    //In this case, we have an interface that is too large
    //We can solve the issue by having three separate interfaces

    void scan(Document &doc) override {
        //"scan" the doc and do something with it
    }
};

//if we wanted multiple funciontalities, we can make more interfaces thru multiple inheritance

struct IMachine: IPrinter, IFax{
    void print(Document &doc) override {
        //do things
    }

    void fax(Document &doc) override {
        //do things
    }
};
///////////////////////////////////////////////////////////////////////////////////////////////////////////////

//Dependency inversion
//High level modules shouldnt rely on low level modeules
//both should rely on abstractions

//Abstractions shouldnt depend on details
//details should depend on abstractions



int main() {
//    Journal j("diary");
//    j.add_entry("I ate today");
//    j.add_entry("I slept");
//    j.save("diary.txt");
    BetterFilter bf{};
    Product apple{"Apple", Color::green, Size::small};
    Product tree{"Tree", Color::green, Size::large};
    Product house{"House", Color::red, Size::large};
    vector<Product *> items{&apple, &tree, &house};
    ColorSpecification s{Color::green};
    SizeSpecification s2{Size::large};
    AndSpecification<Product> s3{s,s2};
    vector<Product *> result = bf.filter(items, s);
    vector<Product *> result2 = bf.filter(items, s2);
    vector<Product *> result3 = bf.filter(items, s3);

    for (auto &i: result) {
        cout << i->name << " is green" << endl;
    }

    for (auto &i: result2) {
        cout << i->name << " is large" << endl;
    }

    for (auto &i: result2) {
        cout << i->name << " is large and green" << endl;
    }

    std::cout << "Finished running" << std::endl;
    return 0;
}