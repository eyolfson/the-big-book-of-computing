#include <stdio.h>
#include <stdint.h>

static
uint8_t mean_1(uint8_t x_0, uint8_t x_1)
{
  return ((uint8_t) (x_0 + x_1)) / 2;
}

static
uint8_t mean_2(uint8_t x_0, uint8_t x_1)
{
  return (x_0 / 2) + (x_1 / 2);
}

static
uint8_t mean_3(uint8_t x_0, uint8_t x_1)
{
  return (x_0 / 2) + (x_1 / 2) + (((x_0 % 2) + (x_1 % 2)) / 2);
}

int main()
{
  uint8_t x_0 = 201;
  uint8_t x_1 = 203;
  printf("%u\n", mean_1(x_0, x_1));
  printf("%u\n", mean_2(x_0, x_1));
  printf("%u\n", mean_3(x_0, x_1));
  return 0;
}
