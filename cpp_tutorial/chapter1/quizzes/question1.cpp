#include <iostream>
#include "io.cpp"
using namespace std;

int readNumber();

int writeAnswer(int x, int y);

int main()
{
  int x,y;
  x = readNumber();
  y = readNumber();
  cout << writeAnswer(x,y) << endl;
  
  return 0;
}
