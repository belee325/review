#include <iostream>
#include <string>
#include <memory>
#include <boost/serialization/serialization.hpp>
#include <boost/archive/text_iarchive.hpp>
#include <boost/archive/text_oarchive.hpp>

using namespace std;
using namespace boost;

struct Address{
    string street, city;
    int suite;
    Address() {}
    Address(const string &street, const string &city, int suite) : street(street), city(city), suite(suite) {}
    Address(const Address& other) : street{other.street}, city{other.city}, suite{other.suite} {}
    friend ostream &operator<<(ostream &os, const Address &address) {
        os << "street: " << address.street << " city: " << address.city << " suite: " << address.suite;
        return os;
    }
private:
    friend class serialization::access;
    template <class archive>
    void serialize(archive& ar, const unsigned version){
        ar& street;
        ar& city;
        ar& suite;
    }
};

struct Contact{
    string name;
    Address* address;
    Contact() {}
    Contact(const string &name, Address* address) : name(name), address(address) {}

    Contact(const Contact& other):
    name{other.name}, address{new Address{*other.address}}
    {}
    ~Contact(){
        delete address;
    }
    friend ostream &operator<<(ostream &os, const Contact &contact) {
        os << "name: " << contact.name << " address: " << *contact.address;
        return os;
    }

private:
    friend class serialization::access;
    template <class archive>
            void serialize(archive& ar, const unsigned version){
                ar& name;
                ar& address;
            }
};

struct EmployeeFactory{
    static unique_ptr<Contact> new_main_office_employee(const string& name, int suite){
        static Contact p{"", new Address{"123 east drive", "London", 0}};
        return new_employee(name, suite, p);
    }
private:
    static unique_ptr<Contact> new_employee(const string& name, int suite, Contact& prototype){
        auto result = make_unique<Contact>(prototype);
        result->name = name;
        result->address->suite = suite;
        return result;
    }
};

//prototype via serialization




//prototypes - partially or fully realized object that you clone/copy
int main() {
    //Contact john{"john doe", new Address{"123 east dr", "london" ,1523}};
    //Contact jane{"jane doe", Address{"123 east dr", "london" ,1522}};
    // how should we structure so making a whole bunch is easier to do
    //we can try:
//    Contact jane{john};
//    jane.name ="Jane smith";
//    jane.address->suite=1522;
//    cout<< john << endl << jane << endl;
    //now the above works since we are using Address object as value
    //it will not work if we tried using Address as a pointer - need to implement deepcopy/\
//  we can do the same with a prototype factory
//    auto john = EmployeeFactory::new_main_office_employee("Me", 1552);
 //   cout << *john << endl;
    std::cout << "Hello, World!" << std::endl;
    auto clone = [](const Contact& c){
        ostringstream oss;
        archive::text_oarchive oa(oss);
        oa << c;
        string s = oss.str();
        cout << s << endl;

        istringstream iss;
        archive::text_iarchive ia(iss);
        Contact result;
        ia >> result;
        return result;
    };
    auto john = EmployeeFactory::new_main_office_employee("John", 123);
    auto jane = clone(*john);
    return 0;
}