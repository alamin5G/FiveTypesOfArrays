# Array Categories Performance Comparison

This project implements a performance comparison of different array categories in Java, as discussed in Chapter 6 (Data Types) Programming Languages and Structures book.

## Overview

This program demonstrates and measures the performance of five array categories using Java and Python:

1. **Static Arrays**: Pre-allocated arrays with fixed size known at compile time
2. **Fixed Stack-Dynamic Arrays**: Arrays with static subscript ranges but allocated at execution time
3. **Stack-Dynamic Arrays**: Arrays with dynamic subscript ranges determined at runtime
4. **Fixed Heap-Dynamic Arrays**: Arrays with dynamic storage allocation from the heap, fixed after creation
5. **Heap-Dynamic Arrays**: Fully dynamic arrays that can grow or shrink during execution (ArrayList in Java)

## Implementation Details for Java

### Static Arrays
- Implementation: Array with fixed size (1,000,000) known at compile time
- Storage allocation occurs when the class is loaded
- Performance: Approximately 6 milliseconds for population and traversal

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

## Conclusions

- For performance-critical applications where the size is known or can be estimated, using fixed-size arrays provides the best performance.
- Setting an initial capacity for ArrayList significantly improves performance (by ~55%) compared to not setting it.
- The flexibility of dynamic arrays (ArrayList) comes with a notable performance cost.
- Java's memory management abstracts many of the theoretical differences between these array categories, resulting in similar performance for the basic array types.

## Usage

Run the program and follow the prompts to input array sizes when requested. The program will display performance metrics for each array type.