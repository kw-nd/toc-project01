import hamiltonian_path_kwilli33

def run_tests():
    test_cases = [
        {
            "name": "Test 1 (Connected - Has Hamiltonian Path, Size 4)",
            "graph": {1: [2], 2: [1, 3], 3: [2, 4], 4: [3, 1]},
            "expected": True
        },
        {
            "name": "Test 2 (Connected - Has Hamiltonian Path, Size 6)",
            "graph": {1: [2, 3], 2: [1, 4], 3: [1, 4], 4: [2, 3, 5], 5: [4, 6], 6: [5, 1]},
            "expected": True
        },
        {
            "name": "Test 3 (Connected - Has Hamiltonian Path, Size 8)",
            "graph": {1: [2, 8], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4, 6], 6: [5, 7], 7: [6, 8], 8: [1, 7]},
            "expected": True
        },
        {
            "name": "Test 4 (Connected - Has Hamiltonian Path, Size 10)",
            "graph": {1: [2, 10], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4, 6], 6: [5, 7], 7: [6, 8], 8: [7, 9], 9: [8, 10], 10: [9, 1]},
            "expected": True
        },
        {
            "name": "Test 5 (Disconnected - No Hamiltonian Path, Size 4)",
            "graph": {1: [2], 2: [1], 3: [4], 4: [3]},
            "expected": False
        },
        {
            "name": "Test 6 (Disconnected - No Hamiltonian Path, Size 6)",
            "graph": {1: [2], 2: [1], 3: [4, 5], 4: [3], 5: [3], 6: []},
            "expected": False
        },
        {
            "name": "Test 7 (Disconnected - No Hamiltonian Path, Size 8)",
            "graph": {1: [2, 3], 2: [1], 3: [1], 4: [5], 5: [4, 6], 6: [5], 7: [8], 8: [7]},
            "expected": False
        },
        {
            "name": "Test 8 (Disconnected - No Hamiltonian Path, Size 12)",
            "graph": {1: [2], 2: [1], 3: [4], 4: [3], 5: [6], 6: [5], 7: [8], 8: [7], 9: [10], 10: [9], 11: [12], 12: [11]},
            "expected": False
        }
    ]

    for test_case in test_cases:
        graph = test_case["graph"]
        expected = test_case["expected"]

        found, _, exec_time = hamiltonian_path_kwilli33.test_hamiltonian(graph, len(graph))

        result = "found" if found else "not found"
        expected_result = "found" if expected else "not found"

        print(f"{test_case['name']}:")
        print(f"    Hamiltonian Path {result}")
        print(f"    Expected {expected_result}")
        print(f"    Time: {exec_time:.2f} µs")
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    run_tests()
