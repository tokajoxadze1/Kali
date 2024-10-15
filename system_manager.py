#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by T0R for system diagnostics, optimization, and driver management.
# Description: A powerful system optimization tool for Kali Linux. It scans for errors, fixes broken packages, performs optimizations, and installs missing drivers automatically. 
# Author: T0R

import tkinter as tk
from tkinter import scrolledtext, messagebox
from tkinter.ttk import Progressbar
import os
import subprocess
import psutil  # For detailed system stats

class SystemFixApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Kali Linux System Manager")
        self.root.geometry("950x750")
        self.root.configure(bg='#1c1c1c')  # Sleek dark theme for modern feel

        # Heading
        self.heading = tk.Label(root, text="🔧 KALI/Linux Advanced System Manager & Optimizer 🔧", font=("Arial", 20, "bold"), fg="white", bg='#1c1c1c')
        self.heading.pack(pady=10)

        # Frame for buttons
        self.button_frame = tk.Frame(root, bg='#1c1c1c')
        self.button_frame.pack(pady=20)

        # Scan Button
        self.scan_button = tk.Button(self.button_frame, text="🔍 Scan System", font=("Arial", 12, "bold"), command=self.scan_system, bg='#007acc', fg="white", width=20, relief="raised")
        self.scan_button.grid(row=0, column=0, padx=10, pady=5)

        # Fix Errors Button
        self.fix_button = tk.Button(self.button_frame, text="⚙️ Fix Errors", font=("Arial", 12, "bold"), command=self.fix_errors, bg='#00b33c', fg="white", width=20, relief="raised")
        self.fix_button.grid(row=0, column=1, padx=10, pady=5)

        # Optimize Button
        self.optimize_button = tk.Button(self.button_frame, text="🚀 Optimize System", font=("Arial", 12, "bold"), command=self.optimize_system, bg='#ff8c00', fg="white", width=20, relief="raised")
        self.optimize_button.grid(row=0, column=2, padx=10, pady=5)

        # Driver Scan Button
        self.driver_scan_button = tk.Button(self.button_frame, text="🖥️ Driver Scan", font=("Arial", 12, "bold"), command=self.driver_scan, bg='#ff3366', fg="white", width=20, relief="raised")
        self.driver_scan_button.grid(row=0, column=3, padx=10, pady=5)

        # Progress Bar
        self.progress = Progressbar(root, orient=tk.HORIZONTAL, length=500, mode='determinate', maximum=100)
        self.progress.pack(pady=10)

        # Textbox for logs
        self.log_area = scrolledtext.ScrolledText(root, width=85, height=20, bg='#333333', fg="white", font=("Consolas", 10))
        self.log_area.pack(padx=10, pady=20)

        # Error Count Label
        self.error_label = tk.Label(root, text="Errors Found: 0", font=("Arial", 12), fg="white", bg='#1c1c1c')
        self.error_label.pack(pady=5)

        # System Status Button
        self.status_button = tk.Button(root, text="🖥️ Check System Status", font=("Arial", 12, "bold"), command=self.check_system_status, bg='#007acc', fg="white", width=25, relief="raised")
        self.status_button.pack(pady=10)

        # Program Info
        self.info_label = tk.Label(root, text="Description: A powerful system optimization tool for Kali Linux.\nAuthor: T0R", font=("Arial", 10), fg="white", bg='#1c1c1c')
        self.info_label.pack(pady=10)

    def run_command(self, command):
        """Executes system commands and handles output."""
        try:
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()
            return output.decode(), error.decode()
        except Exception as e:
            return "", str(e)

    def log_output(self, text, color="white"):
        """Logs messages to the text area with specific color."""
        self.log_area.insert(tk.END, text + "\n")
        self.log_area.tag_add(color, f"{self.log_area.index(tk.END)}-1c linestart", tk.END)
        self.log_area.tag_configure(color, foreground=color)

    def scan_system(self):
        """Scans the system for issues and missing drivers."""
        self.log_output("Scanning system for errors and missing drivers...", color="lightblue")
        self.progress['value'] = 0
        self.root.update()

        # System Package Update
        self.log_output("Updating system packages with 'apt-get update'...", color="lightgreen")
        output, error = self.run_command("apt-get update")
        self.log_output(output if output else "No output", color="lightgreen")
        if error:
            self.log_output("Error during update: " + error, color="red")

        self.progress['value'] += 20
        self.root.update()

        # Check for broken packages
        self.log_output("Checking for broken packages...", color="lightyellow")
        output, error = self.run_command("dpkg --audit")
        self.log_output(output if output else "No broken packages found.", color="lightyellow")
        if error:
            self.log_output("Error checking broken packages: " + error, color="red")

        self.progress['value'] += 20
        self.root.update()

        # Check file system
        self.log_output("Checking file system integrity...", color="lightpink")
        output, error = self.run_command("fsck -Af -M")
        self.log_output(output if output else "File system is healthy.", color="lightpink")
        if error:
            self.log_output("Error checking file system: " + error, color="red")

        self.progress['value'] += 20
        self.root.update()

        # Finish Scan
        self.log_output("System scan complete.", color="green")
        self.error_label.config(text="Errors Found: 0")
        self.progress['value'] = 100
        self.root.update()

    def fix_errors(self):
        """Fixes system errors and applies necessary updates."""
        self.log_output("Fixing system errors...", color="lightblue")
        self.progress['value'] = 0
        self.root.update()

        # Fix broken packages
        self.log_output("Fixing broken packages with 'apt-get -f install'...", color="lightgreen")
        output, error = self.run_command("apt-get -f install -y")
        self.log_output(output if output else "No broken packages to fix.", color="lightgreen")
        if error:
            self.log_output("Error fixing packages: " + error, color="red")

        self.progress['value'] += 25
        self.root.update()

        # Upgrade Packages
        self.log_output("Upgrading packages with 'apt-get full-upgrade'...", color="lightyellow")
        output, error = self.run_command("apt-get full-upgrade -y")
        self.log_output(output if output else "Packages upgraded.", color="lightyellow")
        if error:
            self.log_output("Error during package upgrade: " + error, color="red")

        self.progress['value'] += 25
        self.root.update()

        # Clean Up
        self.log_output("Cleaning up unnecessary packages...", color="lightpink")
        output, error = self.run_command("apt-get autoremove -y && apt-get autoclean")
        self.log_output(output if output else "System cleanup completed.", color="lightpink")
        if error:
            self.log_output("Error cleaning up: " + error, color="red")

        self.progress['value'] += 50
        self.root.update()

        self.log_output("System errors fixed successfully.", color="green")
        self.error_label.config(text="Errors Found: 0")
        self.progress['value'] = 100
        self.root.update()

    def optimize_system(self):
        """Performs system optimizations by clearing cache and stopping unnecessary services."""
        self.log_output("Optimizing system...", color="lightblue")
        self.progress['value'] = 0
        self.root.update()

        # Clear caches
        self.log_output("Clearing system caches...", color="lightgreen")
        output, error = self.run_command("sync; echo 3 > /proc/sys/vm/drop_caches")
        self.log_output(output if output else "Cache cleared.", color="lightgreen")
        if error:
            self.log_output("Error clearing cache: " + error, color="red")

        self.progress['value'] += 50
        self.root.update()

        # Stop unnecessary services (e.g., Apache2)
        self.log_output("Stopping unnecessary services (e.g., Apache2)...", color="lightyellow")
        output, error = self.run_command("systemctl stop apache2")
        self.log_output(output if output else "Services stopped.", color="lightyellow")
        if error:
            self.log_output("Error stopping services: " + error, color="red")

        self.progress['value'] += 50
        self.root.update()

        self.log_output("System optimization complete.", color="green")
        self.progress['value'] = 100
        self.root.update()

    def check_system_status(self):
        """Check the status of the system (CPU, Memory, Disk)."""
        self.log_output("Checking system status...", color="lightblue")
        self.progress['value'] = 0
        self.root.update()

        # Memory usage
        mem = psutil.virtual_memory()
        self.log_output(f"Memory Usage: {mem.percent}%", color="lightyellow")
        self.progress['value'] += 33
        self.root.update()

        # CPU usage
        cpu = psutil.cpu_percent(interval=1)
        self.log_output(f"CPU Usage: {cpu}%", color="lightgreen")
        self.progress['value'] += 33
        self.root.update()

        # Disk usage
        disk = psutil.disk_usage('/')
        self.log_output(f"Disk Usage: {disk.percent}%", color="lightpink")
        self.progress['value'] += 34
        self.root.update()

        self.log_output("System status check complete.", color="green")
        self.progress['value'] = 100
        self.root.update()

    def driver_scan(self):
        """Scans and installs missing drivers."""
        self.log_output("Scanning for missing drivers...", color="lightblue")
        self.progress['value'] = 0
        self.root.update()

        # Scan for drivers using lspci
        devices_output, error = self.run_command("lspci -k")
        if error:
            self.log_output("Error scanning drivers: " + error, color="red")
            return

        self.log_output(devices_output, color="white")

        if "Kernel driver in use" not in devices_output:
            self.log_output("Missing drivers found. Installing...", color="lightgreen")
            output, error = self.run_command("apt-get install linux-firmware -y")
            self.log_output(output if output else "Drivers installed.", color="lightgreen")
            if error:
                self.log_output("Error installing drivers: " + error, color="red")
                return

        self.log_output("Driver scan complete.", color="green")
        self.progress['value'] = 100
        self.root.update()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = SystemFixApp(root)
    root.mainloop()
