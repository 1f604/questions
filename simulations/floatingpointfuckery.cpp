#include <iostream>
#include <math.h>
using namespace std;
void foo()
{
std::cout.precision(64);
std::cout  << std::fixed << ((0.1+0.2)+0.3) << endl << (0.1+(0.2+0.3)) << endl;
  if (((0.1+0.2)+0.3)!=(0.1+(0.2+0.3)))
  {
    std::cout << "Huh?!?\n";  // you might end up here when x == y!!
  }
  else{
      std::cout << "Nothing bad happened\n";
  }
}
 
int main()
{
  foo();
  return 0;
}
