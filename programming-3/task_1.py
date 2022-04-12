from multiprocessing.dummy import freeze_support
import numpy as np
import multiprocessing as mp
from multiprocessing import Pool
# import cupy as cp
import math
import time

# Generate random array with 2^24 in length - maximum hardware
# Generate random array with 2^12 in length - maximum hardware
signal_random_2 = np.random.rand(2**2)
signal_random_4 = np.random.rand(2**4)
signal_random_6 = np.random.rand(2**6)
signal_random_8 = np.random.rand(2**8)
signal_random_10 = np.random.rand(2**10)
signal_random_12 = np.random.rand(2**12)
signal_random_14 = np.random.rand(2**14)
signal_random_16 = np.random.rand(2**16)
signal_random_18 = np.random.rand(2**18)
signal_random_20 = np.random.rand(2**20)
signals_short = [signal_random_2, signal_random_4, signal_random_6, signal_random_8, signal_random_10]
signals_long = [signal_random_2, signal_random_4, signal_random_6, signal_random_8, signal_random_10, signal_random_12, signal_random_14, signal_random_16, signal_random_18]

def dft_1(sample):
    '''
    Discrete Fourier Transform using `for` loop.

    Parameters:
        sample: 1D array of real numbers

    Returns:
        The shifted DFT output
    '''
    N = len(sample)
    dft_output = []
    # Perform DFT
    for k in range(N):
        sum = 0
        for n in range(N):
            sum += sample[n] * math.cos(2 * math.pi * n * k / N)
        dft_output.append(sum)
    # Shift on frequency domain
    dft_output = dft_output[int(N/2):] + dft_output[:int(N/2)]
    return dft_output

def _dft_k(tuple_input):
    '''
    This function is the thread worker for DFT function `dft_1_opt`.
    '''
    sample, k, N = tuple_input
    return sum(sample[n] * math.cos(2 * math.pi * n * k / N) for n in range(N))

def dft_1_opt(sample):
    '''
    This function performs DFT on a sample using a pool of workers.

    Parameters:
        sample: a 1D numpy array of length N
    
    Returns:
        The shifted DFT output of the sample
    '''
    N = len(sample)
    # Create a pool of processes
    pool = Pool(processes=mp.cpu_count())
    # Perform DFT
    dft_output = pool.map(_dft_k, [(sample, i, N) for i in range(N)])
    return dft_output

# Perform DFT on random signal and plot the result
def dft_1_test():
    print("DFT_1 Implementation (for loop)")
    dft_1_output = []
    time_elapsed = []
    for signal in signals_long[6:]:
        start = time.time()
        print(">>> Signal length:", len(signal))
        print(">   Starting DFT at ", time.strftime("%H:%M:%S", time.localtime()))
        dft_1_output.append(dft_1(signal))
        print(">   Finished DFT at ", time.strftime("%H:%M:%S", time.localtime()))
        end = time.time()
        # If time is shorter then 1 second, perform 100 times to see time used
        print(">   Time elapsed: " + str(end - start) + " seconds")
        if end - start < 0.1:
            print(">   Started 1000-round test...")
            start_1000 = time.time()
            for i in range(1000):
                dft_1(signal)
            end_1000 = time.time()
            print(">   Finished 1000-round test, using " + str(end_1000 - start_1000) + " seconds")
            time_elapsed.append((end_1000 - start_1000)/1000)
        elif end - start < 1:
            print(">   Started 100-round test...")
            start_100 = time.time()
            for i in range(100):
                dft_1(signal)
            end_100 = time.time()
            print(">   Finished 100-round test, using " + str(end_100 - start_100) + " seconds")
            time_elapsed.append((end_100 - start_100)/100)
        else:
            time_elapsed.append(end - start)
    return dft_1_output, time_elapsed

# Perform DFT on random signal and plot the result
def dft_1_opt_test():
    print("DFT_1 Implementation (for loop parellel)")
    dft_1_output = []
    time_elapsed = []
    for signal in signals_long:
        start = time.time()
        print(">>> Signal length:", len(signal))
        print(">   Starting DFT at ", time.strftime("%H:%M:%S", time.localtime()))
        dft_1_output.append(dft_1_opt(signal))
        print(">   Finished DFT at ", time.strftime("%H:%M:%S", time.localtime()))
        end = time.time()
        # If time is shorter then 1 second, perform 100 times to see time used
        print(">   Time elapsed: " + str(end - start) + " seconds")
        if end - start < 0.1:
            print(">   Started 1000-round test...")
            start_1000 = time.time()
            for i in range(1000):
                dft_1_opt(signal)
            end_1000 = time.time()
            print(">   Finished 1000-round test, using " + str(end_1000 - start_1000) + " seconds")
            time_elapsed.append((end_1000 - start_1000)/1000)
        elif end - start < 1:
            print(">   Started 100-round test...")
            start_100 = time.time()
            for i in range(100):
                dft_1_opt(signal)
            end_100 = time.time()
            print(">   Finished 100-round test, using " + str(end_100 - start_100) + " seconds")
            time_elapsed.append((end_100 - start_100)/100)
        else:
            time_elapsed.append(end - start)
    return dft_1_output, time_elapsed

if __name__ == "__main__":
    freeze_support()
    dft_1_output, time_elapsed = dft_1_test()
    dft_1_opt_output, time_elapsed_opt = dft_1_opt_test()
