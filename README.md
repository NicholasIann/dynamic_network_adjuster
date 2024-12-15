The Dynamic Network Adjuster project is a solution for real-time monitoring of network traffic in OpenStack environments. The plugin collects information about network traffic (specifically the virtual network used for Devstack), including bytes sent and received by network interfaces, and provides detailed statistics on network usage. The system also includes a Flask-based user interface, which allows administrators to view network traffic metrics in real time. It provides a complete overview of the network status, useful for resource management and planning.
Dynamic Network Adjuster consists of three main components:

1. Monitoring Plugin (dynamic_network_adjuster.py):
The heart of the system is a Python module that collects network traffic information from network interfaces using the psutil library.
The information collected includes bytes sent and received, and total network traffic.
It provides a real-time overview useful for monitoring.

2. User Interface (Flask Web UI - dynamic_network_adjuster_ui.py):
A Flask-based web application that provides a dashboard to visualize network traffic in real-time.
Users can see detailed statistics about data sent and received, with dynamic updates through a visual interface.
The UI is made in HTML, CSS and JavaScript.

3. Configuration Plugin (plugin.sh):
A script that automates the integration of the plugin into DevStack.
It configures the necessary dependencies and ensures that the plugin runs correctly during DevStack startup.

System Workflow:
Network Metrics Monitoring:
The monitoring plugin collects network traffic information using the psutil library, which provides the bytes sent and received by network interfaces. The data is collected in real time and presented for analysis.

Visualization via Flask Interface:
Network traffic information is visualized via the web interface developed with Flask. (dynamic_network_adjuster_ui.py)
The dashboard displays data in real time, allowing administrators to monitor network activity and make decisions based on observed metrics.

Technologies Used:
1. Python for plugin logic.
2. Psutil for monitoring network metrics.
3. Flask for building web UI.
4. OpenStack (DevStack) for cloud platform integration.
5. HTML/CSS/JavaScript for interactive data visualization.
