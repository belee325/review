#include <iostream>
#include <memory>
#include <fstream>
#include <sstream>
#include <vector>
#include <tuple>
using namespace std;
//using namespace boost;
//motivation - some objs are simple enough to create with a single constructor call, others not so much
//Having an obj with 10 cstr is not produictive

//builder - when piecewise obj construction is compicated, provide an API for doing it succintly

struct HtmlElement{
    string name, text;
    vector<HtmlElement> elements;
    const size_t  indent_size =2;

    HtmlElement(const string &name, const string &text) : name(name), text(text) {}

    HtmlElement() {}

    string str(int indent = 0) const{
        ostringstream oss;
        string i (indent_size*indent, ' ');
        oss << i << "<" << name << ">" << endl;
        if(text.size() > 0){
            oss << string(indent_size*(indent + 1), ' ') << text << endl;
        }
        for (const auto& e:elements){
            oss << e.str(indent + 1);
        }
        oss << i << "</" << name << ">" << endl;
        return oss.str();
    }
};


struct HtmlBuilder{
    HtmlElement root;
    HtmlBuilder(string root_name){
        root.name = root_name;
    }
    void add_child(string child_name, string child_text){
        HtmlElement e{child_name, child_text};
        root.elements.emplace_back(e);
    }

    string str() const {
        return root.str();
    }
};



int main() {
    HtmlBuilder b{"ul"};
    b.add_child("li", "Hello");
    b.add_child("li", "World");
    std::cout << b.str() << std::endl;
    return 0;
}