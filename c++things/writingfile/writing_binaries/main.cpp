#include <iostream>
#include <fstream>

using namespace std;

#pragma pack(push, 1)
struct Test{
	char name[50];
	int num;
	double weight;
};
#pragma pack(pop)

int main(int argc, char **argv)
{
	Test p {"me", 24, 170.1};
	string file_name{"../Test.bin"};
	ofstream file_out{file_name, ios::binary};
	if(!file_out){
		cout << "Something went wrong" << endl;
	}else{
		file_out.write(reinterpret_cast<char *>(&p), sizeof(Test));
		file_out << &p << endl;
		file_out.close();
	}
	
	Test q;
	
	ifstream file_in{file_name, ios::binary};
	if(!file_in){
		cout << "Cant read file" << endl;
	} else{
		file_in.read(reinterpret_cast<char *>(&q), sizeof(Test));
		file_in.close();
	}
	cout << "Name: " << q.name << endl << "Num: " << q.num << endl << "Weight: " << q.weight << endl;
	
	
	return 0;
}
