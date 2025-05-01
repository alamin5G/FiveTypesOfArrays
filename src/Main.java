import java.util.concurrent.TimeUnit;

public class Main {



    /**
     * Performance test for Fixed Stack-Dynamic category.
     * Implementation: Local array declaration with fixed size known at compile time (int[] arr = new int[CONSTANT];)
     * but allocation happens at runtime when the method/declaration is reached.
     * Uses a local int[] for the benchmark.
     */
    /*public static void checkPerformanceForFixedStackDynamic(int size) {
        System.out.println("\n--- Performance Test: Fixed Stack-Dynamic ---");
        System.out.println("Category Implementation: Local int[" + size + "] (fixed size declared locally). Size: " + size);
        long startTime, endTime, duration;
        long sum;

        startTime = System.nanoTime();
        // The size is fixed *for this execution context* when declared
        int[] array = new int[size];
        sum = 0L;
        for (int i = 0; i < size; i++) {
            array[i] = i;
            sum += array[i];
        }
        endTime = System.nanoTime();
        duration = TimeUnit.NANOSECONDS.toMillis(endTime - startTime);
        System.out.println("  Result: Sum = " + sum + ", Time = " + duration + " ms");
        System.gc(); // Suggest GC
    }*/

    /**
     * Performance test for Stack-Dynamic category.
     * Implementation: Local array declaration where size is determined at runtime
     * before allocation. (int[] arr = new int[variable];)
     * The 'size' parameter passed to this method represents the runtime-determined size.
     */
    /*public static void checkPerformanceForStackDynamic(int size) {
        System.out.println("\n--- Performance Test: Stack-Dynamic ---");
        System.out.println("Category Implementation: Local int[variableSize] (size determined at runtime). Size: " + size);
        long startTime, endTime, duration;
        long sum;

        startTime = System.nanoTime();
        // Size 'size' is dynamic from the caller's perspective
        int[] array = new int[size];
        sum = 0L;
        for (int i = 0; i < size; i++) {
            array[i] = i;
            sum += array[i];
        }
        endTime = System.nanoTime();
        duration = TimeUnit.NANOSECONDS.toMillis(endTime - startTime);
        System.out.println("  Result: Sum = " + sum + ", Time = " + duration + " ms");
        System.gc(); // Suggest GC
    }*/

    /**
     * Performance test for Fixed Heap-Dynamic category.
     * Implementation: Standard Java array allocated explicitly on the heap with 'new'.
     * Size is fixed after allocation.
     */
    /*public static void checkPerformanceForFixedHeapDynamic(int size) {
        System.out.println("\n--- Performance Test: Fixed Heap-Dynamic ---");
        System.out.println("Category Implementation: Standard 'new int[" + size + "]' on heap. Size: " + size);
        long startTime, endTime, duration;
        long sum;

        startTime = System.nanoTime();
        int[] array = new int[size]; // Explicit heap allocation request
        sum = 0L;
        for (int i = 0; i < size; i++) {
            array[i] = i;
            sum += array[i];
        }
        endTime = System.nanoTime();
        duration = TimeUnit.NANOSECONDS.toMillis(endTime - startTime);
        System.out.println("  Result: Sum = " + sum + ", Time = " + duration + " ms");
        System.gc(); // Suggest GC
    }*/

