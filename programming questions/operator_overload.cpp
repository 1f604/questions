#include <stdio.h>
#include <iostream>
using namespace std;

struct AGE {
  int years;
  AGE(int years)
          : years(years)
      {
      }
  void operator+(const AGE& age) {
     if (years + age.years < 121) {
        years = years + age.years;
     }

  }
};


class AGE2 {
  int years;
public:
  int getyears(){ return years;}
  AGE2(int years)
          : years(years)
      {
      }
  void operator+(const AGE2 age) {
     if (years + age.years < 121) {
        years = years + age.years;
     }

  }
};

int main()
{
    AGE newage(5);
    AGE yeah(15);
    cout << newage.years;
    newage + yeah;
    cout << newage.years;
    AGE2 newage2(5);
    AGE2 yeah2(15);
    cout << newage2.getyears();
    newage2 + yeah2;
    cout << newage2.getyears();
    return 0;
}
