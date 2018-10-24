#include <iostream>
#include <cstring>
#include <vector>
using namespace std;

class Test{
public:
	int id;
	char* name;
	friend std::ostream& operator<<(ostream& os, const Test &t){
		os << "ID: " << t.id << "Name :" << t.name << endl;
		return os;
	}
	friend void swap(Test& lhs, Test& rhs){
		cout << "calling swap" << endl;
		using std::swap;
		swap(lhs.id, rhs.id);
		swap(lhs.name,rhs.name);
	}
	
	Test(int id, char* name): id{id}, name{name} {
		cout << "overloaded constructor" << endl;
		//cout << id << name << endl;
	}
	
	Test() : Test{0, "No Name"} {cout << "Default constructor" << endl;}
	
	Test(Test&& other): id{other.id}, name{other.name}{
		cout << "move construct" << endl;
		other.name = nullptr;
	}
	
	Test(const Test &other): id{other.id}{
		cout << "Copy constructor" << endl;
		delete [] name;
		name = new char[strlen(other.name)+1];
		strcpy(name,other.name);
	}
	
	Test& operator=(Test other){
		//notice that we pass by value here so the copy constructor gets called
		swap(*this, other);
		return *this;
	}
//	Test& operator=(const Test &other){
//		cout << "copy assignment" << endl;
//		if(this == &other){
//			return *this;
//		}
//		id = other.id;
//		delete [] name;
//		name = new char[strlen(other.name) + 1];
//		strcpy(name,other.name);
//		return *this;
//	}
//	
//	Test& operator=(Test &&other){
//		cout << "Move assigment" << endl;
//		if(this == &other){
//			return *this;
//		}
//		this->id = other.id;
//		delete [] name;
//		name = new char[strlen(other.name) + 1];
//		strcpy(name,other.name);
//		other.name = nullptr;
//		return *this;
//	}
	~Test(){
		cout << "Destructor" << endl;
	}
	void print(){
		cout << "id: " << id << endl << "Name: " << name << endl; 
	}
};

Test make_new_test(int id, string name){
	char* new_name = new char[strlen(name.c_str()) + 1];
	strcpy(new_name, name.c_str());
	return Test(id, new_name);
}

int main(int argc, char **argv)
{
	Test t{1, "first test"};
	Test t2{2, "second test"};
	cout << t << t2 << endl;
	t.print();
	t2.print();
	Test t3 {t2};
	t2 = t;
	t2.print();
	t2 = make_new_test(2,"second test from method");
	t2.print();
	t3.print();
	
	vector<Test> test_vec{};
	test_vec.push_back(Test{1, "first in vec"});
	cout << "added first" << endl;
	test_vec.push_back(Test{2, "second in vec"});
	cout << "added second" << endl;
	test_vec.push_back(Test{3, "third in vec"});
	cout << "added third" << endl;
	test_vec.push_back(Test{4, "fourth in vec"});
	cout << "added fourth" << endl;
	test_vec.push_back(Test{5, "fifth in vec"});
	cout << "added fifth" << endl;
	
	return 0;
}