    /**
     * Performance test for Heap-Dynamic category.
     * Implementation: Java ArrayList, which grows dynamically on the heap.
     * Testing population using add() which may trigger resizing.
     */
    /*public static void checkPerformanceForHeapDynamic(int size) {
        System.out.println("\n--- Performance Test: Heap-Dynamic ---");
        System.out.println("Category Implementation: ArrayList<Integer> using add(). Size: " + size);
        long startTime, endTime, duration;
        long sum;

        // Test 1: Without initial capacity (emphasizes resizing)
        System.out.println("  Variant: No initial capacity");
        startTime = System.nanoTime();
        ArrayList<Integer> arrayList = new ArrayList<>();
        sum = 0L;
        for (int i = 0; i < size; i++) {
            arrayList.add(i); // Potential resizing, boxing
        }
        // Separate summation after population
        for(Integer val : arrayList) { sum += val; }
        endTime = System.nanoTime();
        duration = TimeUnit.NANOSECONDS.toMillis(endTime - startTime);
        System.out.println("    Result: Sum = " + sum + ", Time = " + duration + " ms");
        arrayList = null; // Help GC

        // Test 2: With initial capacity (minimizes resizing)
        System.out.println("  Variant: With initial capacity");
        startTime = System.nanoTime();
        ArrayList<Integer> arrayListWithCap = new ArrayList<>(size);
        sum = 0L;
        for (int i = 0; i < size; i++) {
            arrayListWithCap.add(i); // Still boxing, less resizing
        }
        // Separate summation
        for(Integer val : arrayListWithCap) { sum += val; }
        endTime = System.nanoTime();
        duration = TimeUnit.NANOSECONDS.toMillis(endTime - startTime);
        System.out.println("    Result: Sum = " + sum + ", Time = " + duration + " ms");
        arrayListWithCap = null; // Help GC

        System.gc(); // Suggest GC
    }*/

    public static void main(String[] args) {

        /**
        * Here we are implementing the staic type array with 1M data
        * to manipulate and travers, we will measure that how much time
        * it will take for the static type array
        * Result: after running it takes 6 milliseconds
        * SS: https://prnt.sc/0FrQSfT43pqY
        * */

        /**
        Static Category: Storage allocated when the class is loaded
        (before main runs, effectively). Size must be known at compile
        time (or class loading time).
        */

        System.out.println("\n===== Starting Performance Comparisons =====");
        int size = 1000000; // 1M



        System.out.println("\n--- Performance Test: Static (Operational Speed) ---");
        System.out.println("Category Implementation: Simulating operations on pre-allocated fixed storage (using local int[]). Size: " + size);
        long startTime, endTime, duration;
        long sum;

        startTime = System.nanoTime();
        int[] staticArray = new int[size]; // Size 100 is fixed
        sum = 0L;
        for (int i = 0; i < size; i++) {
            staticArray[i] = i; //traverse and insert
            sum += staticArray[i]; //manipulate
        }
        endTime = System.nanoTime();
        duration = TimeUnit.NANOSECONDS.toMillis(endTime - startTime);
        System.out.println("  Result: Sum = " + sum + ", Time = " + duration + " ms");
        System.gc(); // Suggest GC




        // You can still call the demonstration methods if you like
        // Scanner scanner = new Scanner(System.in);
        // demonstrateStatic();
        // demonstrateFixedStackDynamic();
        // demonstrateStackDynamic(scanner);
        // demonstrateFixedHeapDynamic();
        // demonstrateHeapDynamic();
        // scanner.close();




//        int testSize1 = 100000;  // 100k
//        int testSize2 = 1000000; // 1M

//        System.out.println("\n*** Running tests, size: " + testSize1 + " ***");
//        checkPerformanceForStatic(testSize1);
//        checkPerformanceForFixedStackDynamic(testSize1);
//        checkPerformanceForStackDynamic(testSize1);
//        checkPerformanceForFixedHeapDynamic(testSize1);
//        checkPerformanceForHeapDynamic(testSize1); // Contains two variants inside

//        System.out.println("\n*** Running tests, size: " + testSize2 + " ***");
//        checkPerformanceForStatic(testSize2);
//        checkPerformanceForFixedStackDynamic(testSize2);
//        checkPerformanceForStackDynamic(testSize2);
//        checkPerformanceForFixedHeapDynamic(testSize2);
//        checkPerformanceForHeapDynamic(testSize2); // Contains two variants inside

        // Optional: Larger size - may require more heap memory via JVM options (e.g., -Xmx2g)
        // int testSize3 = 10000000; // 10M
        // System.out.println("\n*** Running tests for size: " + testSize3 + " ***");
        // checkPerformanceForStatic(testSize3);
        // checkPerformanceForFixedStackDynamic(testSize3);
        // checkPerformanceForStackDynamic(testSize3);
        // checkPerformanceForFixedHeapDynamic(testSize3);
        // checkPerformanceForHeapDynamic(testSize3);

        System.out.println("\n===== Performance Comparisons Complete =====");
    }
}