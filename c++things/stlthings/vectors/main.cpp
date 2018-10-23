#include <iostream>
#include <vector>
#include <iterator>
using namespace std;
int main(int argc, char **argv)
{
	vector<string> v(5, "DEF");
	vector<int> v2;
	cout << sizeof(v2) << endl;
	v[3] = "A";
	v.push_back("one");
	cout << v[3]<< endl;
	for(auto &s: v){
		cout << s << endl;
	}
	cout << "iterator version" << endl;
	auto it = v.begin();
	while(it != v.end()){
		cout << *it << endl;
		it++;
	}
	return 0;
}