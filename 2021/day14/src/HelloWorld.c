#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char* argv[])
{
  int i;
  double x[10];
  printf("hello world\n");
  for (i = 0; i < 10; i++)
  {
    x[i] = cos(i * M_PI / 3);
    printf("x[%d] : %f\n", i, x[i]);
  }
  return EXIT_SUCCESS;  
}
