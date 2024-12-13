from flask import Flask, render_template
import psutil
import os

app = Flask(__name__)

def get_network_traffic():
    """ Ottieni il traffico di rete attivo (bytes inviati e ricevuti) """
    net_io = psutil.net_io_counters()
    return net_io.bytes_sent, net_io.bytes_recv

def get_qos_status():
    """ Restituisce lo stato attuale di QoS (per semplicità, lo stato è statico) """
    # Questo è solo un esempio: personalizza per integrare con il sistema di QoS effettivo
    return {
        'qos_active': True,
        'rate_limit': '100mbit',
        'buffer_size': '1600'
    }

@app.route('/')
def index():
    """ Visualizza la dashboard con i dati di traffico e QoS """
    traffic_sent, traffic_received = get_network_traffic()
    qos_status = get_qos_status()
    return render_template('index.html', traffic_sent=traffic_sent, traffic_received=traffic_received, qos_status=qos_status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
