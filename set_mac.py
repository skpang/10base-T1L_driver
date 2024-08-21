from smbus import SMBus
import time
import os

mac = bytearray()
i2cbus = SMBus(1)  # Create a new I2C bus
i2caddress = 0x50  # Address of MAC address device
i2cbus.write_byte(i2caddress,0xfa)

 

     
def get_mac():
	mac_str = ' '
	i2cbus = SMBus(1)  # Create a new I2C bus
	i2caddress = 0x50  # Address of device
	i2cbus.write_byte(i2caddress,0xfa)
	a = 0
	a = i2cbus.read_byte(i2caddress)
	mac_str = mac_str + f'{a:x}' + ':'
	
	a = i2cbus.read_byte(i2caddress)
	mac_str = mac_str + f'{a:x}' + ':'

	a = i2cbus.read_byte(i2caddress)
	mac_str = mac_str + f'{a:x}' + ':'

	a = i2cbus.read_byte(i2caddress)
	mac_str = mac_str + f'{a:x}' + ':'

	a = i2cbus.read_byte(i2caddress)
	mac_str = mac_str + f'{a:x}' + ':'
	
	a = i2cbus.read_byte(i2caddress)
	mac_str = mac_str + f'{a:x}' 					
	
	print("MAC address read from 24AA02E48 chip :" + mac_str)
	cmd_str = 'sudo ip link set dev eth1 address' + mac_str
	print(cmd_str)
	os.system(cmd_str)


print(' ')
print('##########################################')		
print('\nRaspberry Pi 10Base-T1L Hat skpang.co.uk 07/24')
os.system("sudo ip link set eth1 down")
get_mac()
os.system('sudo ip link set eth1 up')
print("MAC address set\n")
