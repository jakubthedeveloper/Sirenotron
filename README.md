![image](plate.png)

This is documentation for my electronic project, an analog siren synthesizer "Sirenotron".

![image](timelapse/14.jpg)

I built it from scratch, designing it on paper, part by part, module by module, through multiple iterations of design, soldering, part replacement, voltage checks, and audio testing. Finally, the schematic looks like this:

<img src="schematic.jpg" width="500" />

Digitalized version:

<img src="Sirenotron-Schematic-EasyEda.png" width="500" />

And the instrument sounds like this:

[YouTube: SIRENOTRON - my Hand-crafted Analog Siren Synthesizer](https://youtu.be/M3CLcUoV7Gw)

The Sirenotron consists of a single square-wave oscillator based on the 555 timer and an LFO (low-frequency oscillator) based on an LM358. The LFO controls the pitch of the oscillator and has two modes: triangle and square. Additionally, there is a switch that enables Acid mode for the square-wave LFO. Technically, Acid mode is implemented by adding a single capacitor, but musically it gives a nice TB-303-like sound caused by voltage jumps on the edges of the square.

Controls:
- LFO speed
- LFO shape (triangle / off / square)
- Acid mode (off / on)
- Oscillator pitch
- Tone (simple low-pass filter)
- Volume
- "Fire!" button to trigger the sound

LEDs:
- Power on - an LED built into the "Fire!" button
- LFO speed - green LED
- Sound activated by pressing "Fire!" - red LED

Power: 9V DC, center-negative polarity (minus on the tip).


Here are some images from the building process:

<img src="timelapse/1.jpg" width="500" />
<img src="timelapse/2.jpg" width="500" />
<img src="timelapse/3.jpg" width="500" />
<img src="timelapse/4.jpg" width="500" />
<img src="timelapse/5.jpg" width="500" />
<img src="timelapse/6.jpg" width="500" />
<img src="timelapse/7.jpg" width="500" />
<img src="timelapse/8.jpg" width="500" />
<img src="timelapse/9.jpg" width="500" />
<img src="timelapse/10.jpg" width="500" />
<img src="timelapse/11.jpg" width="500" />
<img src="timelapse/12.jpg" width="500" />
<img src="timelapse/13.jpg" width="500" />
<img src="timelapse/14.jpg" width="500" />
<img src="timelapse/15.jpg" width="500" />
<img src="timelapse/16.jpg" width="500" />
