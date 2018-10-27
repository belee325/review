#include "ring.h"
using namespace std;
int main(int argc, char **argv)
{
	ring<string> textring(3);
	textring.add("one");
	textring.add("two");
	textring.add("three");
	cout << textring << endl;
	textring.add("four");
	cout << textring << endl;
	
	ring<int> int_ring{1,2,3,4,5,6,7,8,9,10};
	cout << int_ring << endl;
	
	auto it = textring.begin();
	auto it2 = textring.end();
	while(it != it2){
		cout << *it << endl;
		it++;
	}
	
	for(auto val: textring){
		cout << val << endl;
	}
	return 0;
}
