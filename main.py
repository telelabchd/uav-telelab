from Forwarder import Forwarder
def start():
    # Ml feed
    forwarder = Forwarder("5559", "5560")
    forwarder.connect()
    print("started basicfeed")

start()
