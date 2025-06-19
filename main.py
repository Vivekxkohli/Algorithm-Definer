import tkinter as tk
from tkinter import scrolledtext, ttk
from ttkbootstrap import Style
import threading
import time

class AlgorithmExplanationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Algorithm Explanation")
        self.root.geometry("700x680")
        self.style = Style(theme="darkly")  # Modern Theme
        
        self.dark_mode = False  # Toggle for Dark Mode
        
        self.algorithm_details = {
            "bubble sort": (
                "Bubble Sort",
                "Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.",
                "Algorithm:\n\nbegin BubbleSort(arr)\nfor i from 0 to n-1\n   for j from 0 to n-i-1\n      if arr[j] > arr[j+1]\n         swap(arr[j], arr[j+1])\n   end for\nend for\nreturn arr\nend BubbleSort\n",
                "Example:\n\nInput: [5, 3, 8, 4, 2]\nOutput: [2, 3, 4, 5, 8]"
            ),
            "binary search": (
                "Binary Search",
                "Binary search is a fast search algorithm with time complexity O(log n). It works by repeatedly dividing in half the portion of the list that could contain the target value, until it finds the value or concludes that it is not present.",
                "Algorithm:\n\nbegin BinarySearch(arr, target)\nlow = 0, high = length(arr)-1\nwhile low <= high\n   mid = (low + high) // 2\n   if arr[mid] == target\n      return mid\n   else if arr[mid] < target\n      low = mid + 1\n   else\n      high = mid - 1\nend while\nreturn -1\nend BinarySearch",
                "Example:\n\nInput: [1, 3, 5, 7, 9, 11, 13]\nTarget: 7\nOutput: Found at index 3"
            ),
            "selection sort": (
                "Selection Sort",
                "Selection sort divides the list into a sorted and an unsorted region, repeatedly selecting the smallest element from the unsorted region and moving it to the sorted region.",
                "Algorithm:\n\nbegin SelectionSort(arr)\nn = length(arr)\nfor i from 0 to n-1\n   minIndex = i\n   for j from i+1 to n\n      if arr[j] < arr[minIndex]\n         minIndex = j\n   swap(arr[minIndex], arr[i])\nend for\nreturn arr\nend SelectionSort\n",
                "Example:\n\nInput: [64, 25, 12, 22, 11]\nOutput: [11, 12, 22, 25, 64]"
            ),
            "insertion sort": (
                "Insertion Sort",
                "Insertion sort builds a sorted list one element at a time, inserting each new element into its correct position.",
                "Algorithm:\n\nbegin InsertionSort(arr)\nn = length(arr)\nfor i from 1 to n-1\n   key = arr[i]\n   j = i - 1\n   while j >= 0 and arr[j] > key\n      arr[j+1] = arr[j]\n      j = j - 1\n   arr[j+1] = key\nend for\nreturn arr\nend InsertionSort\n",
                "Example:\n\nInput: [12, 11, 13, 5, 6]\nOutput: [5, 6, 11, 12, 13]"
            ),
            "merge sort": (
                "Merge Sort",
                "Merge sort is a divide and conquer algorithm that splits an array into halves, sorts each half, and merges the sorted halves.",
                "Algorithm:\n\nbegin MergeSort(arr)\nif length of arr <= 1\n   return arr\nmid = length(arr) / 2\nleft_half = MergeSort(first half of arr)\nright_half = MergeSort(second half of arr)\nreturn Merge(left_half, right_half)\nend MergeSort\n\nbegin Merge(left_half, right_half)\nresult = empty array\nwhile left_half is not empty and right_half is not empty\n   if first element of left_half <= first element of right_half\n      append first element of left_half to result\n      remove first element from left_half\n   else\n      append first element of right_half to result\n      remove first element from right_half\n   end if\nend while\nappend remaining elements of left_half to result\nappend remaining elements of right_half to result\nreturn result\nend Merge\n",
                "Example:\n\nInput: [38, 27, 43, 3, 9, 82, 10]\nOutput: [3, 9, 10, 27, 38, 43, 82]"
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

        # Thread control variables
        self.typewriter_thread = None  
        self.stop_typewriter = False   

        # Header
        self.header = tk.Label(root, text="Algorithm Explanation Tool", font=("Arial", 20, "bold"), fg="white", bg="#343a40", pady=15)
        self.header.pack(fill=tk.X)

        # Input Section
        self.input_frame = tk.Frame(root, bg="#222222", pady=10)
        self.input_frame.pack(fill=tk.X, padx=100)
        
        self.algorithm_entry = ttk.Entry(self.input_frame, width=40, style="info.TEntry")
        self.algorithm_entry.insert(0, "e.g., Bubble Sort, Binary Search")
        self.algorithm_entry.pack(side=tk.LEFT, padx=10, pady=5)
        
        self.algorithm_entry.bind("<Return>", lambda event: self.display_explanation())

        # Placeholder functionality
        self.algorithm_entry.bind("<FocusIn>", lambda event: self.clear_placeholder())
        self.algorithm_entry.bind("<FocusOut>", lambda event: self.restore_placeholder())

        self.submit_button = ttk.Button(self.input_frame, text="🔍 Search", style="success.TButton", command=self.display_explanation)
        self.submit_button.pack(side=tk.LEFT, padx=10)
        
        self.dark_mode_button = ttk.Button(self.input_frame, text="🌙 Dark Mode", style="primary.TButton", command=self.toggle_dark_mode)
        self.dark_mode_button.pack(side=tk.LEFT, padx=10)

        # Hint List
        self.hint_frame = tk.Frame(root, bg="#222222")
        self.hint_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.hint_label = tk.Label(self.hint_frame, text="Search Suggestions:", font=("Arial", 12, "bold"), bg="#222222", fg="white")
        self.hint_label.pack(anchor="w")

        self.hint_buttons = []
        hints = ["Bubble Sort", "Binary Search", "Depth First Search", "Kruskal's Algorithm"]
        for hint in hints:
            button = ttk.Button(self.hint_frame, text=hint, style="info.TButton", command=lambda h=hint: self.select_hint(h))
            button.pack(side=tk.LEFT, padx=5)
            self.hint_buttons.append(button)

        # Explanation Area
        self.explanation_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12), bd=2, relief=tk.FLAT, height=15)
        self.explanation_area.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)
        self.explanation_area.config(state=tk.DISABLED, bg="#282a36", fg="white")
        
    def clear_placeholder(self):
        """Clear the input field when focused."""
        if self.algorithm_entry.get() == "e.g., Bubble Sort, Binary Search":
            self.algorithm_entry.delete(0, tk.END)  
    
    def restore_placeholder(self):
        """Restore the placeholder text if the input field is empty."""
        if not self.algorithm_entry.get():
            self.algorithm_entry.insert(0, "e.g., Bubble Sort, Binary Search")
    
    def select_hint(self, hint):
        """Handle hint selection to populate the search bar **without auto-searching**."""
        self.algorithm_entry.delete(0, tk.END)
        self.algorithm_entry.insert(0, hint)

    def typewriter_effect(self, text):
        """Typewriter animation effect for explanation text with thread safety."""
        self.explanation_area.config(state=tk.NORMAL)
        self.explanation_area.delete(1.0, tk.END)  # Ensure fresh content
        
        self.stop_typewriter = False  

        for char in text:
            if self.stop_typewriter:  # If a new request comes in, stop typing
                return  
            self.explanation_area.insert(tk.END, char)
            self.explanation_area.update()
            time.sleep(0.01)  

        self.explanation_area.config(state=tk.DISABLED)

    def display_explanation(self):
        """Fetch and display the explanation with typewriter animation."""
        algorithm = self.algorithm_entry.get().strip().lower()

        if algorithm in self.algorithm_details:
            details = self.algorithm_details[algorithm]
            explanation_text = f"{details[0]}\n\n{details[1]}\n\n{details[2]}\n\n{details[3]}"
        else:
            explanation_text = f"Explanation for '{algorithm}' not found."

        # Stop previous thread safely
        self.stop_typewriter = True  
        if self.typewriter_thread and self.typewriter_thread.is_alive():
            self.typewriter_thread.join()  

        # Start a new thread
        self.typewriter_thread = threading.Thread(target=self.typewriter_effect, args=(explanation_text,), daemon=True)
        self.typewriter_thread.start()
    
    def toggle_dark_mode(self):
        """Toggle between dark and light mode."""
        if not self.dark_mode:
            self.root.configure(bg="#f8f9fa")
            self.header.config(bg="#f8f9fa", fg="black")
            self.input_frame.config(bg="#f8f9fa")
            self.hint_frame.config(bg="#f8f9fa")
            self.hint_label.config(bg="#f8f9fa", fg="black")
            self.explanation_area.config(bg="#ffffff", fg="black")
            self.dark_mode_button.config(text="☀ Light Mode", style="warning.TButton")
        else:
            self.root.configure(bg="#1e1e2e")
            self.header.config(fg="white", bg="#1e1e2e")
            self.input_frame.config(bg="#1e1e2e")
            self.hint_frame.config(bg="#1e1e2e")
            self.hint_label.config(bg="#1e1e2e", fg="white")
            self.explanation_area.config(bg="#282a36", fg="white")
            self.dark_mode_button.config(text="🌙 Dark Mode", style="primary.TButton")
        
        self.dark_mode = not self.dark_mode
    
if __name__ == "__main__":
    root = tk.Tk()
    app = AlgorithmExplanationGUI(root)
    root.mainloop()
