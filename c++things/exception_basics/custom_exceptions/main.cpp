#include <iostream>
#include "MyException.h"
using namespace std;
void throw_custom_error(){
    throw MyException();
}

int main(int argc, char **argv)
{
    try{
        throw_custom_error();
    }
    catch(MyException &e){
        cout << "Error code " << e.what() << endl;
    }
	printf("hello world\n");
	return 0;
}
