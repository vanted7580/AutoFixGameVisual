
print("Created By @VANTED (https://github.com/vanted7580)")

import configparser
import wmi
import os
import shutil
import time
from pathlib import Path

print(Path().absolute())


c = wmi.WMI()

time.sleep(0.1)

product = c.Win32_BaseBoard()[0].Product
monitor = c.Win32_DesktopMonitor()[1].PNPDeviceID.rsplit("\\")[1]

monitor_manufacturer = monitor[0:len(monitor)-4]
monitor_code = monitor[-4:]

print("Model:", product)
print("Monitor:", monitor)

config = configparser.ConfigParser()
config_path = 'config.ini'
config.read(config_path)

GPU_CODES = {
    'INTEL_IGPU': config['GPU_CODE']['INTEL_IGPU'],
    'NVIDIA_GPU': config['GPU_CODE']['NVIDIA_GPU'],
    'AMD_GPU': config['GPU_CODE']['AMD_GPU'],
    'AMD_IGPU': config['GPU_CODE']['AMD_IGPU'],
}

SYSTEM_PATH = {
    'GameVisual': config['SYSTEM_PATH']['GameVisual'],
    'Color': config['SYSTEM_PATH']['Color'],
}

COLOR_PROFILE = {
    'CMDEF': 'CMDEF',
    'ColorGamut': ['ASUS_DCIP3.icm', 'ASUS_DisplayP3.icm', 'ASUS_sRGB.icm']
}

available_gpu = {
    'INTEL_IGPU': -1,
    'NVIDIA_GPU': -1,
    'AMD_GPU': -1,
    'AMD_IGPU': -1,
}

gpu_list = [
    ('Intel', 'Internal', 'INTEL_IGPU'),
    ('NVIDIA', 'Integrated RAMDAC', 'NVIDIA_GPU'),
    ('AMD', 'Integrated RAMDAC', 'AMD_GPU'),
    ('AMD', 'Internal', 'AMD_IGPU'),
]

for gpu in c.Win32_VideoController():
    gpu_name = str(gpu.AdapterCompatibility)
    gpu_dac = str(gpu.AdapterDACType)
    for dat in gpu_list:
        cur = True if gpu_name.find(dat[0]) != -1 else False
        dac = gpu_dac == dat[1]
        if cur and dac:
            available_gpu[dat[2]] = 0
            print("GPU found: " + gpu.Description + "")

profiles = []

cur_path = os.path.abspath(os.getcwd())

colro_entries = os.listdir(cur_path + '/color/')

for profile in colro_entries:
    for gpu in available_gpu:
        if available_gpu[gpu] <0 or available_gpu[gpu] > 1: continue

        screen = True if profile.find(monitor_code) != -1 else False
        gpu_code = True if profile.find(GPU_CODES[gpu]) != -1 else False
        CMDEF = True

        if available_gpu[gpu] == 1:
            CMDEF = True if profile.find(COLOR_PROFILE['CMDEF']) != -1 else False

        if screen and gpu_code and CMDEF:
            profiles.append(profile)
            available_gpu[gpu] =  available_gpu[gpu] + 1

time.sleep(0.1)

print("Available profile:", profiles)


if len(profiles) > 0:

    for profile in profiles:
        splits = profile.split('_')
        splits[0] = product
        new_name = ''
        for split in splits:
            new_name = new_name + split + "_"
        new_name = new_name[:-1]

        shutil.copy2(cur_path + '\\color\\' + profile, cur_path)

        try:
            os.rename(profile, new_name)
        except:
            os.remove(profile)

        shutil.copy2(cur_path + "\\" + new_name, SYSTEM_PATH['GameVisual'])

        if profile.find(COLOR_PROFILE['CMDEF']) != -1:
            shutil.copy2(cur_path + "\\" + new_name, SYSTEM_PATH['Color'])


    for color_gamut in COLOR_PROFILE['ColorGamut']:
        shutil.copy2(cur_path + '\\color\\' + color_gamut, SYSTEM_PATH['GameVisual'])

time.sleep(0.1)

print("Done")
time.sleep(2)
