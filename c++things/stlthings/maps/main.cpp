#include <iostream>
#include <map>

using namespace std;

class Person{
	
	friend bool operator< (const Person &lhs, const Person &rhs){
		return (lhs.name == rhs.name) ? (lhs.name < rhs.name) : (lhs.age < rhs.age);
	}
	
	friend bool operator==(const Person &lhs, const Person &rhs){
		return (lhs.age == rhs.age) && (lhs.name == rhs.name);
	}
	
	friend ostream& operator<<(ostream &os, const Person &p){
		os << p.name << " " << p.age << endl;
		return os;
	}
public:
	string name;
	int age;
	Person(): Person{"no name", 1000}{}
	Person(string name, int age): name{name}, age{age} {}
	void print() const{
		cout << "Name: " << name << endl << "Age: " << age << endl;
	}
	
	ostream& operator<<(ostream &os){
		os << name << " " << age << endl;
		return os;
	}
};


int main(int argc, char **argv)
{
	map<int, Person> m;
	m.emplace(1,Person("James", 15));
	m.emplace(2, Person());
	auto it = m.begin();
	while(it != m.end()){
		cout << it->first << endl;
		it->second.print();
		cout << endl;
		//cout << it->second;
		it++;
	}
	Person a{"a",1};
	Person b{"b",2};
	cout << boolalpha << (a < b);
	map<Person, int> rev_m;
	rev_m[a] = 1;
	rev_m[b] = 2;
	auto it_rev = rev_m.begin();
	while(it_rev != rev_m.end()){
		cout << it_rev->first << endl;
		it_rev++;
	}
	return 0;
}
