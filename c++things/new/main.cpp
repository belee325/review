#include <iostream>
#include <cstring>
using namespace std;
int main() {
    char arr[] = {'h', 'e', 'l', 'l','o'};
    char* arr2 = new char(5);
    arr2 = arr;
    memset(arr2, 0x0, 5);
    if(*(int*)arr){
        arr[0] = 'w';
    }
    cout << arr <<endl;
    return 0;
}