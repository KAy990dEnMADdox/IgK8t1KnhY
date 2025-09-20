# 代码生成时间: 2025-09-20 13:52:57
import psutil
import pandas as pd
import os

"""
Process Manager - A simple program to manage system processes using Python and Pandas

This program allows users to list processes, kill processes, and view the system's CPU usage.
"""

class ProcessManager:
    """
    ProcessManager class to interact with system processes
    """

    def __init__(self):
        """
        Initializes the ProcessManager instance
        """
        pass

    def list_processes(self):
        """
        Lists all running processes and returns a DataFrame
        """
        try:
            processes = []
            for proc in psutil.process_iter(['pid', 'name', 'status', 'create_time', 'memory_percent']):
                try:
                    proc_info = proc.info
                    processes.append(proc_info)
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    continue
            df = pd.DataFrame(processes)
            return df
        except Exception as e:
            print(f"Error listing processes: {e}")

    def kill_process(self, pid):
        """
        Kills a process by its PID
        """
        try:
            process = psutil.Process(pid)
            process.terminate()
            process.wait()
            print(f"Process {pid} terminated")
        except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
            print(f"Error terminating process {pid}: {e}")

    def get_cpu_usage(self):
        """
        Returns the current CPU usage percentage
        """
        return psutil.cpu_percent(interval=1)

# Example usage
if __name__ == '__main__':
    manager = ProcessManager()

    # List all processes
    processes_df = manager.list_processes()
    print(processes_df)

    # Get CPU usage
    cpu_usage = manager.get_cpu_usage()
    print(f"Current CPU usage: {cpu_usage}%")

    # Kill a process by PID (replace 1234 with the actual PID)
    manager.kill_process(1234)
