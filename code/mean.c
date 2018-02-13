#include <assert.h>
#include <stdio.h>
#include <stdint.h>
#include <time.h>

uint32_t mean_1(uint32_t x_0, uint32_t x_1)
{
  return (x_0 + x_1) / 2;
}

uint32_t mean_2(uint32_t x_0, uint32_t x_1)
{
  return (x_0 / 2) + (x_1 / 2);
}

uint32_t mean_3(uint32_t x_0, uint32_t x_1)
{
  return (x_0 / 2) + (x_1 / 2) + (((x_0 % 2) + (x_1 % 2)) / 2);
}

int32_t nano_elapsed(struct timespec *start, struct timespec *end)
{
  uint32_t ret;
  if ((end->tv_nsec - start->tv_nsec) < 0) {
    ret = (end->tv_sec - start->tv_sec - 1) * 1000000000;
    ret += end->tv_nsec - start->tv_nsec + 1000000000;
  }
  else {
    ret = (end->tv_sec - start->tv_sec) * 1000000000;
    ret += end->tv_nsec - start->tv_nsec;
  }
  return ret;
}

int main()
{
  uint32_t x_0 = UINT32_MAX - 2;
  uint32_t x_1 = UINT32_MAX - 4;
  printf("Result 1: %u\n", mean_1(x_0, x_1));
  printf("Result 2: %u\n", mean_2(x_0, x_1));
  printf("Result 3: %u\n", mean_3(x_0, x_1));

  struct timespec start;
  struct timespec end;

  assert(clock_gettime(CLOCK_MONOTONIC, &start) == 0);
  for (int32_t i = 0; i < 100000000; ++i) {
    mean_1(x_0, x_1);
  }
  assert(clock_gettime(CLOCK_MONOTONIC, &end) == 0);
  int32_t elapsed = nano_elapsed(&start, &end);
  printf("Elapsed 1: %d.%d s\n", elapsed / 1000000000, elapsed % 1000000000);

  assert(clock_gettime(CLOCK_MONOTONIC, &start) == 0);
  for (int32_t i = 0; i < 100000000; ++i) {
    mean_2(x_0, x_1);
  }
  assert(clock_gettime(CLOCK_MONOTONIC, &end) == 0);
  elapsed = nano_elapsed(&start, &end);
  printf("Elapsed 2: %d.%d s\n", elapsed / 1000000000, elapsed % 1000000000);

  assert(clock_gettime(CLOCK_MONOTONIC, &start) == 0);
  for (int32_t i = 0; i < 100000000; ++i) {
    mean_3(x_0, x_1);
  }
  assert(clock_gettime(CLOCK_MONOTONIC, &end) == 0);
  elapsed = nano_elapsed(&start, &end);
  printf("Elapsed 3: %d.%d s\n", elapsed / 1000000000, elapsed % 1000000000);

  return 0;
}
