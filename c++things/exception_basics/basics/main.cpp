#include <iostream>
using namespace std;

class CanGoWrong{
public:
    CanGoWrong(){
        char *p_mem = new char[999999999999999];
        delete [] p_mem;
    }
};

void might_go_wrong(){
    bool error =true;
    if(error){
        throw 8;
    }
}

int main(int argc, char **argv)
{
//    try{
//        might_go_wrong();
//    }
//    catch(int &e){
//        cout<<"something went wrong " << endl <<  "Error code " << e << endl;
//    }
//    
//    cout<< "still running." << endl;
    try{
        CanGoWrong wrong;
    }
    catch(bad_alloc &e){
        cout<< "Something went wrong " << e.what();
    }
    return 0;
}
