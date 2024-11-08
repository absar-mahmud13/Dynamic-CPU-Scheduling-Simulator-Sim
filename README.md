# Dynamic CPU Scheduling Simulator

A Python simulator for dynamic CPU scheduling algorithms, including **First-Come, First-Serve (FCFS)**, **Shortest Job First (SJF)**, and **Priority Scheduling**. This simulator calculates and displays important metrics such as turnaround time and waiting time for each process, and visualizes the process scheduling through Gantt charts.

## Features

- Implements three CPU scheduling algorithms: **FCFS**, **SJF**, and **Priority Scheduling**
- Calculates average turnaround and waiting times for each algorithm
- Visualizes scheduling order using Gantt charts for better understanding

## Getting Started

### Prerequisites

Make sure you have Python 3 installed and `matplotlib` for visualization.

To install `matplotlib`, run:
```bash
pip install matplotlib
```

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/dynamic-cpu-scheduling-simulator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd dynamic-cpu-scheduling-simulator
   ```

### Usage

1. Run the script:
   ```bash
   python dynamic_cpu_scheduling_simulator.py
   ```
2. Enter details for each process, including arrival time, burst time, and priority.

The program will display:
- Average turnaround and waiting times for each algorithm.
- Gantt charts for visualizing the execution order.

### Example Input

```
Enter the number of processes: 3

Enter details for Process 1
Arrival Time: 0
Burst Time: 4
Priority (higher number = higher priority): 2

Enter details for Process 2
Arrival Time: 1
Burst Time: 3
Priority (higher number = higher priority): 1

Enter details for Process 3
Arrival Time: 2
Burst Time: 5
Priority (higher number = higher priority): 3
```

### Example Output

```
FCFS Scheduling:
Average Turnaround Time: 7.33
Average Waiting Time: 4.0

SJF Scheduling:
Average Turnaround Time: 6.67
Average Waiting Time: 3.33

Priority Scheduling:
Average Turnaround Time: 6.0
Average Waiting Time: 2.67
```

Each algorithm also generates a Gantt chart for the execution sequence.
## Output:
![1](https://github.com/user-attachments/assets/cd3bc90a-badc-4a73-8fb2-ca2d62c93ea9)

![FCFS](https://github.com/user-attachments/assets/d37ea6ed-0fef-4c71-9034-551a475008cf)

![Priority](https://github.com/user-attachments/assets/abb91d8a-c54b-4f1c-b539-4c1029b75962)

![SJF](https://github.com/user-attachments/assets/b683379f-0f27-4084-8ba6-87982730e554)


## Files

- `dynamic_cpu_scheduling_simulator.py`: Main script implementing the simulator.
- `README.md`: Documentation for the project.
- `sample_output.txt`: Example output for different sample inputs.

## License

This project is licensed under the MIT License.

