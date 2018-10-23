#ifndef MYEXCEPTION_H
#define MYEXCEPTION_H
#include <exception>

class MyException: public std::exception {
public:
    MyException() = default;
    ~MyException() = default;
    virtual const char* what() const throw(){
        return "This is an error code";
    }
};

#endif // MYEXCEPTION_H
