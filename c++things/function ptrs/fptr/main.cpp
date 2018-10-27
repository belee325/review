#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;
bool is_even(int num){
	return (num % 2 == 0)? true:false;
}
void print(int num){
	cout << "Hello: " << num << endl;
}

class increment{
private:
	int num;
public:
	increment(int num):num{num} {}
	int operator()(int num_in){
		return num_in += num;
	}
};

string make_string(int num){
	stringstream ss;
	ss << num;
	string ret = ss.str();
	return ret;
}

int main(int argc, char **argv)
{
	increment inc(5);
	void (*f_ptr)(int) = print;
	string (*f_ptr2)(int) = make_string;
	f_ptr(7);
	cout << f_ptr2(14) << endl;
	vector<int> v;
	for(int i =0; i < 11; i++){
		v.push_back(i);
	}
	transform(v.begin(), v.end(),v.begin(), increment(5));
	int num_even{count_if(v.begin(), v.end(), is_even)};
	cout << "even elements in vector: " << num_even << endl; 
	
	int num_even_lambda{count_if(v.begin(), v.end(), [](int x){
		return (x % 2 == 0)? true : false;})
	};
	cout << "even elements lambda in vector: " << num_even_lambda << endl;
	return 0;
}
