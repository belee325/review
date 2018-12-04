#include <iostream>
#include <string>
#include <map>
#include <vector>
using namespace std;

//flyweight is space optimization that lets us use less memory
//by externally storing the data associated with an obj
typedef uint32_t key;

//struct User{
//protected:
//    static map<key, string> names;
//    static key seed;
//
//};
//
//key User::seed{0};
//map<key, string> User::names{};

class FormattedText{
public:
    struct TextRange{
        int start, end;
        bool capitalize; // bold, italic .. .etc
        bool covers(int position) const{
            return position >= start && position <= end;
        }
    };
    TextRange& get_range(int start, int end){
        formatting.emplace_back(TextRange{start,end});
        return *formatting.rbegin();
    }
private:
    string plain_text;
    vector<TextRange> formatting;
public:
    FormattedText(const string &plain_text) : plain_text(plain_text) {}

    friend ostream &operator<<(ostream &os, const FormattedText &obj) {
        string s;
        for (int i = 0; i <obj.plain_text.length() ; ++i) {
            auto c = obj.plain_text[i];
            for(const auto& rng : obj.formatting){
                if(rng.covers(i) && rng.capitalize){
                    c = toupper(c);
                }
                s += c;
            }
        }
        return os << s;
    }
};



int main() {
    FormattedText ft{"This is awesome"};
    ft.get_range(0,4).capitalize = true;
    std::cout << ft << std::endl;
    return 0;
}