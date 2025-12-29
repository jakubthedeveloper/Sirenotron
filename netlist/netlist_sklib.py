from collections import defaultdict
from skidl import Pin, Part, Alias, SchLib, SKIDL, TEMPLATE

from skidl.pin import pin_types

SKIDL_lib_version = '0.0.1'

netlist = SchLib(tool=SKIDL).add_parts(*[
        Part(**{ 'name':'LM358', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'LM358'}), 'ref_prefix':'U', 'fplist':['', ''], 'footprint':'Package_DIP:DIP-8_W7.62mm', 'keywords':'dual opamp', 'description':'Low-Power, Dual Operational Amplifiers, DIP-8/SOIC-8/TO-99-8', 'datasheet':'http://www.ti.com/lit/ds/symlink/lm2904-n.pdf', 'pins':[
            Pin(num='3',name='+',func=pin_types.INPUT,unit=1),
            Pin(num='2',name='-',func=pin_types.INPUT,unit=1),
            Pin(num='1',name='~',func=pin_types.OUTPUT,unit=1),
            Pin(num='5',name='+',func=pin_types.INPUT,unit=2),
            Pin(num='6',name='-',func=pin_types.INPUT,unit=2),
            Pin(num='7',name='~',func=pin_types.OUTPUT,unit=2),
            Pin(num='8',name='V+',func=pin_types.PWRIN,unit=3),
            Pin(num='4',name='V-',func=pin_types.PWRIN,unit=3)], 'unit_defs':[{'label': 'uA', 'num': 1, 'pin_nums': ['3', '1', '2']},{'label': 'uB', 'num': 2, 'pin_nums': ['5', '6', '7']},{'label': 'uC', 'num': 3, 'pin_nums': ['4', '8']}] }),
        Part(**{ 'name':'NE555P', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'NE555P'}), 'ref_prefix':'U', 'fplist':['Package_DIP:DIP-8_W7.62mm'], 'footprint':'Package_DIP:DIP-8_W7.62mm', 'keywords':'single timer 555', 'description':'Precision Timers, 555 compatible,  PDIP-8', 'datasheet':'http://www.ti.com/lit/ds/symlink/ne555.pdf', 'pins':[
            Pin(num='8',name='VCC',func=pin_types.PWRIN),
            Pin(num='1',name='GND',func=pin_types.PWRIN),
            Pin(num='2',name='TR',func=pin_types.INPUT,unit=1),
            Pin(num='5',name='CV',func=pin_types.INPUT,unit=1),
            Pin(num='4',name='R',func=pin_types.INPUT,unit=1),
            Pin(num='3',name='Q',func=pin_types.OUTPUT,unit=1),
            Pin(num='7',name='DIS',func=pin_types.INPUT,unit=1),
            Pin(num='6',name='THR',func=pin_types.INPUT,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'R', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'R'}), 'ref_prefix':'R', 'fplist':[''], 'footprint':'Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal', 'keywords':'R res resistor', 'description':'Resistor', 'datasheet':'~', 'pins':[
            Pin(num='1',name='~',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='~',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'C', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'C'}), 'ref_prefix':'C', 'fplist':[''], 'footprint':'Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm', 'keywords':'cap capacitor', 'description':'Unpolarized capacitor', 'datasheet':'~', 'pins':[
            Pin(num='1',name='~',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='~',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'Conn_01x03', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'Conn_01x03'}), 'ref_prefix':'J', 'fplist':[''], 'footprint':'Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical', 'keywords':'connector', 'description':'Generic connector, single row, 01x03, script generated (kicad-library-utils/schlib/autogen/connector/)', 'datasheet':'~', 'pins':[
            Pin(num='1',name='Pin_1',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='Pin_2',func=pin_types.PASSIVE,unit=1),
            Pin(num='3',name='Pin_3',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] }),
        Part(**{ 'name':'Conn_01x02', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'Conn_01x02'}), 'ref_prefix':'J', 'fplist':[''], 'footprint':'Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical', 'keywords':'connector', 'description':'Generic connector, single row, 01x02, script generated (kicad-library-utils/schlib/autogen/connector/)', 'datasheet':'~', 'pins':[
            Pin(num='1',name='Pin_1',func=pin_types.PASSIVE,unit=1),
            Pin(num='2',name='Pin_2',func=pin_types.PASSIVE,unit=1)], 'unit_defs':[] })])