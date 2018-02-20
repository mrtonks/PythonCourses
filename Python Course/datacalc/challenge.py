# Write a small program to display information on the
# four clocks whose functions we have just looked at:
# i.e. time(), perf_counter, monotonic() and process_time().
#
# Use the documentation for the get_clock_info() function
# to work out how to call it for each of the clocks.
import time
from time import get_clock_info as get_clock

print("Time: {:.10}".format(get_clock('time').resolution))
print("Perf_counter: {:.20}".format(get_clock('perf_counter').resolution))
print("Monotonic: {:.10}".format(get_clock('monotonic').resolution))
print("Process_time: {:.20}".format(get_clock('process_time').resolution))
