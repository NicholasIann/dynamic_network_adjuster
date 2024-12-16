import psutil
import os
import time
from subprocess import call

def get_network_traffic():
    """ Ottieni il traffico di rete attivo (bytes inviati e ricevuti) """
    net_io = psutil.net_io_counters()
    return net_io.bytes_sent, net_io.bytes_recv

def adjust_qos(traffic_sent, traffic_received):
    """ Adatta le configurazioni di QoS in base al traffico di rete """
    if traffic_sent > 1000000000 or traffic_received > 1000000000:  # Se supera 1GB
        print("High network traffic detected. Adjusting QoS settings...")
        call(["tc", "qdisc", "add", "dev", "eth0", "root", "handle", "1:0", "tbf", "rate", "100mbit", "buffer", "1600", "limit", "3000"])
    else:
        print("Network traffic is normal. No adjustment needed.")

def monitor_and_adjust():
    """ Funzione per monitorare e regolare la rete periodicamente """
    while True:
        traffic_sent, traffic_received = get_network_traffic()
        adjust_qos(traffic_sent, traffic_received)
        time.sleep(10)  # Controlla ogni 10 secondi

if __name__ == "__main__":
    monitor_and_adjust()
