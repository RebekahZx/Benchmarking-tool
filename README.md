# Benchmarking-tool
This is a CPU benchmarking tool developed using the Tkinter library in Python. It allows users to assess the performance of their CPU by running a benchmarking task and calculating a score based on the time taken to complete the task.

The main features of the application include:

User interface with a window displaying the title "CPU Benchmark Tool" and a button to start the benchmarking process.
Input field for specifying the number of iterations for the benchmarking task.
Output field to display the benchmarking score after the task is completed.
Status message area to provide feedback on the progress of the benchmarking process.
Upon clicking the "Run Benchmark" button, the application initiates a benchmarking task that involves performing mathematical computations for a specified number of iterations. The elapsed time for completing the task is recorded, and a score is calculated based on the inverse of the elapsed time (lower time indicating better performance). This score is then displayed in the output field, along with a status message indicating the completion of the benchmarking process.

To ensure responsiveness and prevent the user interface from freezing during the benchmarking task, the task is executed in a separate thread using the threading module.

Overall, this CPU benchmarking tool provides a simple yet effective way for users to evaluate the performance of their CPU and make informed decisions about hardware upgrades or optimizations.
