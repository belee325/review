#include <iostream>
#include <list>
using namespace std;
int main(int argc, char **argv)
{
	list<int> l;
	
	
	l.push_back(1);
	l.push_back(2);
	l.push_front(3);
	auto it = l.begin();
	while(it != l.end()){
		cout << *it << endl;
		it++;
	}
}
