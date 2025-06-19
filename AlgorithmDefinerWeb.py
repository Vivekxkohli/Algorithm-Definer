import streamlit as st

algorithm_details = {
    "bubble sort": (
        "Bubble Sort",
        "Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.",
        "Algorithm:\n\nbegin BubbleSort(arr)\nfor i from 0 to n-1\n   for j from 0 to n-i-1\n      if arr[j] > arr[j+1]\n         swap(arr[j], arr[j+1])\nend for\nreturn arr\nend BubbleSort\n",
        "Example:\n\nInput: [5, 3, 8, 4, 2]\n\nOutput: [2, 3, 4, 5, 8]"
    ),
    "binary search": (
        "Binary Search",
        "Binary search is a fast search algorithm with time complexity O(log n). It works by repeatedly dividing in half the portion of the list that could contain the target value, until it finds the value or concludes that it is not present.",
        "Algorithm:\n\nbegin BinarySearch(arr, target)\nlow = 0, high = length(arr)-1\nwhile low <= high\n   mid = (low + high) // 2\n   if arr[mid] == target\n      return mid\n   else if arr[mid] < target\n      low = mid + 1\n   else\n      high = high - 1\nend while\nreturn -1\nend BinarySearch",
        "Example:\n\nInput: [1, 3, 5, 7, 9, 11, 13]\nTarget: 7\n\nOutput: Found at index 3"
    ),
    "selection sort": (
        "Selection Sort",
        "Selection sort divides the list into a sorted and an unsorted region, repeatedly selecting the smallest element from the unsorted region and moving it to the sorted region.",
        "Algorithm:\n\nbegin SelectionSort(arr)\nn = length(arr)\nfor i from 0 to n-1\n   minIndex = i\n   for j from i+1 to n\n      if arr[j] < arr[minIndex]\n         minIndex = j\n   swap(arr[minIndex], arr[i])\nend for\nreturn arr\nend SelectionSort\n",
        "Example:\n\nInput: [64, 25, 12, 22, 11]\n\nOutput: [11, 12, 22, 25, 64]"
    ),
    "insertion sort": (
        "Insertion Sort",
        "Insertion sort builds a sorted list one element at a time, inserting each new element into its correct position.",
        "Algorithm:\n\nbegin InsertionSort(arr)\nn = length(arr)\nfor i from 1 to n-1\n   key = arr[i]\n   j = i - 1\n   while j >= 0 and arr[j] > key\n      arr[j+1] = arr[j]\n      j = j - 1\n   arr[j+1] = key\nend for\nreturn arr\nend InsertionSort\n",
        "Example:\n\nInput: [12, 11, 13, 5, 6]\n\nOutput: [5, 6, 11, 12, 13]"
    ),
    "merge sort": (
        "Merge Sort",
        "Merge sort is a divide and conquer algorithm that splits an array into halves, sorts each half, and merges the sorted halves.",
        "Algorithm:\n\nbegin MergeSort(arr)\nif length of arr <= 1\n   return arr\nmid = length(arr) / 2\nleft_half = MergeSort(first half of arr)\nright_half = MergeSort(second half of arr)\nreturn Merge(left_half, right_half)\nend MergeSort",
        "Example:\n\nInput: [38, 27, 43, 3, 9, 82, 10]\n\nOutput: [3, 9, 10, 27, 38, 43, 82]"
    ),
    "depth first search": (
        "Depth-First Search (DFS)",
        "A graph traversal algorithm that explores as far as possible along each branch before backtracking.",
        "Algorithm:\n\nbegin DFS(graph, start_node)\nvisited = empty set\nstack = empty stack\npush start_node onto stack\nwhile stack is not empty\n   node = pop from stack\n   if node is not visited\n      visit(node)\n      add node to visited\n      for each neighbor of node\n         if neighbor is not visited\n            push neighbor onto stack\nend while\nend DFS\n",
        "Example:\n\nUsed for solving maze problems and pathfinding in graphs."
    ),
    "breadth first search": (
        "Breadth-First Search (BFS)",
        "A graph traversal algorithm that explores all neighbor nodes at the present depth before moving on to the next depth level.",
        "Algorithm:\n\nbegin BFS(graph, start_node)\nvisited = empty set\nqueue = empty queue\nenqueue start_node onto queue\nwhile queue is not empty\n   node = dequeue from queue\n   if node is not visited\n      visit(node)\n      add node to visited\n      for each neighbor of node\n         if neighbor is not visited\n            enqueue neighbor onto queue\nend while\nend BFS\n",
        "Example:\n\nUsed for shortest path algorithms like in social networks or AI pathfinding."
    ),
    "dijkstra's algorithm": (
        "Dijkstra's Algorithm",
        "Finds the shortest path between nodes in a graph with non-negative edge weights.",
        "Algorithm:\n\nbegin Dijkstra(graph, start_node)\ndistances = map with initial distance of infinity for all nodes\nprevious = map with initial previous node of null for all nodes\nset distance of start_node to 0\npriority_queue = empty priority queue\nenqueue start_node with priority 0 onto priority_queue\nwhile priority_queue is not empty\n   current_node = dequeue from priority_queue\n   for each neighbor of current_node\n      new_distance = distance[current_node] + weight between current_node and neighbor\n      if new_distance < distance[neighbor]\n         set distance of neighbor to new_distance\n         set previous of neighbor to current_node\n         enqueue neighbor with priority new_distance onto priority_queue\nend while\nend Dijkstra\n",
        "Example:\n\nUsed in Google Maps to find the shortest route between locations."
    ),
    "kruskal's algorithm": (
        "Kruskal's Algorithm",
        "Finds a minimum spanning tree for a weighted graph by selecting edges in ascending order of weight.",
        "Algorithm:\n\nbegin Kruskal(graph)\nsort all edges in increasing order of weight\ninitialize an empty minimum spanning tree\nfor each edge in sorted edges\n   if adding edge to minimum spanning tree does not form a cycle\n      add edge to minimum spanning tree\nreturn minimum spanning tree\nend Kruskal\n",
        "Example:\n\nUsed in network design and clustering algorithms."
    )
}

# --- Streamlit App ---

st.set_page_config(page_title="Algorithm Explanation Tool", layout="centered")

st.title("🧮 Algorithm Explanation Tool")
st.write("Enter the name of an algorithm or choose a suggestion:")

# --- Hint buttons ---
hints = ["Bubble Sort", "Binary Search", "Depth First Search", "Kruskal's Algorithm"]
hint_clicked = st.columns(len(hints))

for i, hint in enumerate(hints):
    if hint_clicked[i].button(hint):
        st.session_state["algorithm_input"] = hint

# --- Search input ---
algorithm_input = st.text_input("Algorithm name:", st.session_state.get("algorithm_input", ""))
algorithm = algorithm_input.strip().lower()

# --- Display explanation ---
if st.button("🔍 Search"):
    if algorithm in algorithm_details:
        details = algorithm_details[algorithm]
        st.subheader(details[0])
        st.write(details[1])
        st.code(details[2], language="text")
        st.info(details[3])
    else:
        st.error(f"Explanation for '{algorithm}' not found.")
