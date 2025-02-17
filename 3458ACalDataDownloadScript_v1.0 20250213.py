# HP / Agilent / Keysight 3458A Cal Constants Downloader
# Near Far Media - v1.0 20250212
# License: MIT - https://opensource.org/license/MIT

import pyvisa  # For GPIB
import sys     # For exit
import time    # For sleep

print("---------------------------------------------------")
print("|       HP 3458A Calibration Data Downloader      |")
print("|         Near Far Media - v1.0 20250113          |")
print("---------------------------------------------------\n")
print("This script will allow you to download the")
print("calibration data in your 3458A Multimeter.\n")
print("Ensure you have 'Keysight IO Libraries Suite' installed")
print("if using a 83257B USB-GPIB adapter, or the National")
print("Instruments 'NI-488.2' software package installed if")
print("using an NI GPIB-USB-HS adapter.")
print("Other GPIB adapters may work, but I didn't check.")
print("Python 3 and PyVISA must also be installed.")
print("Ensure the 3458A is powered on, connected to the PC")
print("and visible in the respective software package.\n")

rm = pyvisa.ResourceManager()
resources = rm.list_resources()
print("Discovered {} devices".format(len(resources)))
print(f"{resources}")
print("Ignoring non-GPIB devices\n")

# Variables for our search loop:
target_device_id = '3458A'    # Instrument to search for
is_found = False              # Whether or not the instrument is found
target_interface = 'GPIB'     # Interface to search for
inst_id = None                # Instrument (if found)



# Loop through the list of GPIB devices
for name in resources:
    if target_interface in name:
        print(f"Opening device: {name} ...")
        try:
            inst = rm.open_resource(name)       # Create instrument variable 'inst'
            inst.write('END ALWAYS')            # Tell 3458A to respond properly
            inst_id = inst.query("ID?").strip() # Send command to request instrument ID string

            # Query details of connected instrument to find a match
            if target_device_id in inst_id:
                is_found = True
                break  # Break out of loop (stop searching) if found

        except:
            print("Instrument not connected!\n")

print(f"{inst_id}") # The search loop is complete. Did we find it?
if not is_found:
    print(f"Error: Device {target_device_id} not found")
#    inst.close()
    rm.close()
    input("Press ENTER to exit.")
    sys.exit(1)  # Exit app with an error code

inst.timeout = 20000          # Global timeout for GPIB interface comms

print(f"Device {target_device_id} found")

inst_rev = inst.query("REV?").strip()
print (f"Firmware revision: {inst_rev}")
inst_temp = inst.query("TEMP?").strip()
print (f"Internal Temperature: {inst_temp} Deg.C\n")

print("Select Calibration Item to read out:")
print("0: Initial (nominal) values")
print("1: Actual Values")
print("3: Upper Limit")
print("5: Lower Limit")
cal_item = input("")

while cal_item not in {"0", "1", "3", "5"}:
    cal_item=input("Please choose 0, 1, 3, or 5")

print("\nstart\n")

for const_id in range(1,254):
    cal_out = inst.query(f"CAL? {const_id},{cal_item}").strip()
    print (f"{cal_out}")
    continue

print("\nend")

inst.close() # close instrument
rm.close() #close resource manager session
sys.exit(0)
