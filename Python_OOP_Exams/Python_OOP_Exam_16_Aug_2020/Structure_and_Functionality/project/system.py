from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:

    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):

        power_hardware = PowerHardware(name, capacity, memory)

        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):

        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):

        for hardware in System._hardware:

            if hardware.name == hardware_name:
                express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
                hardware.install(express_software)
                System._software.append(express_software)
                return

        return "Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):

        for hardware in System._hardware:

            if hardware.name == hardware_name:
                light_software = LightSoftware(name, capacity_consumption, memory_consumption)
                hardware.install(light_software)
                System._software.append(light_software)
                return
        return "Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):

        for hardware in System._hardware:
            if hardware.name == hardware_name:
                for software in System._software:
                    if software.name == software_name:

                        hardware.uninstall(hardware)
                        System._software.remove(software)
                        return
        return "Some of the components do not exist"

    @staticmethod
    def analyze():

        number_of_hardware_components = len(System._hardware)
        number_of_software_components = len(System._software)

        total_software_memory_consumption = 0
        total_hardware_memory = 0

        total_software_capacity_consumption = 0
        total_hardware_capacity = 0

        for software in System._software:

            total_software_capacity_consumption += software.capacity_consumption
            total_software_memory_consumption += software.memory_consumption

        for hardware in System._hardware:

            total_hardware_capacity += hardware.capacity
            total_hardware_memory += hardware.memory

        return f"System Analysis\n" \
               f"Hardware Components: {number_of_hardware_components}\n" \
               f"Software Components: {number_of_software_components}\n" \
               f"Total Operational Memory: {total_software_memory_consumption} / {total_hardware_memory}\n" \
               f"Total Capacity Taken: {total_software_capacity_consumption} / {total_hardware_capacity}"

    @staticmethod
    def system_split():
        pass
