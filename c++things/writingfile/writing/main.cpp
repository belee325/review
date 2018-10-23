#include <iostream>
#include <fstream>
using namespace std;
int main(int argc, char **argv)
{
	ofstream f {"../test.txt"};
	if(!f){
		cout << "something went wrong";
	}
	else{
		f << "writing a line to file" << endl;
		f << "writing a second line to file" << endl;
		f << "writing a third line to file" << endl;
		f << "writing a fourth line to file" << endl;
		f.close();
	}
	ifstream in_file {"../test.txt"};
	if(!in_file){
		cout << "Couldnt open file" << endl;
	}
	else{
		string line;
		while(getline(in_file, line)){
			cout << line << endl;
		}
	}
	return 0;
}
