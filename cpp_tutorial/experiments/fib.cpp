#include <iostream>
using namespace std;

float fib(float x)
{
  if (x == 0){ return 1; }
  else if (x == 1){ return 1; }
  else { return fib(x-1) + fib(x-2); }
}

int main()
{
  for(float i = 10; i < 200; i++){
    cout << i << ":" << fib(i) << endl;
  }

  return 0;
}
