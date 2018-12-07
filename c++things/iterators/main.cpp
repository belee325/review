#include <iostream>
#include <string>
#include <vector>

template<typename T>
struct BinaryTree;

template<typename T>
struct Node {
    T value = T();
    Node<T> *left{nullptr}, *right{nullptr}, *parent{nullptr};
    BinaryTree<T> *tree{nullptr};

    Node(T value) : value(value) {}

    Node(T value, Node<T> *left, Node<T> *right) : value(value), left(left), right(right) {
        this->left->tree = this->right->tree = tree;
        this->left->parent = this->right->parent = this;
    }

    void set_tree(BinaryTree<T> *t) {
        tree = t;
        if (left) left->set_tree(t);
        if (right) right->set_tree(t);
    }

    ~Node() {
        if (left) delete left;
        if (right) delete right;
    }
};

template<typename T>
struct BinaryTree {
    Node<T> *root{nullptr};

    BinaryTree(Node<T> *root) : root(root) {
        root->set_tree(this);
    }

    ~BinaryTree() {
        if (root) delete root;
    }

    template<typename U>
    struct PreOrderIterator {
        Node<U> *current;

        PreOrderIterator(Node<U> *current) : current(current) {}

        bool operator!=(const PreOrderIterator<U> &other) {
            return current != other.current;
        }

        PreOrderIterator<U> &operator++() {
            if (current->right) {
                current = current->right;
                while (current->left)
                    current = current->left;
            } else {
                Node<T> *p = current->parent;
                while (p && current == p->right) {
                    current = p;
                    p = p->parent;
                }
                current = p;
            }
            return *this;
        }

        Node<U> &operator*() { return *current; }
    };
        typedef PreOrderIterator<T> iterator;

        iterator end() {
            return iterator{nullptr};
        }

        iterator begin() {
            Node<T> *n = root;

            if (n)
                while (n->left)
                    n = n->left;
            return iterator{n};
        }
};


using namespace std;

int main() {


    std::cout << "Hello, World!" << std::endl;
    return 0;
}