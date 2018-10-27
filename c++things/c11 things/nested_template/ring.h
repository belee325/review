#ifndef RING_H
#define RING_H
#include <iostream>
#include <initializer_list>
using namespace std;
template<typename T>
class ring
{
	friend ostream& operator<<(ostream &os, ring &r){
		cout << "[ ";
		for(int i =0; i < r.size; i++){
			cout << r.arr[i] << " "; 
		}
		cout << "]";
		return os;
	}
private:
	int size;
	int curr_size;
	T *arr;
public:
	class iterator;
	void add(T obj){
		if (curr_size >= size){
			curr_size = 0;
		}
		arr[curr_size] = obj;
		curr_size++;
	}
	T& get(int idx){
		return arr[idx];
	}
	iterator begin(){
		return iterator(0, *this);
	}
	iterator end(){
		return iterator(size, *this);
	}
	ring(int size_in) : size{size_in}, curr_size{0}, arr{new T [size_in]} {}
	ring(initializer_list<T> lst){
		size =lst.size();
		curr_size = 0;
		arr = new T [lst.size()];
		for(auto val: lst){
			add(val);
		}
	}
	~ring() {
		delete [] arr; 
	}
};

template<typename T>
class ring<T>::iterator{
private:
	int idx;
	ring<T> &a_ring; 
public:
	iterator(int idx, ring<T> &r): idx{idx}, a_ring{r} {}
	
	iterator& operator++(int){
		idx++;
		return *this;
	}
	
	iterator& operator++(){
		idx++;
		return *this;
	}
	
	bool operator!=(iterator& other){
		return idx!=other.idx;
	}
	T& operator*(){
		return a_ring.arr[idx];
	}
};
#endif // RING_H