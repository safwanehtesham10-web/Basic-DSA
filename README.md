# Python DSA Practice Suite

A structured repository containing clean, minimal Python implementations of essential data structures and algorithmic patterns. Each file is an autonomous script containing its function definition and test execution block.

---

## Repository Layout

```text
.
├── problem_001_print_1_to_n_recursion.py
├── problem_002_factorial_of_n.py
├── problem_003_fibonacci_number.py
├── problem_004_sum_of_digits.py
├── problem_005_power_of_number.py
├── problem_006_check_sorted_array.py
├── problem_007_subsequences_of_string.py
├── problem_008_tower_of_hanoi.py
├── problem_009_permutations_of_string.py
├── problem_010_subset_sum.py
├── problem_011_first_and_last_occurrence.py
├── problem_012_count_occurrences.py
├── problem_013_floor_and_ceil.py
├── problem_014_search_insert_position.py
├── problem_015_merge_sorted_arrays.py
├── problem_016_valid_parentheses.py
├── problem_017_next_greater_element.py
├── problem_018_min_stack.py
├── problem_019_reverse_stack_recursion.py
├── problem_020_remove_duplicates_linked_list.py
└── README.md
```

---

## Topic Breakdown

### 1. Recursion & Combinatorics
Focuses on stack frame traversal, base condition handling, and branching decision trees.

* **[Problem 001: 1 to N Sequence](problem_001_print_1_to_n_recursion.py)** — Natural number printing via call stack unwind.
* **[Problem 002: Factorial Calculation](problem_002_factorial_of_n.py)** — Product accumulation through recursive reduction.
* **[Problem 003: Fibonacci Evaluation](problem_003_fibonacci_number.py)** — Dual-branch recursion computing the $k$-th term.
* **[Problem 004: Digit Summation](problem_004_sum_of_digits.py)** — Decimal decomposition utilizing modulus and floor division.
* **[Problem 005: Exponentiation](problem_005_power_of_number.py)** — Linear exponent reduction for integer powers.
* **[Problem 006: Array Monotonicity](problem_006_check_sorted_array.py)** — In-place index stepping to verify non-decreasing order without slicing.
* **[Problem 007: String Subsequences](problem_007_subsequences_of_string.py)** — State tree branching by character inclusion/exclusion.
* **[Problem 008: Tower of Hanoi](problem_008_tower_of_hanoi.py)** — Classic 3-peg recursive disk transposition.
* **[Problem 009: String Permutations](problem_009_permutations_of_string.py)** — Systematic generation of all character arrangements.
* **[Problem 010: Subset Sum Target](problem_010_subset_sum.py)** — Backtracking search for target summation in integer subsets.

### 2. Searching & Two-Pointer Mechanics
Techniques for interval reduction, linear traversal, and sorted array merging.

* **[Problem 011: First and Last Occurrences](problem_011_first_and_last_occurrence.py)** — Logarithmic boundary search with dual binary search passes.
* **[Problem 012: Frequency in Sorted Array](problem_012_count_occurrences.py)** — Early-exit single-pass counting for target value instances.
* **[Problem 013: Boundary Search (Floor & Ceil)](problem_013_floor_and_ceil.py)** — Finding greatest predecessor and least successor values.
* **[Problem 014: Search Insertion Point](problem_014_search_insert_position.py)** — Standard binary search returning insertion indices.
* **[Problem 015: Merging Ordered Lists](problem_015_merge_sorted_arrays.py)** — Dual pointer merge procedure running in linear time.

### 3. Linear Structures (Stacks & Linked Lists)
Implementation of dynamic LIFO buffers and singly-linked list node pointers.

* **[Problem 016: Balanced Bracket Verification](problem_016_valid_parentheses.py)** — Hash-map matching using a stack accumulator.
* **[Problem 017: Monotonic Stack (Next Greater)](problem_017_next_greater_element.py)** — Monotonically decreasing stack to discover next greater values.
* **[Problem 018: Constant-Time Min Stack](problem_018_min_stack.py)** — Class implementation maintaining minimum value history in $O(1)$ time.
* **[Problem 019: In-Place Recursive Stack Inversion](problem_019_reverse_stack_recursion.py)** — Reversing stack order without allocating auxiliary data structures.
* **[Problem 020: Deduplication in Linked List](problem_020_remove_duplicates_linked_list.py)** — Pointer manipulation skipping redundant contiguous nodes.

---

## Running the Solutions

### Prerequisites
* Python 3.8 or higher. No external libraries required.

### Single Program Execution
Run any specific file by passing its path to the Python interpreter:

```bash
python problem_014_search_insert_position.py
```

### Batch Execution (Run All)

**PowerShell (Windows):**
```powershell
Get-ChildItem -Filter "problem_*.py" | ForEach-Object {
    Write-Host "`n>>> Running $($_.Name)..." -ForegroundColor Cyan
    python $_.FullName
}
```

**Bash / Linux / macOS:**
```bash
for file in problem_*.py; do
    echo -e "\n>>> Running $file..."
    python3 "$file"
done
```
