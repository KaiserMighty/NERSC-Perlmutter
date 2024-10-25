#include <algorithm>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <random>
#include <vector>
#include <string.h>



void 
setup(int64_t N, uint64_t A[])
{
   printf(" inside sum_indirect problem_setup, N=%lld \n", N);

   srand48(48);
   for (int64_t j = 0; j < N; ++j)
   {
      A[j] = lrand48() % N;
   }
}

int64_t
sum(int64_t N, uint64_t A[])
{
   printf(" inside sum_indirect perform_sum, N=%lld \n", N);

   int64_t total_sum = 0;
   int64_t indx = A[0];
   for (int64_t i = 0; i < N; ++i)
   {
      total_sum += A[indx];
      indx = A[indx];
   }

   return total_sum;
}

