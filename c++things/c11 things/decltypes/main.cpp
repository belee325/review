#include <iostream>
#include <typeinfo>
using namespace std;

template <class T, class K>
auto test(T val1, K val2) -> decltype(val1 + val2) {
	return val1 + val2;
}

int main(int argc, char **argv)
{
	string value;
	decltype(value) name= "bob";
	cout << typeid(value).name() << endl;
	cout << name << endl;
	cout << test(4,4) << endl;
	return 0;
}
