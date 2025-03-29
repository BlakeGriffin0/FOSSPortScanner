# GUI for Python
# Importing the tkinter module
import tkinter as tk
from tkinter import ttk
import socket  # Import socket for port scanning

# Create the root window (top-level window)
root = tk.Tk()
root.title("Home FOSS Port Scanner")
root.geometry("600x600") #window size
root.resizable(True, True) #allow resizing
# Create a frame and add it to the root window
frame = ttk.Frame(root, padding="10 10 10 10")
frame.pack(fill=tk.BOTH, expand=True)



# Adding functionality to scan open ports
def scan_ports():
    ip = ip_entry.get()
    try:
        start_port = int(start_port_entry.get())
        end_port = int(end_port_entry.get())
    except ValueError:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Invalid port range. Please enter valid integers.\n")
        return

    # Show the loading indicator
    loading_label.config(text="Scanning...")
    loading_label.update_idletasks()

    result_text.delete("1.0", tk.END)  # Clear previous results
    result_text.insert(tk.END, f"Scanning IP: {ip}, Ports: {start_port}-{end_port}\n")
    result_text.update_idletasks()

    open_ports_found = False  # Track if any open ports are found

    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                if s.connect_ex((ip, port)) == 0:
                    open_ports_found = True
                    try:
                        service = socket.getservbyport(port)
                    except OSError:
                        service = "Unknown service"
                    result_text.insert(tk.END, f"Port {port} is open (Service: {service})\n")
        except Exception as e:
            result_text.insert(tk.END, f"Error scanning port {port}: {e}\n")
        result_text.update_idletasks()

    if not open_ports_found:
        result_text.insert(tk.END, "All ports are closed.\n")

    # Hide the loading indicator after the scan is complete
    loading_label.config(text="Scan complete.")
    loading_label.update_idletasks()

# Adding input fields and labels for IP and port range
ip_label = ttk.Label(frame, text="IP Address:")
ip_label.pack()
ip_entry = ttk.Entry(frame)
ip_entry.pack()

start_port_label = ttk.Label(frame, text="Start Port:")
start_port_label.pack()
start_port_entry = ttk.Entry(frame)
start_port_entry.pack()

end_port_label = ttk.Label(frame, text="End Port:")
end_port_label.pack()
end_port_entry = ttk.Entry(frame)
end_port_entry.pack()

# Adding a button to trigger the port scan
scan_button = ttk.Button(frame, text="Scan Ports", command=scan_ports)
scan_button.pack()

# Adding a text widget to display scan results
result_text = tk.Text(frame, height=8, width=40)
result_text.pack()

# Adding a loading indicator label
loading_label = ttk.Label(frame, text="")
loading_label.pack()

# Make the buttons visible


# Start the main event loop
root.mainloop()