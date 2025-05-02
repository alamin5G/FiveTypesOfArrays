# Array Categories Performance Comparison

This project implements a performance comparison of different array categories in Java and Python, as discussed in Chapter 6 (Data Types) of Programming Languages and Structures book.

## Development Environment

### Java Implementation

- **IDE**: IntelliJ IDEA Ultimate 2025.1
- **JDK**: Java Development Kit 23
- **Operating System**: Windows 11
- **Libraries**: Java standard libraries (java.util.ArrayList, java.util.concurrent.TimeUnit)

### Python Implementation

- **IDE**: PyCharm Professional
- **Python Version**: Python 3.11
- **Operating System**: Windows 11
- **Libraries**: Standard Python libraries (time, numpy, array)

## Overview

This program demonstrates and measures the performance of five array categories using Java and Python:

1. **Static Arrays**: Pre-allocated arrays with fixed size known at compile time
2. **Fixed Stack-Dynamic Arrays**: Arrays with static subscript ranges but allocated at execution time
3. **Stack-Dynamic Arrays**: Arrays with dynamic subscript ranges determined at runtime
4. **Fixed Heap-Dynamic Arrays**: Arrays with dynamic storage allocation from the heap, fixed after creation
5. **Heap-Dynamic Arrays**: Fully dynamic arrays that can grow or shrink during execution (ArrayList in Java, lists in Python)

## Implementation Details for Java

### Static Arrays

- Implementation: Array with fixed size (1,000,000) known at compile time
- Storage allocation occurs when the class is loaded
- Performance: Approximately 6 milliseconds for population and traversal
- 

### Fixed Stack-Dynamic Arrays

- Implementation: Local array declaration with fixed size known at compile time
- Allocation happens at runtime when the method is executed
- Performance: Approximately 10 milliseconds

### Stack-Dynamic Arrays

- Implementation: Local array declaration where size is determined at runtime via user input
- Deallocated after method execution
- Performance: Approximately 6 milliseconds

### Fixed Heap-Dynamic Arrays

- Implementation: Standard Java array allocated explicitly on the heap using the 'new' keyword
- Size is defined by user input at runtime but fixed after allocation
- Performance: Approximately 6 milliseconds

### Heap-Dynamic Arrays

- Implementation: Java ArrayList that grows dynamically based on the number of elements
- Two variants tested:
  1. Without initial capacity (emphasizes dynamic resizing): ~60 milliseconds
  2. With initial capacity (minimizes resizing): ~27 milliseconds

## Key Findings for Java

1. The basic array implementations (Static, Fixed Stack-Dynamic, Stack-Dynamic, and Fixed Heap-Dynamic) show similar performance in Java, typically around 6-10 milliseconds for 1,000,000 elements.
2. Heap-Dynamic arrays (ArrayList) show significantly higher overhead:

   - Without initial capacity: ~60 milliseconds (10x slower than basic arrays)
   - With initial capacity: ~27 milliseconds (4-5x slower than basic arrays)
3. The performance difference in ArrayList is primarily due to:

   - Dynamic resizing operations
   - Boxing/unboxing overhead (converting between int and Integer)
   - Additional method call overhead for add() operations

## Python Implementation Performance Analysis Report

### Test Environment

- Language: Python
- Array Size: 1,000,000 elements (1M)
- Operations: Array creation, element insertion, summation
- Measurements: Time in milliseconds (ms)

### Performance Results Summary


#### 1. Static

- **Execution Time**: 213 ms
- **Implementation**: Local list with fixed size (pre-allocated in the main function)
- **Memory**: Stack-based allocation
- **Characteristics**:
  - Pre-determined size at compile time
  - Efficient memory usage
  - No resizing overhead

#### 2. Fixed Stack-Dynamic

- **Execution Time**: 66.52 ms
- **Implementation**: Local list with fixed size
- **Memory**: Stack-based allocation
- **Characteristics**:
  - Pre-determined size at compile time
  - Efficient memory usage
  - No resizing overhead

#### 3. Stack-Dynamic

- **Execution Time**: 64.60 ms
- **Implementation**: Size determined at runtime
- **Memory**: Stack allocation with dynamic sizing
- **Characteristics**:
  - Flexible size determination
  - Similar performance to fixed stack-dynamic
  - Efficient memory management

#### 4. Heap-Dynamic

##### Variant 1: Dynamic Growth (list.append())

- **Execution Time**: 84.28 ms
- **Implementation**: Dynamic resizing using append
- **Characteristics**:
  - Higher overhead due to resizing operations
  - More flexible but slower
  - Memory reallocation costs

##### Variant 2: Pre-allocated List

- **Execution Time**: 63.39 ms
- **Implementation**: Pre-allocated capacity
- **Characteristics**:
  - Best performance among tested methods
  - No resizing overhead
  - Efficient memory utilization

#### 5. Fixed Heap-Dynamic (with ArrayList comparison)

##### List Append Implementation

- **Execution Time**: 229.70 ms
- **Characteristics**:
  - Highest overhead due to continuous resizing
  - Most flexible but least performant

##### Pre-allocated Implementation

- **Execution Time**: 21.00 ms
- **Characteristics**:
  - Best performance overall
  - Optimal memory usage
  - Fixed size after allocation

