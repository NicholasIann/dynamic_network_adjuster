function dynamic_network_adjuster_start {
    python3 $DEST/plugins/dynamic_network_adjuster/dynamic_network_adjuster.py
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
