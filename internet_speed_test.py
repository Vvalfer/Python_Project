import speedtest

def test_internet_speed():
    st = speedtest.Speedtest()

    st.download()
    st.upload()

    download_speed = st.results.download() / 1_000_000
    print(f"Download Speed : {download_speed:.2f} Mbps")

    upload_speed = st.results.upload() / 1_000_000
    print(f"upload Speed : {upload_speed:.2f} Mbps")

    server = st.get_best_server()
    ping = server["latency"]
    print(f"Ping: {ping} ms")
    
test_internet_speed()
