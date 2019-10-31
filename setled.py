
import Sqlquery
import modbus_tk.modbus_tcp as mt
import modbus_tk.defines as md
master = mt.TcpMaster("192.168.1.10", 502)
master.set_timeout(5.0)
query=Sqlquery()
allnum = query.select_all('1')
freenum = query.select_free('1')
Hold_value = master.execute(slave=1, function_code=md.READ_HOLDING_REGISTERS, starting_address=1, quantity_of_x=3, output_value=5)
Hold_value = master.execute(slave=1, function_code=md.READ_HOLDING_REGISTERS, starting_address=1, quantity_of_x=3, output_value=5)
Coils_value = master.execute(slave=1, function_code=md.READ_COILS, starting_address=1,  quantity_of_x=3, output_value=5)