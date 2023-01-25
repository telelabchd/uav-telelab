from Forwarder import Forwarder

def start():
    # Ml feed
    forwarder = Forwarder("5561", "5562")
    forwarder.connect()
    print("started ml feed")
start()