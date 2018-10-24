#ifndef TEST_H
#define TEST_H
#include <iostream>
#include <string>
using namespace std;

template<typename T, typename K>
class Test
{
private:
	T id;
	K name;
public:
	Test(T id, K name) : id{id}, name{name} {}
	~Test() = default;
	void print(){
		cout << id << " "<< name << endl;
	}

};

#endif // TEST_H
