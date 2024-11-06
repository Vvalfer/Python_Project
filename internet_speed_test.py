import speedtest

def test_internet_speed():
    st = speedtest.Speedtest()

    # Obtenez une liste de serveurs
    servers = st.get_servers()
    
    # Choisissez le meilleur serveur parmi la liste
    best_server = st.get_best_server(servers)
    
    st.download()
    st.upload()

    download_speed = st.results.download / 1_000_000
    print(f"Download Speed : {download_speed:.2f} Mbps")

    upload_speed = st.results.upload / 1_000_000
    print(f"Upload Speed : {upload_speed:.2f} Mbps")

    ping = best_server["latency"]
    print(f"Ping: {ping} ms")
    
test_internet_speed()
