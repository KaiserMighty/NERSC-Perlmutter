# CUDA Vector Addition
Vector additions executed in multiple forms: cpu (not cuda, not run on a GPU), gpu_1t (single thread), gpu_256t (256 threads), gpu_256t_mb (multiple thread-blocks), and gpu_256t_mb_prefetch (pre-execution data-transfer) using CUDA; ran on Perlmutter@NERSC on a NVIDIA GPU node.

## Assumptions
There is no cost associated with accessing, incrementing, and testing the loop index variable.  
Accessing the built-in CUDA variables `threadIdx`, `blockDim`, etc. is also for free.  
Since their impact is negligible, the calculation of `index` and `stride` in the GPU codes are free.  
Only the contents of the loop inside the `add` function performing the sum is included in my analysis.  

## Equations and Formulas
```
Problem Size (N)                = 536870912
Number of Arithmetic Operations = 1N
Number of Memory Accesses       = 3N (2 Reads and 1 Write)
Size of Data Type (Float)       = 4 Bytes
MFLOP/s                         = (# of Arithmetic Operations/Runtime in Seconds)/(1024*1024)
Memory Bandwidth Utilization    = (# of Memory Accesses * Size of Data Type)/Runtime in Seconds
```

## Performance Table
|Implementation      |Runtime (ms)|MFLOP/s    |Mem Bandwidth (GB/s)|
|--------------------|------------|-----------|--------------------|
|cpu                 |1282.14     |399.3323662|5024764023          |
|gpu_1t              |51271.97425 |9.985962263|125652484.4         |
|gpu_256t            |1744.066506 |293.5667867|3693925043          |
|gpu_256t_mb         |1223.747945 |418.3868109|5264524423          |
|gpu_256t_mb_prefetch|4.741113    |107991.5201|1358847795000       |

## Analysis
To calculate the MFLOP/s performance gain from the CPU-only code to the final version of the GPU-code, all we have to do is divide the final version of the GPU-code’s MFLOP/s with the CPU-only code’s MFLOP/s from the performance table. This gives us the gain as a multiplier: `107991.5201399 / 3323662 = 270.4301711`. The MFLOP/s performance gain is a little over `270.43x` going from the CPU-only code to the prefetched-GPU code.

To calculate the Memory Bandwidth performance gain from the CPU-only code to the final version of the GPU-code, all we have to do is divide the final version of the GPU-code’s Memory Bandwidth with the CPU-only code’s Memory Bandwidth from the performance table. This gives us the gain as a multiplier: `1358847795000 / 5024764023 = 270.4301712`. The Memory Bandwidth performance gain is a little over `270.43x` going from the CPU-only code to the prefetched-GPU code.

To calculate the maximum number of concurrent threads, we need to figure out how many SMs our processor has, and how many threads each SM supports. The Perlmutter uses NVIDIA A100s, which have `108` SMs, each of which can support a maximum of `2048` threads: `Max Concurrent Threads = 108 * 2048 = 221184`. Our program specifies the size of blocks as 256. The program also prints out the number of thread blocks before running the function, which is 2097152 thread blocks: `Threads Launched = 256 * 2097152 = 536870912`. Since the number of threads the program needs is larger than the maximum number of threads supported, we can assume all threads are being used concurrently. As such, the number of concurrent threads being run is `221184`.