import tkinter as tk
import time
import math
import threading

class CPUBenchmarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CPU Benchmark Tool")
        self.root.geometry("500x350")  # Set the window size
        self.root.configure(bg="#F4EEEE")  # Set background color

        self.iterations_var = tk.IntVar(value=10)
        self.score_var = tk.StringVar(value="")
        self.status_var = tk.StringVar(value="")

        self.create_widgets()

    def create_widgets(self):
        header_label = tk.Label(self.root, text="CPU Benchmark Tool", font=(
            "Arial", 20, "bold"), bg="#F4EEEE", fg="#2D2D2D")
        header_label.pack(pady=15)

        iterations_frame = tk.Frame(self.root, bg="#F4EEEE")
        iterations_frame.pack()

        iterations_label = tk.Label(iterations_frame, text="Iterations:", font=(
            "Arial", 14), bg="#F4EEEE", fg="#2D2D2D")
        iterations_label.pack(side="left", padx=10)

        iterations_entry = tk.Entry(
            iterations_frame, textvariable=self.iterations_var, font=("Arial", 14), width=5)
        iterations_entry.pack(side="left")

        run_button = tk.Button(self.root, text="Run Benchmark", command=self.run_benchmark, font=(
            "Arial", 14), bg="#2D2D2D", fg="white")
        run_button.pack(pady=20)

        result_frame = tk.Frame(self.root, bg="#F4EEEE")
        result_frame.pack()

        score_label = tk.Label(result_frame, text="Score:", font=(
            "Arial", 16, "bold"), bg="#F4EEEE", fg="#2D2D2D")
        score_label.pack()

        self.score_label = tk.Label(result_frame, textvariable=self.score_var, font=(
            "Arial", 16), bg="#F4EEEE", fg="#2D2D2D")
        self.score_label.pack()

        status_label = tk.Label(self.root, textvariable=self.status_var, font=(
            "Arial", 12), bg="#F4EEEE", fg="#B77F7F")  # Adjusted color
        status_label.pack()

    def run_benchmark(self):
        iterations = self.iterations_var.get()
        self.score_var.set("")
        self.status_var.set("Running benchmark...")

        def benchmark_task():
            start_time = time.time()

            for _ in range(iterations):
                result = 0
                for i in range(1, 1000000):
                    result += math.sqrt(i)

            end_time = time.time()
            elapsed_time = end_time - start_time

            # Scoring mechanism: Lower time is better
            score = 1 / elapsed_time

            self.score_var.set(f"Score: {score:.2f}")
            self.status_var.set("Benchmark completed.")

        thread = threading.Thread(target=benchmark_task)
        thread.start()

def main():
    root = tk.Tk()
    app = CPUBenchmarkApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()