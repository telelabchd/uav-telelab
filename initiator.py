
import os
from multiprocessing import Pool

processes = ("main.py", "main2.py","zmqser.py", "ml_sub_client.py")
#process_dict = {"main": "main.py", "main2": "main2.py","zmqser": "zmqser.py", "ml_sub_client": "ml_sub_client.py", "webserver": "webserver.py"}, "webserver.py"
#running_process = {}

def run_process(process):
    os.system('python {}'.format(process))

pool = Pool(processes=4)


pool.map(run_process, processes)

