import time
import os
import psutil


class System_Usage:
    def __init__(self,unit: str="B", dir="/"):
        self.unit = unit.upper()
        self.dir = dir
    @property
    def time_convertor(self) -> float:
        if self.unit == 'sec':
            return round(1000,2)
    @property
    def unit_multiplier(self) -> int:
        if self.unit == 'TB':
            return 1024 ** 4
        elif self.unit == 'GB':
            return 1024 ** 3
        elif self.unit == 'MB':
            return 1024 ** 2
        elif self.unit == 'KB':
            return 1024
        else:
            return 1
    #TODO: Threading and these functions
    '''
    def timing(self,func) -> int:
        def wrapper(*args,**kwargs):
            self.start = time.perf_counter()
            result = func(*args,**kwargs)
            self.end = time.perf_counter()
            print(self.end - self.start)
            return result
        return wrapper
    '''
    def memory_info(self) -> dict:
        memory = psutil.virtual_memory()
        return {
            "total": memory.total / self.unit_multiplier,
            "available": memory.available / self.unit_multiplier,
            "free": memory.free / self.unit_multiplier,
            "percent": f'{memory.percent}%',
            "used": memory.used / self.unit_multiplier,
            "active": memory.active / self.unit_multiplier,
            "wired": memory.wired/ self.unit_multiplier
        }
    def storage_info(self):
        disk = psutil.disk_usage(self.dir)
        return {
            "total": disk.total / self.unit_multiplier,
            "used": disk.used / self.unit_multiplier,
            "free": disk.free / self.unit_multiplier,
            "percent": f'{disk.percent}%',
            "partitions": dict(enumerate(psutil.disk_partitions(all=True))),
            "disk_stats": psutil.disk_io_counters()._asdict(),
        }
    def swap_memory(self) -> dict:
        swap = psutil.swap_memory()
        return {
            "free":swap.free / self.unit_multiplier,
            "total":swap.total / self.unit_multiplier,
            "used": swap.total / self.unit_multiplier,
            "percent": f'{swap.percent}%',
            "swap_in": swap.sin / self.unit_multiplier,
            "swap_out": swap.sout / self.unit_multiplier,
        }
    def kernal_info(self) -> dict:
        kernal = os.uname()
        return{
            "kernal_version":kernal.release,
            "system_name":kernal.sysname,
            "node_name":kernal.nodename,
            "machine":kernal.machine,
        }
    #@timing
    def network_info(self)-> dict:
        network= psutil.net_io_counters()
        return{
            "send": network.bytes_sent / self.unit_multiplier,
            "recieve": network.bytes_recv/ self.unit_multiplier,
            "packets_recieve": network.packets_recv,
            "packets_send": network.packets_sent,
            "errin":network.errin,
            "errout":network.errout,
            "dropin":network.dropin,
            "dropout":network.dropout,
        }
    def network_info_sudo(self)-> dict:
        return{
            "net_connect": psutil.net_connections(),
            "net_addrs": psutil.net_if_addrs()._asdict(),
            "net_stats": psutil.net_if_stats()._asdict()
        }
    def cpu_info(self) -> dict:
        return{
        "physical_cores": psutil.cpu_count(logical=False),
        "total_cores": psutil.cpu_count(logical=True),
        "cpu_freq": psutil.cpu_freq()._asdict(),
        "cpu_stats": psutil.cpu_stats()._asdict(),
        "cpu_usage_per_core": dict(enumerate(psutil.cpu_percent(percpu=True,interval=0.1))),
        "cpu_percent": f'{psutil.cpu_percent(interval=0.1)}%',
        "cpu_spent_times": psutil.cpu_times()._asdict(),
        "cpu_spent_times_percent": psutil.cpu_times_percent()._asdict(),
        }
    def load_average(self) -> dict:
        load_average = psutil.getloadavg()
        return{
            "1min": load_average[0],
            "5min": load_average[1],
            "10min": load_average[2]
        }
    def time_of_file(self,file_path: str) -> float:
        start = time.perf_counter()
        with open(file_path,'r') as f:
            f.read();
        end = time.perf_counter()
        total = end - start
        return f"Time Elapsed: {total*1000:.2f}s"
    
'''  def machine_info(self) -> dict:
        return{
            "boot_time":psutil.boot_time() * self.time_convertor,
            "battery":psutil.sensors_battery(),
        }
'''
#print(System_Usage("GB").machine_info())