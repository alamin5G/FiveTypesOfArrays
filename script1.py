import time
import gc



def check_performance_for_fixed_stack_dynamic():
    """
    Performance test for Fixed Stack-Dynamic category concept.
    Implementation: Local list with size conceptually 'fixed' for this scope.
    Size is hardcoded within the function, mirroring the Java example structure.
    Result: Time = 66.52 ms
    """
    size = 1000000 # 1M - Hardcoded size like the Java method
    print("--- Performance Test: Fixed Stack-Dynamic ---")
    print(f"Category Implementation: Local list = [0] * {size} (fixed size declared locally). Size: {size}")
    start_time, end_time, duration = 0.0, 0.0, 0.0
    total_sum = 0

    start_time = time.time()
    # Size is fixed for this list object upon creation
    lst = [0] * size
    total_sum = 0
    for i in range(size):
        lst[i] = i
        total_sum += lst[i]
    end_time = time.time()
    duration = (end_time - start_time) * 1000 # milliseconds
    print(f"  Result: Sum = {total_sum}, Time = {duration:.2f} ms")
    del lst # Help GC
    gc.collect()

def check_performance_for_stack_dynamic(size):
    """
    Performance test for Stack-Dynamic category concept.
    Implementation: List created locally, size determined by the 'size' parameter
    passed at runtime (simulating dynamic determination like user input).
    Result: Time = 64.60 ms
    """
    print("--- Performance Test: Stack-Dynamic ---")
    print(f"Category Implementation: Local list = [0] * variable_size (size determined at runtime via user input). Size: {size}")
    start_time, end_time, duration = 0.0, 0.0, 0.0
    total_sum = 0

    start_time = time.time()
    # Size 'size' is dynamic from the caller's perspective
    lst = [0] * size
    total_sum = 0
    for i in range(size):
        lst[i] = i
        total_sum += lst[i]
    end_time = time.time()
    duration = (end_time - start_time) * 1000 # milliseconds
    print(f"  Result: Sum = {total_sum}, Time = {duration:.2f} ms")
    del lst # Help GC
    gc.collect()

def check_performance_for_heap_dynamic(size):
    """
    Performance test for Heap-Dynamic category.
    Implementation: Python list using .append() which grows dynamically (like ArrayList w/o capacity)
                    and list pre-allocation (like ArrayList w/ capacity).
    Result with List append(): Time = 84.28 ms
    Result with List pre-allocation: Time = 63.39 ms
    """
    print("--- Performance Test: Heap-Dynamic ---")
    print(f"Category Implementation: list.append() vs list pre-allocation. Size: {size}")
    start_time, end_time, duration = 0.0, 0.0, 0.0
    total_sum = 0

    # Variant 1: Using append (simulates ArrayList without initial capacity - resizing cost)
    print("  Variant: Using list.append()")
    start_time = time.time()
    lst_append = []
    total_sum = 0
    for i in range(size):
        lst_append.append(i) # Dynamic resizing may occur
        # Summing during append loop
        total_sum += i
    end_time = time.time()
    duration = (end_time - start_time) * 1000 # milliseconds
    print(f"    Result: Sum = {total_sum}, Time = {duration:.2f} ms")
    del lst_append # Help GC

    # Variant 2: Pre-allocating list (simulates ArrayList with initial capacity - less resizing)
    print("  Variant: Using list pre-allocation")
    start_time = time.time()
    lst_prealloc = [0] * size
    total_sum = 0
    for i in range(size):
        lst_prealloc[i] = i # Assign value
        total_sum += lst_prealloc[i]
    end_time = time.time()
    duration = (end_time - start_time) * 1000 # milliseconds
    print(f"    Result: Sum = {total_sum}, Time = {duration:.2f} ms")
    del lst_prealloc # Help GC

    gc.collect()

