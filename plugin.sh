#!/bin/bash

function dynamic_network_adjuster_install {
    echo "Installing Dynamic Network Adjuster Plugin..."
    pip install psutil flask
}

function dynamic_network_adjuster_start {
    # Avvia il monitoraggio della rete in background
    python3 $DEST/plugins/dynamic_network_adjuster/dynamic_network_adjuster.py &

    # Avvia la UI Flask
    python3 $DEST/plugins/dynamic_network_adjuster/ui/dynamic_network_adjuster_ui.py &
}

if [[ "$1" == "stack" ]]; then
    case "$2" in
        install)
            dynamic_network_adjuster_install
            ;;
        post-config)
            dynamic_network_adjuster_start
            ;;
    esac
fi

