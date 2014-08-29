#include <iostream>
using namespace std;

class Obj1 {
public:
    void         A() { cout << "A" << endl; }
    virtual void B() { cout << "B" << endl; }
    virtual void C() = 0;
};

class Obj2 : public Obj1 {
public:
    void         A() { cout << "Q" << endl; }
    void C() { cout << "X" << endl; }
};

class Obj3 : public Obj1 {
public:
    void B() { cout << "P" << endl; }
    void C() { cout << "Y" << endl; }
};

class Obj4 : public Obj2 {
public:
    void A() { cout << "F" << endl; }
    void B() { cout << "G" << endl; }
};

class Obj5 : public Obj2 {
public:
    void C() { cout << "H" << endl; }
};

void TestA(Obj2 ob_a, Obj2& ob_b)
{
    ob_a.A();
    ob_b.B();
    ob_b.C();
}

void TestB(Obj1& ob_a, Obj2& ob_b)
{
    ob_a.A();
    ob_a.B();
    ob_b.B();
    ob_b.C();
}

int main(int argc, char const *argv[])
{
    // causes of error commented out

    // Obj1 ob1;
    Obj2 ob2;
    Obj3 ob3;
    Obj4 ob4;
    Obj5 ob5;

    // TestA(ob3, ob4);
    // TestA(ob4, ob5);
    // cout << endl;
    // TestB(ob2, ob5);
    // cout << endl;
    TestB(ob4, ob2);

    return 0;
}