# ===========================================================
# Main execution block mirroring the Java structure
# ===========================================================
if __name__ == "__main__":

    print("===========================================================")
    print("===== Starting Performance Comparisons for Static =====")
    static_test_size = 1000000 # 1M - Hardcoded size for the static test in main

    print("--- Performance Test: Static (Operational Speed) ---")
    print(f"Category Implementation: Simulating operations on pre-allocated fixed storage (using local list). Size: {static_test_size}")
    start_time_s, end_time_s, duration_s = 0.0, 0.0, 0.0
    sum_s = 0

    start_time_s = time.time()
    # Simulates operating on storage whose size was fixed conceptually 'before runtime'
    static_array_sim = [0] * static_test_size
    sum_s = 0
    for i in range(static_test_size):
        static_array_sim[i] = i # traverse and insert
        sum_s += static_array_sim[i] # manipulate
    end_time_s = time.time()
    duration_s = (end_time_s - start_time_s) * 1000 # milliseconds
    print(f"  Result: Sum = {sum_s}, Time = {duration_s:.2f} ms")
    del static_array_sim
    gc.collect() # Suggest GC
    print("===== Ending Performance Comparisons for Static ========")
    print("===========================================================")

    print("===========================================================")
    print("*** Running tests for Fixed Stack Dynamic ***")
    # Calls the function where size is hardcoded internally
    check_performance_for_fixed_stack_dynamic()
    print("===========================================================")


    print("===========================================================")
    print("*** Running tests for Stack Dynamic ***")
    try:
        # Get size from user input for Stack Dynamic test
        stack_dynamic_size_str = input(f"Enter size for the stack-dynamic list (e.g., 1000000): ")
        stack_dynamic_array_size = int(stack_dynamic_size_str)
        check_performance_for_stack_dynamic(stack_dynamic_array_size) # Pass runtime size
    except ValueError:
        print("Invalid input. Please enter an integer.")
    print("===========================================================")


#    Performance test for Heap-Dynamic category.
#    Implementation: Python list using .append() which grows dynamically (like ArrayList w/o capacity)
#                  and list pre-allocation (like ArrayList w/ capacity).
#    Result with List append(): Time = 229.70 ms
#    Result with List pre-allocation: Time = 21.00 ms

    print("===========================================================")
    print("*** Running tests for Fixed Heap Dynamic ***")
    try:
        # Get size from user input for Fixed Heap Dynamic test
        heap_dynamic_size_str = input(f"Enter size for the fixed heap-dynamic list/tuple (e.g., 1000000): ")
        heap_dynamic_array_size = int(heap_dynamic_size_str)

        print(f"--- Performance Test: Fixed Heap-Dynamic ---")
        print(f"Category Implementation: list pre-allocation or tuple creation on heap. Size: {heap_dynamic_array_size}")

        # Variant 1: List pre-allocation (inline test)
        print("  Variant: List pre-allocation")
        start_time_fh_l, end_time_fh_l, duration_fh_l = 0.0, 0.0, 0.0
        sum_fh_l = 0
        start_time_fh_l = time.time()
        fixed_heap_list = [0] * heap_dynamic_array_size
        sum_fh_l = 0
        for i in range(heap_dynamic_array_size):
            fixed_heap_list[i] = i
            sum_fh_l += fixed_heap_list[i]
        end_time_fh_l = time.time()
        duration_fh_l = (end_time_fh_l - start_time_fh_l) * 1000 # milliseconds
        print(f"    Result: Sum = {sum_fh_l}, Time = {duration_fh_l:.2f} ms")
        del fixed_heap_list

        # Variant 2: Tuple creation (inline test - immutable fixed heap)
        print("  Variant: Tuple creation")
        start_time_fh_t, end_time_fh_t, duration_fh_t = 0.0, 0.0, 0.0
        sum_fh_t = 0
        start_time_fh_t = time.time()
        fixed_heap_tuple = tuple(range(heap_dynamic_array_size)) # Create tuple
        sum_fh_t = sum(fixed_heap_tuple)     # Sum tuple (efficiently)
        end_time_fh_t = time.time()
        duration_fh_t = (end_time_fh_t - start_time_fh_t) * 1000 # milliseconds
        print(f"    Result: Sum = {sum_fh_t}, Time = {duration_fh_t:.2f} ms")
        del fixed_heap_tuple

        gc.collect() # Suggest GC after Fixed Heap tests
    except ValueError:
         print("Invalid input. Please enter an integer.")
    print("===========================================================")


    print("===========================================================")
    print("*** Running tests for Heap Dynamic ***")
    # Using a fixed size for this call, similar to Java testSize1
    heap_dynamic_test_size = 1000000
    check_performance_for_heap_dynamic(heap_dynamic_test_size) # Contains two variants inside
    print("===========================================================")


    print("===== Performance Comparisons Complete =====")
    print("===========================================================")