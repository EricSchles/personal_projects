#include <iostream>
using namespace std;

float fib(int arr_size)
{
  float arr[arr_size];
  arr[0] = 1;
  arr[1] = 1;
  for( int i = 2; i < arr_size; i++){ arr[i] = arr[i-1] + arr[i-2]; }
  return arr[arr_size - 1];
}

int main(){
  for (int i = 10; i < 200; i++)
    {
      cout << i << ":" << fib(i) << endl;
    }

  return 0;
}
