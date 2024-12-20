# Vector Matrix Multiplication
Vector-matrix multiplication in multiple forms: basic, vectorized, and shared-memory parallel using OpenMP; ran on Perlmutter@NERSC on a CPU node.

## Equations
```
MFLOP/s                                = (# of Arithmetic Operations/1000000)/Runtime
% of Peak Memory Bandwidth Utilization = ((# of Memory Accesses * Size of Data Type)/Runtime)/Capacity
Number of Arithmetic Operations        = 2N^2
Number of Memory Accesses              = 2N^2+2N
Size of Data Type (Double)             = 8 Bytes
Theoretical Peak Capacity              = 204.8 * 1000000000
```

## Runtime (s)
|Problem Size|blas   |basic  |vectorized|omp-1  |omp-4  |omp-16 |omp-64 |
|------------|-------|-------|----------|-------|-------|-------|-------|
|1024        |0.00016|0.00091|0.00021   |0.00087|0.00047|0.00028|0.00068|
|2048        |0.00050|0.00358|0.00091   |0.00361|0.00177|0.00170|0.00172|
|4096        |0.00417|0.01454|0.00417   |0.01450|0.00435|0.00333|0.00334|
|8192        |0.01713|0.05830|0.01696   |0.05815|0.01554|0.01298|0.01345|
|16384       |0.07179|0.23351|0.06997   |0.23336|0.06026|0.05577|0.05818|

## MFLOP/s
|Problem Size|blas      |basic    |vectorized|omp-1    |omp-4    |omp-16    |omp-64    |
|------------|----------|---------|----------|---------|---------|----------|----------|
|1024        |13107.2000|2304.5626|9986.4381 |2410.5195|4462.0255|7489.8286 |3084.0471 |
|2048        |16777.2160|2343.1866|9218.2505 |2323.7141|4739.3266|4934.4753 |4877.0977 |
|4096        |8046.6264 |2307.7326|8046.6264 |2314.0988|7713.6625|10076.4060|10046.2371|
|8192        |7835.2439 |2302.1909|7913.7811 |2308.1295|8636.9194|10340.3488|9979.0132 |
|16384       |7478.3523 |2299.1346|7672.8728 |2300.6124|8909.2418|9626.5181 |9227.7572 |

## % of Peak Memory Bandwidth Utilization
|Problem Size|blas    |basic  |vectorized|omp-1  |omp-4   |omp-16  |omp-64  |
|------------|--------|-------|----------|-------|--------|--------|--------|
|1024        |51.2500%|9.0110%|39.0476%  |9.4253%|17.4468%|29.2857%|12.0588%|
|2048        |65.5680%|9.1575%|36.0264%  |9.0814%|18.5220%|19.2847%|19.0605%|
|4096        |31.4398%|9.0168%|31.4398%  |9.0417%|30.1389%|39.3706%|39.2527%|
|8192        |30.6102%|8.9940%|30.9170%  |9.0172%|33.7421%|40.3969%|38.9853%|
|16384       |29.2141%|8.9815%|29.9740%  |8.9873%|34.8038%|37.6059%|36.0481%|

## Speedup
|Problem Size|omp-4  |omp-16 |omp-64 |
|------------|-------|-------|-------|
|16384       |3.87255|4.18433|4.01100|