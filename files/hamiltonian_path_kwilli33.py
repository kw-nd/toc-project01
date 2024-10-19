import time
import csv
import numpy as np
import matplotlib.pyplot as plt
from itertools import permutations

# Function to check if a given path is a Hamiltonian path
# It ensures the path visits each vertex exactly once and that consecutive vertices are connected.
def is_hamiltonian_path(graph, path):
    visited = set(path)
    # If the number of unique vertices visited is less than the total number of vertices in the graph, it's not Hamiltonian.
    if len(visited) != len(graph):
        return False
    
    # Check each consecutive pair in the path to ensure they're connected in the graph
    for i in range(len(path) - 1):
        if path[i + 1] not in graph[path[i]]:
            return False
    return True

# Function to brute force all permutations of vertices to find a Hamiltonian path
def brute_force_hamiltonian(graph, num_vertices):
    # Get the list of vertices from the graph (keys are the vertices)
    vertex_list = list(graph.keys())
    # Generate all possible permutations of the vertices
    for perm in permutations(vertex_list):
        # Check if the current permutation is a Hamiltonian path
        if is_hamiltonian_path(graph, perm):
            return True, perm
    # Return false if no Hamiltonian path is found after trying all permutations
    return False, []

# Function to read a graph from a CNF-like CSV file
def read_graph_from_cnf(filename):
    graphs = []
    num_vertices_list = []

    # Open the CSV file and initialize the graph structure
    with open(filename, 'r', encoding='utf-8-sig') as csvfile:
        csv_reader = csv.reader(csvfile)
        graph = {}
        num_vertices = 0

        # Iterate through each row in the CSV file
        for row in csv_reader:
            # Skip comment lines or empty rows
            if not row or row[0].startswith('c'):
                if graph:
                    # Save the current graph and its number of vertices
                    graphs.append(graph)
                    num_vertices_list.append(num_vertices)
                # Reset for the next graph
                graph = {}
                num_vertices = 0
                continue
            # Skip header lines starting with 'p'
            if row[0].startswith('p'):
                continue

            try:
                # Convert the row into a list of integers (clause literals) and ignore zeros
                clause = list(map(int, filter(None, row)))
                clause = [literal for literal in clause if literal != 0]
                if not clause:
                    continue

                # Determine the number of vertices by taking the absolute max of literals
                num_vertices = max(num_vertices, *map(abs, clause))

                # Build the graph as an adjacency list (undirected)
                for i in range(len(clause)):
                    for j in range(i + 1, len(clause)):
                        u = abs(clause[i])
                        v = abs(clause[j])

                        if u not in graph:
                            graph[u] = []
                        if v not in graph:
                            graph[v] = []

                        # Add edges between u and v in both directions
                        if v not in graph[u]:
                            graph[u].append(v)
                        if u not in graph[v]:
                            graph[v].append(u)
            except ValueError as e:
                continue
        # Append the last graph after finishing file read
        if graph:
            graphs.append(graph)
            num_vertices_list.append(num_vertices)

    return graphs, num_vertices_list

# Function to test if a Hamiltonian path exists in the graph and measure execution time
def test_hamiltonian(graph, num_vertices):
    start_time = time.time()
    # Use brute force to find the Hamiltonian path
    found, path = brute_force_hamiltonian(graph, num_vertices)
    end_time = time.time()
    # Calculate execution time in microseconds
    exec_time = (end_time - start_time) * 1e6
    return found, path, exec_time

if __name__ == "__main__":
    # Main function to run the Hamiltonian path test cases and plot results
    def run_cases(csv_filename):
        sizes = []
        times = []
        colors = []

        # Read graphs from the provided CNF-like CSV file
        graphs, num_vertices_list = read_graph_from_cnf(csv_filename)
        
        plt.figure()

        # Process each graph and plot the results incrementally
        for i, graph in enumerate(graphs):
            num_vertices = num_vertices_list[i]
            found, path, exec_time = test_hamiltonian(graph, num_vertices)
            
            # Collect sizes, execution times, and set color (green for found, red for not found)
            sizes.append(num_vertices)
            times.append(exec_time)
            colors.append('green' if found else 'red')
            
            plt.clf()  # Clear the previous plot
            # Scatter plot to display time vs. graph size
            plt.scatter(sizes, times, c=colors, alpha=0.8, s=50, edgecolor='black')
            plt.title('Time to Find Hamiltonian Path vs. Graph Size')
            plt.xlabel('Number of Vertices')
            plt.ylabel('Time (µs)')
            plt.yscale('log')  # Log scale to better visualize time differences
            plt.xticks(ticks=sizes)

            # Plot the exponential equation as the points increase
            if len(sizes) > 2:
                sizes_np = np.array(sizes)
                times_np = np.array(times)

                try:
                    # Fit the points to an exponential curve using log transformation
                    a, b = np.polyfit(sizes_np, np.log(times_np), 1)
                    equation = f"y = exp({a:.2e} * x + {b:.2e})"
                    # Display the equation on the plot
                    plt.text(0.05, 0.95, equation, transform=plt.gca().transAxes, fontsize=10, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.5))
                except Exception as e:
                    print(f"Equation fit failed: {e}")

            # Save the current plot to a PNG file
            plt.savefig('plots_kwilli33.png')

        plt.close()

    csv_filename = 'data_kwilli33.cnf.csv'
    run_cases(csv_filename)