# 3457A-Calibration-Downloader
A script to download the calibration constants from the 3458A multimeter via GPIB

Install Python and PyVISA, then your choice of Keysight IO Libraries Suite (if using a HPAK USP-GPIB adapter) or National Instruments NI-488.2 software if using an NI GPIB-USB-HS, or whatever respective drivers you need for your GPIB adapter.

It will automatically find and communicate with your 3457A to allow you to read out the calibration constants. </br>
Operation is self explanatory. The readout options are as follows: </br>
0: Initial (nominal) values - These are the values for a blank uncalibrated instrument. </br>
1: Actual Values - These are the specific calibration values for your instrument. </br>
3: Upper Limit - The upper allowable limit, if your instrument exceeds these, you have a problem.. </br>
5: Lower Limit - The lower allowable limit, as above. </br>

I have tested it under Windows 10 using an Agilent 83257B USB-GPIB adapter with the Keysight IO Libraries Suite installed, and also a National Instruments GPIB-USB-HS adapter with the NI libraries installed and it works perfectly on both. It should work on any GPIB interfaces that PyVISA supports, let me know how you go with your setup. </br>
(I found the Keysight software 'just works' a bit better with it's auto discovery of connected devices, but once the NI software can see the instrument, it's smooth sailing).
