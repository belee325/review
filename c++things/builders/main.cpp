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
    //we can make this into a fluent builder by changing the
    //return type to a reference or a pointer of the builder
//    void add_child(string child_name, string child_text){
//        HtmlElement e{child_name, child_text};
//        root.elements.emplace_back(e);
//    }

    HtmlBuilder& add_child(string child_name, string child_text){
        HtmlElement e{child_name, child_text};
        root.elements.emplace_back(e);
        return *this;
    }

    string str() const {
        return root.str();
    }

    static HtmlBuilder build(string root_name){
        return {root_name};
    }
};

////////////////////////////////////////////////////////////////////////////////////////////////////////////
//groovy style builder

struct Tag{
    string name, text;
    vector<Tag> children;
    vector<pair<string,string>> attributes;
protected:
public:
    Tag(const string &name, const string &text) : name(name), text(text) {}

    Tag(const string &name, const vector<Tag> &children) : name(name), children(children) {}
};

struct P: Tag{
    P(const string &text) : Tag("P", text) {}
    P(initializer_list<Tag> children)
    : Tag{"P", children}{}
};

struct IMG:Tag{
    explicit IMG(const string& url) : Tag{"IMG", ""}{
        attributes.emplace_back(make_pair("src", url));
    }
};
////////////////////////////////////////////////////////////////
//facade builder?
class PersonBuilder;
class Person{
    string street_address, post_code, city;
    string company_name, position;
    int income{0};
    static PersonBuilder create();
    friend class PersonBuilder;
    friend class PersonJobBuilder;
    friend class PersonAddressBuilder;
};
#include <string>
#include <utility>
#include <vector>
#include <ostream>
using namespace std;

class CodeBuilder
{
    vector<pair<string,string>> fields;
    string class_name;
public:
    CodeBuilder(const string& class_name): class_name{class_name} {}

    CodeBuilder& add_field(const string& name, const string& type)
    {
        fields.emplace_back(type,name);
        return *this;
    }

    friend ostream& operator<<(ostream& os, const CodeBuilder& obj)
    {
        os << "Class " << obj.class_name << '\n'<< "{\n";
        for(auto& f: fields){
            os << "\t" << f.first << " " << f.second << ";\n";
        }
        os << "};";
        return os;
    }
};
int main() {
    HtmlBuilder b{"ul"};
    b.add_child("li", "Hello").add_child("li", "World");
    //b.add_child("li", "World");
    std::cout << b.str() << std::endl;
    return 0;
}