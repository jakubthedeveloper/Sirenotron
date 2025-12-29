###############################################################################
# Environment
###############################################################################

import os
os.environ['KICAD9_SYMBOL_DIR'] = '/usr/share/kicad/symbols'
from skidl import *

###############################################################################
# Nets
###############################################################################

vcc = Net('VCC')
gnd = Net('GND')

vref = Net('VREF')

lfo_tri = Net('LFO_TRI')
lfo_sqr = Net('LFO_SQR')
lfo_sel = Net('LFO_SEL')

cv_555  = Net('CV_555')
audio   = Net('AUDIO')
out     = Net('OUT')

###############################################################################
# Power
###############################################################################

vcc.drive = POWER
gnd.drive = POWER

###############################################################################
# Footprints + helpers
###############################################################################

R_FP = 'Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P7.62mm_Horizontal'
C_FP = 'Capacitor_THT:C_Disc_D5.0mm_W2.5mm_P5.00mm'

PIN2 = 'Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical'
PIN3 = 'Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical'

def R(val, ref=None):
    r = Part('Device', 'R', value=val, ref=ref)
    r.footprint = R_FP
    return r

def C(val, ref=None):
    c = Part('Device', 'C', value=val, ref=ref)
    c.footprint = C_FP
    return c

###############################################################################
# ICs
###############################################################################

lm358 = Part('Amplifier_Operational', 'LM358', ref='U1')
lm358.footprint = 'Package_DIP:DIP-8_W7.62mm'

ne555 = Part('Timer', 'NE555P', ref='U2')
ne555.footprint = 'Package_DIP:DIP-8_W7.62mm'

op  = lm358.unit['uA']
pwr = lm358.unit['uC']

###############################################################################
# VREF
###############################################################################

r_vref1 = R('100k', 'R1')
r_vref2 = R('100k', 'R2')
c_vref  = C('100n', 'C1')

r_vref1[1] += vcc
r_vref1[2] += vref
r_vref2[1] += vref
r_vref2[2] += gnd

c_vref[1] += vref
c_vref[2] += gnd

###############################################################################
# LM358 LFO
###############################################################################

pwr['V+'] += vcc
pwr['V-'] += gnd

r_bias = R('1M', 'R3')
r_his  = R('220k', 'R4')
c_lfo  = C('22u', 'C2')

r_bias[1] += vref
r_bias[2] += op['-']

c_lfo[1] += op['~']
c_lfo[2] += lfo_tri

# LFO RATE POT (model: 2xR + wiper)
rv1a = R('50k', 'RV1A')
rv1b = R('50k', 'RV1B')
rv1w = Net('RV1_W')

rv1a[1] += lfo_tri
rv1a[2] += rv1w
rv1b[1] += rv1w
rv1b[2] += gnd
rv1w     += op['~']

op['+'] += vref
op['~'] += lfo_sqr

r_his[1] += op['~']
r_his[2] += op['-']

###############################################################################
# LFO MODE – PANEL CONNECTOR (SP3T)
###############################################################################

j_mode = Part('Connector_Generic', 'Conn_01x03', ref='J_MODE')
j_mode.footprint = PIN3

j_mode[1] += lfo_sqr
j_mode[2] += lfo_sel
j_mode[3] += lfo_tri

r_cv = R('470', 'R5')
r_cv[1] += lfo_sel
r_cv[2] += cv_555

###############################################################################
# ACID – PANEL CONNECTOR (SPST)
###############################################################################

j_acid = Part('Connector_Generic', 'Conn_01x02', ref='J_ACID')
j_acid.footprint = PIN2

c_acid = C('100u', 'C3')

j_acid[1] += lfo_sqr
j_acid[2] += c_acid[1]
c_acid[2] += cv_555

###############################################################################
# CV FILTER
###############################################################################

c_cv = C('10n', 'C4')
c_cv[1] += cv_555
c_cv[2] += gnd

###############################################################################
# NE555 AUDIO OSC
###############################################################################

rc_node = Net('RC_NODE')
timing  = Net('TIMING')

ne555[8] += vcc
ne555[1] += gnd
ne555[4] += vcc
ne555[3] += audio
ne555[2] += timing
ne555[6] += timing
ne555[7] += rc_node
ne555[5] += cv_555

r6 = R('1k',   'R6')
r7 = R('2.2k', 'R7')
c5 = C('10n',  'C5')

r6[1] += vcc
r6[2] += rc_node
r7[1] += rc_node
r7[2] += timing
c5[1] += timing
c5[2] += gnd

###############################################################################
# OUTPUT + MASTER POT (PANEL)
###############################################################################

rv3a = R('25k', 'RV3A')
rv3b = R('25k', 'RV3B')
rv3w = Net('RV3_W')

rv3a[1] += audio
rv3a[2] += rv3w
rv3b[1] += rv3w
rv3b[2] += gnd
rv3w     += out

j_master = Part('Connector_Generic', 'Conn_01x03', ref='J_MASTER')
j_master.footprint = PIN3

j_master[1] += audio
j_master[2] += rv3w
j_master[3] += gnd

###############################################################################
# TONE POT (PANEL)
###############################################################################

rv4a = R('50k', 'RV4A')
rv4b = R('50k', 'RV4B')
rv4w = Net('RV4_W')

rv4a[1] += out
rv4a[2] += rv4w
rv4b[1] += rv4w
rv4b[2] += gnd

j_tone = Part('Connector_Generic', 'Conn_01x03', ref='J_TONE')
j_tone.footprint = PIN3

j_tone[1] += out
j_tone[2] += rv4w
j_tone[3] += gnd

###############################################################################
# AUDIO JACK – PANEL CONNECTOR (T, S, G)
###############################################################################

j_audio = Part('Connector_Generic', 'Conn_01x03', ref='J_AUDIO')
j_audio.footprint = PIN3

j_audio[1] += out
j_audio[2] += gnd
j_audio[3] += gnd

###############################################################################
# LEDS – PANEL CONNECTORS
###############################################################################

j_led_pwr = Part('Connector_Generic', 'Conn_01x02', ref='J_LED_PWR')
j_led_pwr.footprint = PIN2

j_led_lfo = Part('Connector_Generic', 'Conn_01x02', ref='J_LED_LFO')
j_led_lfo.footprint = PIN2

r8 = R('2.2k', 'R8')
r8[1] += vcc
r8[2] += j_led_pwr[1]
j_led_pwr[2] += gnd

r9 = R('220', 'R9')
r9[1] += lfo_sqr
r9[2] += j_led_lfo[1]
j_led_lfo[2] += gnd

###############################################################################
# FINAL
###############################################################################

ERC()
generate_netlist()

