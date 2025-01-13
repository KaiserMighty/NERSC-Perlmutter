# NERSC Perlmutter High Performance Computing Projects
Code ran and analyzed on Perlmutter at NERSC, an HPE Cray Shasta platform, GPU-accelerated supercomputer while learning High Performance Computing and Performance Modelling. The 3 projects are outlined below, each project folder contains all the source code, terminal output from the super computer, and subsequent analysis in their respective readme files.

## sum_performance_modelling
Array Sum Computation implemented in 3 different memory access patterns. Direct, Vector, and Indirect. This project's purpose was to learn performance modelling and CPU memory architecture.

## vector_matrix_multiplication
1D Vector Matrix Multiplication implemented at 3 levels of concurrency. Simple, Vectorized, and OpenMP Multi-threading. This project's purpose was to learn how the CPU cache architecture impacts code parallelism.

## cuda_gpu_vector_addition
Vector Addition implemented 5 different ways. CPU Only, 1 Thread - 1 Thread Block GPU, 256 Threads - 1 Thread Block GPU, 256 Threads - Many Thread Blocks GPU, and 256 Threads - Many Thread Blocks GPU with Prefetch. This project's purpose was to learn CUDA and GPU architecture.
