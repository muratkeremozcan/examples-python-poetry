# benchmark(target_func, arg1, arg2..) style: directly passes the target function and its args for measurement.
# @benchmark decorator style: wraps an inner function so you can benchmark arbitrary code blocks inline.

def create_list():
    return [i for i in range(1000)]
def create_set():
    return set([i for i in range(1000)])
def find(it, el=50):
    return el in it

def test_list(benchmark):
    benchmark(find, create_list())
    # Adjusted threshold based on actual benchmark results (~667ns mean)
    benchmark.extra_info['threshold'] = '700ns'
    assert benchmark.stats['mean'] < 700e-9  # 700ns in seconds

def test_set(benchmark):
    benchmark(find, create_set())
    # Adjusted threshold based on actual benchmark results (~94ns mean)
    benchmark.extra_info['threshold'] = '100ns'
    assert benchmark.stats['mean'] < 100e-9  # 100ns in seconds
	
# in decorator style
def test_list2(benchmark):
    @benchmark
    def bench_find_list():
        find(create_list())
    
    # Adjusted threshold based on actual benchmark results (~23.5μs mean)
    benchmark.extra_info['threshold'] = '25μs'
    assert benchmark.stats['mean'] < 25e-6  # 25 microseconds in seconds

def test_set2(benchmark):
    @benchmark
    def bench_find_set():
        find(create_set())
    
    # Adjusted threshold based on actual benchmark results (~35μs mean)
    benchmark.extra_info['threshold'] = '40μs'
    assert benchmark.stats['mean'] < 40e-6  # 40 microseconds in seconds

# Name (time in ns)          Min                   Max                Mean             StdDev              Median                IQR             Outliers  OPS (Mops/s)            Rounds  Iterations
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# test_set               47.0795 (1.0)        323.7498 (1.0)       51.9697 (1.0)       5.1208 (1.0)       53.7490 (1.0)       5.8289 (1.0)      2235;1686       19.2420 (1.0)      192010         100
# test_list             177.4428 (3.77)     1,364.1849 (4.21)     195.2731 (3.76)     20.6461 (4.03)     202.1444 (3.76)     21.5929 (3.70)     2682;1943        5.1210 (0.27)     198378          27
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# •	Mean: the arithmetic average of all run-times; indicates overall central tendency but is sensitive to outliers.
# •	Median: the 50th-percentile (middle) run-time; shows the “typical” case and ignores extreme values.
# •	StdDev: the root-mean-square deviation from the mean; measures how much run-times bounce around.
# •	IQR: the span from the 25th to 75th percentile; captures the width of your middle 50% of runs, robust to extremes.

# 	•	Mean: set ∼52 ns vs list ∼195 ns → set is ~4× faster
# 	•	Median: set’s 53.7 ns vs list’s 202.1 ns → typical run confirms the mean
# 	•	StdDev: set’s 5 ns vs list’s 20 ns → list times jump around four times more
# 	•	IQR: set’s 5.8 ns vs list’s 21.6 ns → list’s middle-50% of runs also much wider spread

# In short, all four metrics agree: find on a set is faster and more predictable than on a list.

def test_iterate_list(benchmark):
    @benchmark
    def bench_iterate_list():
        for _ in [i for i in range(1000)]:
            pass
    
    # Adjusted threshold based on actual benchmark results (~29.4μs mean)
    benchmark.extra_info['threshold'] = '35μs'
    assert benchmark.stats['mean'] < 35e-6  # 35 microseconds in seconds

def test_iterate_set(benchmark):
    @benchmark
    def bench_iterate_set():
        for _ in {i for i in range(1000)}:
            pass
    
    # Adjusted threshold based on actual benchmark results (~39μs mean)
    benchmark.extra_info['threshold'] = '45μs'
    assert benchmark.stats['mean'] < 45e-6  # 45 microseconds in seconds