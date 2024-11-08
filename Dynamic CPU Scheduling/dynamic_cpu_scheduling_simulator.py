# -*- coding: utf-8 -*-
"""Dynamic CPU Scheduling Simulator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CGIIOt3GJRXqnc2um0cDeafQ934_nSj3
"""

import matplotlib.pyplot as plt

# Define a class for Process
class Process:
    def __init__(self, process_id, arrival_time, burst_time, priority):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

# First-Come, First-Serve (FCFS) Scheduling
def fcfs(processes):
    processes.sort(key=lambda x: x.arrival_time)  # Sort by arrival time
    current_time = 0
    for process in processes:
        current_time = max(current_time, process.arrival_time) + process.burst_time
        process.completion_time = current_time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
    return processes

# Shortest Job First (SJF) Scheduling
def sjf(processes):
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))  # Sort by arrival time, then by burst time
    current_time = 0
    completed = []
    while processes:
        available = [p for p in processes if p.arrival_time <= current_time]
        if available:
            shortest = min(available, key=lambda x: x.burst_time)
            processes.remove(shortest)
            current_time += shortest.burst_time
            shortest.completion_time = current_time
            shortest.turnaround_time = shortest.completion_time - shortest.arrival_time
            shortest.waiting_time = shortest.turnaround_time - shortest.burst_time
            completed.append(shortest)
        else:
            current_time += 1  # Increment time if no process is ready
    return completed

# Priority Scheduling
def priority_scheduling(processes):
    processes.sort(key=lambda x: (x.arrival_time, -x.priority))  # Sort by arrival time, then by priority
    current_time = 0
    completed = []
    while processes:
        available = [p for p in processes if p.arrival_time <= current_time]
        if available:
            highest_priority = max(available, key=lambda x: x.priority)
            processes.remove(highest_priority)
            current_time += highest_priority.burst_time
            highest_priority.completion_time = current_time
            highest_priority.turnaround_time = highest_priority.completion_time - highest_priority.arrival_time
            highest_priority.waiting_time = highest_priority.turnaround_time - highest_priority.burst_time
            completed.append(highest_priority)
        else:
            current_time += 1
    return completed

# Function to calculate and print the metrics
def calculate_metrics(processes):
    total_turnaround_time = sum(p.turnaround_time for p in processes)
    total_waiting_time = sum(p.waiting_time for p in processes)
    avg_turnaround_time = total_turnaround_time / len(processes)
    avg_waiting_time = total_waiting_time / len(processes)
    return avg_turnaround_time, avg_waiting_time

# Function to visualize the Gantt Chart
def visualize_gantt_chart(processes, algorithm_name):
    fig, ax = plt.subplots(figsize=(10, 2))
    start_time = 0
    for process in processes:
        ax.broken_barh([(start_time, process.burst_time)], (10, 9), facecolors=('tab:blue'))
        ax.text(start_time + process.burst_time / 2, 14, f"P{process.process_id}", ha='center')
        start_time += process.burst_time
    ax.set_xlabel('Time')
    ax.set_yticks([15])
    ax.set_yticklabels([algorithm_name])
    ax.grid(True)
    plt.show()

# Function to simulate scheduling and report
def simulate_scheduling(process_list):
    # FCFS Simulation
    fcfs_processes = fcfs(process_list.copy())
    fcfs_avg_tat, fcfs_avg_wt = calculate_metrics(fcfs_processes)
    print("FCFS Scheduling:")
    print("Average Turnaround Time:", fcfs_avg_tat)
    print("Average Waiting Time:", fcfs_avg_wt)
    visualize_gantt_chart(fcfs_processes, "FCFS")

    # SJF Simulation
    sjf_processes = sjf(process_list.copy())
    sjf_avg_tat, sjf_avg_wt = calculate_metrics(sjf_processes)
    print("\nSJF Scheduling:")
    print("Average Turnaround Time:", sjf_avg_tat)
    print("Average Waiting Time:", sjf_avg_wt)
    visualize_gantt_chart(sjf_processes, "SJF")

    # Priority Scheduling Simulation
    priority_processes = priority_scheduling(process_list.copy())
    priority_avg_tat, priority_avg_wt = calculate_metrics(priority_processes)
    print("\nPriority Scheduling:")
    print("Average Turnaround Time:", priority_avg_tat)
    print("Average Waiting Time:", priority_avg_wt)
    visualize_gantt_chart(priority_processes, "Priority")

# Function to get user input for processes
def get_user_input():
    process_list = []
    num_processes = int(input("Enter the number of processes: "))
    for i in range(num_processes):
        print(f"\nEnter details for Process {i + 1}")
        process_id = i + 1
        arrival_time = int(input("Arrival Time: "))
        burst_time = int(input("Burst Time: "))
        priority = int(input("Priority (higher number = higher priority): "))
        process = Process(process_id, arrival_time, burst_time, priority)
        process_list.append(process)
    return process_list

# Main execution
if __name__ == "__main__":
    process_list = get_user_input()
    simulate_scheduling(process_list)