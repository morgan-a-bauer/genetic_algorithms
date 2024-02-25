"""
test_objective_funcs.py
Morgan Bauer
22 February 2024

Tests for objective_funcs.py in homework 01 for CS-470 Evolutionary Computation
pledged
"""
from objective_funcs import objective_func_1, objective_func_2, objective_func_3

if __name__ == "__main__":
    print("=" * 100)
    print("Testing objective_func_1()")
    print("\nobjective_function_1(2 ** 30 - 1, 2 ** 30 - 1, 10)")
    print("Expected: 1.0")
    print("Observed:", objective_func_1(2 ** 30 - 1, 2 ** 30 - 1, 10))
    print("\nobjective_function_1(0, 2 ** 30 - 1, 10)")
    print("Expected: 0.0")
    print("Observed:", objective_func_1(0, 2 ** 30 - 1, 10))
    print("\nobjective_function_1(20475, 2 ** 30 - 1, 10)")
    print("Expected: 6.3568272464368e-48")
    print("Observed:", objective_func_1(20475, 2 ** 30 - 1, 10))
    print("\nobjective_function_1(2 ** 30 - 2, 2 ** 30 - 1, 10)")
    print("Expected: 0.9999999906867743")
    print("Observed:", objective_func_1(2 ** 30 - 2, 2 ** 30 - 1, 10))
    print("\nobjective_func_1() tests complete")
    print("=" * 100)
    print("Testing objective_func_2()")
    print("\nobjective_function_2(2 ** 30 - 1, 2 ** 30 - 1)")
    print("Expected: 0.0")
    print("Observed:", objective_func_2(2 ** 30 - 1, 2 ** 30 - 1))
    print("\nobjective_function_2(0, 2 ** 30 - 1)")
    print("Expected: 0.0")
    print("Observed:", objective_func_2(0, 2 ** 30 - 1))
    print("\nobjective_function_2(493921239, 2 ** 30 - 1)")
    print("Expected: 0.2367417599987327")
    print("Observed:", objective_func_2(493921239, 2 ** 30 - 1))
    print("\nobjective_function_2(889058229, 2 ** 30 - 1)")
    print("Expected: 0.8389920245747362")
    print("Observed:", objective_func_2(889058229, 2 ** 30 - 1))
    print("\nobjective_func_2() tests complete")
    print("=" * 100)
    print("Testing objective_func_3()")
    print("\nobjective_function_3(2 ** 30 - 1, 2 ** 30 - 1)")
    print("Expected: 1.9899020385619612")
    print("Observed:", objective_func_3(2 ** 30 - 1, 2 ** 30 - 1))
    print("\nobjective_function_3(0, 2 ** 30 - 1)")
    print("Expected: 2.0")
    print("Observed:", objective_func_3(0, 2 ** 30 - 1))
    print("\nobjective_function_3(562209904, 2 ** 30 - 1)")
    print("Expected: 2.598076211353316")
    print("Observed:", objective_func_3(562209904, 2 ** 30 - 1))
    print("\nobjective_function_3(840739847, 2 ** 30 - 1)")
    print("Expected: 2.417589505802252")
    print("Observed:", objective_func_3(840739847, 2 ** 30 - 1))
    print("\nobjective_func_3() tests complete")