### Performance Analysis for Python

#### Fastest to Slowest Implementation:

1. Fixed Heap-Dynamic (Pre-allocated): 21.00 ms
2. Heap-Dynamic (Pre-allocated): 63.39 ms
3. Stack-Dynamic: 64.60 ms
4. Fixed Stack-Dynamic: 66.52 ms
5. Heap-Dynamic (Dynamic Growth): 84.28 ms
6. Static (pre-allocated) : 213 ms
7. Fixed Heap-Dynamic (List Append): 229.70 ms

#### Key Findings:

1. **Pre-allocation Advantage**:

   - Pre-allocated implementations consistently perform better
   - Reduces memory reallocation overhead
   - More predictable performance
2. **Dynamic Growth Impact**:

   - Dynamic resizing significantly impacts performance
   - Append operations can be up to 3-4 times slower
   - Memory reallocation creates substantial overhead
3. **Stack vs Heap**:

   - Stack-based implementations show consistent performance
   - Heap allocations can be faster when properly pre-allocated
   - Dynamic heap allocations show the most variance
4. **Memory Management Effects**:

   - Garbage collection impacts overall performance
   - Proper memory cleanup is essential
   - Pre-allocation reduces memory fragmentation

## Comparative Analysis: Java vs Python

### Performance Comparison

| Array Category                    | Java Performance (ms) | Python Performance (ms) | Ratio (Python/Java) |
| --------------------------------- | --------------------- | ----------------------- | ------------------- |
| Static                            | 6                     | 213                     | 35.5x               |
| Fixed Stack-Dynamic               | 10                    | 66.52                   | 6.65x               |
| Stack-Dynamic                     | 6                     | 64.60                   | 10.77x              |
| Fixed Heap-Dynamic                | 6                     | 21.00                   | 3.5x                |
| Heap-Dynamic (no preallocation)   | 60                    | 84.28                   | 1.4x                |
| Heap-Dynamic (with preallocation) | 27                    | 63.39                   | 2.35x               |

### Syntax Comparison

#### Java Array Declaration and Initialization

```java
Fixed Stack-Dynamic void method() { int[] array = new int[1000000]; }
Stack-Dynamic int size = getUserInput(); int[] array = new int[size];
Fixed Heap-Dynamic int[] array = new int[size]; // Allocated on heap in Java
Heap-Dynamic ArrayList list = new ArrayList<>(); 
Dynamic growth ArrayList  list = new ArrayList<>(size); // With initial capacity
```

#### Python Array Declaration and Initialization

```python
# Fixed Stack-Dynamic
array = [0] * 1000000
# Stack-Dynamic
size = int(input("Enter size: ")) array = [0] * size
# Heap-Dynamic (dynamic growth)
array = [] for i in range(size): array.append(i)
# Heap-Dynamic (pre-allocated)
array = [0] * size for i in range(size): array[i] = i
```

### Key Differences Between Java and Python Implementation

1. **Type System**:

   - Java: Strongly typed, primitive arrays vs object arrays (int[] vs Integer[])
   - Python: Dynamically typed, lists can contain mixed types
2. **Memory Management**:

   - Java: More explicit memory allocation, separate heap and stack concepts
   - Python: Memory management is more abstracted, implementation details hidden
3. **Performance Characteristics**:

   - Java: Generally faster for array operations due to primitive types and JIT compilation
   - Python: Higher overhead due to dynamic typing and interpreter nature
4. **Array Resizing**:

   - Java: Arrays are fixed-size, ArrayList handles dynamic sizing
   - Python: Lists automatically resize with amortized constant time complexity
5. **Syntax Verbosity**:

   - Java: More verbose syntax with explicit typing
   - Python: More concise syntax with less type information

## Conclusions and Recommendations

### General Findings

- For performance-critical applications where the size is known or can be estimated, using fixed-size arrays provides the best performance in both languages.
- Pre-allocation significantly improves performance for dynamic collections in both Java and Python.
- Java generally outperforms Python for equivalent array operations, with Python typically 2-10x slower depending on the operation.
- The flexibility of dynamic arrays comes with a performance cost in both languages.

### For Java Development

- Use primitive arrays when possible for best performance
- Pre-allocate ArrayList with the expected size when using dynamic collections
- Consider using Arrays.fill() for bulk initialization
- Be aware of autoboxing overhead when using collections of primitives

### For Python Development

- Use pre-allocated lists ([0] * size) rather than building lists with append()
- Consider NumPy arrays for numerical computations for significant performance gains
- Be mindful of memory overhead of Python objects compared to primitive values
- Use list comprehensions for better performance when creating lists

### Best Practices for Both Languages

- Choose the appropriate array type based on your application needs
- Pre-allocate when size is known or can be estimated
- Minimize dynamic resizing operations
- Consider memory cleanup for long-running operations
- Balance flexibility needs against performance requirements

## Usage

Run the Java** *'Main.java'*** program in IntelliJ IDEA and follow the prompts to input array sizes when requested. The program will display performance metrics for each array type.

For the Python implementation, run the '***script1.py***' script in PyCharm using the equivalent Python code structure to compare performance characteristics.
