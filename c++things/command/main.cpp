#include <iostream>
#include <string>
#include <vector>

using namespace std;
//ordinary statements are perishable - cannot undo a field or property assignment
//cant directly serialize a sequence of actions
//want an obj that represents an operation
//X should change its field Y to Z or X should do W()
//gui commands/multilevel undo redo/ macro recording ... etc
//command is an object that represents an instruction to perform a particular action
//Contains all the information necessary for the action to be taken

struct BankAccount {
    int balance{0};
    int overdraft_limit{-500};

    bool deposit(int amt) {
        if(amt <= 0){
            return false;
        }
        balance += amt;
        cout << "deposited " << amt;
        cout << "Balance is now: " << balance << endl;
        return true;
    }

    bool withdraw(int amt) {
        if (balance - amt >= overdraft_limit) {
            balance -= amt;
            cout << "withdrew " << amt << " Balance is now " << balance << endl;
            return true;
        }
        return false;
    }

    friend ostream &operator<<(ostream &os, const BankAccount &account) {
        os << "balance: " << account.balance << " overdraft_limit: " << account.overdraft_limit;
        return os;
    }
};

struct Command {
    bool succeeded;
    virtual void call() = 0;
    virtual void undo() = 0;
};

struct BankAccountCommand : Command {
    BankAccount &account;
    enum Action {
        deposit, withdraw
    } action;
    int amount;

    BankAccountCommand(BankAccount &account, Action action, int amount) : account(account), action(action),
                                                                          amount(amount) { succeeded = false;}

    void call() override {
        switch (action) {
            case deposit:
                succeeded = account.deposit(amount);
                break;
            case withdraw:
                succeeded = account.withdraw(amount);
                break;
        }
    }

    void undo() override{
        if (!succeeded) return;
        switch (action){
            case deposit:
                cout << "undoing a deposit"<< endl;
                succeeded = account.withdraw(amount);
                break;
            case withdraw:
                cout << "undoing a withdraw" << endl;
                succeeded = account.deposit(amount);
                break;
        }
    }

};

struct CompositeBankAccountCommand: vector<BankAccountCommand>, Command{
    CompositeBankAccountCommand(const initializer_list<BankAccountCommand> &items) : vector(items) {}

    void call() override {
        for(auto& cmd : *this){
            cmd.call();
        }
    }

    void undo() override {
        for(auto it = rbegin(); it != rend(); it++){
            it->undo();
        }
    }
};


struct DependentCompositeCommand : CompositeBankAccountCommand{
    DependentCompositeCommand(const initializer_list<BankAccountCommand> &items) : CompositeBankAccountCommand(items) {}

    void call() override {
        bool ok = true;
        for(auto& cmd : *this){
            if(ok){
                cmd.call();
                ok = cmd.succeeded;
            }
            else{
                cmd.succeeded = false;
            }
        }
    }
};

struct MoneyTransferCommand : DependentCompositeCommand{

    MoneyTransferCommand(BankAccount& from,BankAccount& to, int amount):
            DependentCompositeCommand{
                    BankAccountCommand{from, BankAccountCommand::withdraw, amount},
                    BankAccountCommand{to, BankAccountCommand::deposit, amount}
            } {};

};

    int main() {
//        BankAccount acct{};
//        vector<BankAccountCommand> commands{
//                BankAccountCommand{acct, BankAccountCommand::deposit, 10000},
//                BankAccountCommand{acct, BankAccountCommand::withdraw, 1000}
//        };
//        for(auto& cmd :commands){
//            cmd.call();
//        }
//        for(auto it = commands.rbegin(); it != commands.rend(); it++){
//            it->undo();
//        }
//        cout << acct << endl;

        BankAccount ba, ba2;
        ba.deposit(100);
        MoneyTransferCommand cmd{ba, ba2, 4000};
        cout << "before transfer" << endl << ba << endl << ba2 << endl;
        cmd.call();
        cout << "after transfer" << endl << ba << endl << ba2 << endl;
        cmd.undo();
        cout << "after transfer reversal" << endl << ba << endl << ba2 << endl;
        return 0;
    }