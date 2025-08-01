---
title: "Remington 1.1"
author: "Stephen McAllister"
description: "Custom keyboard layout: 60% with arrow keys. BLE and battery-powered."
created_at: "2025-07-03"
---

> 📘 Total Time:  23 hours

#### 7_3_2025 Design key layout

*1.2h* I want this to be a very small, BLE enabled, battery powered keyboard. I like the Drop Alt board design, so I'm aiming for something like that.

Getting full arrow keys (where the up/down keys aren't .5u tall) wreaks havoc with spacing. I got rid of the right shift key. 

Having func keys tertiary to the num row is fine, but I want a completely seperate esc and del key, so dropped those on the right near the arrow keys. In a final version those might just be macros.

![Initial Keyboard Layout](assets/initial_layout.png)

---

#### 7_15_2025 Schematic + PCB V1

*1h* Started this by laying out the switches and diodes on the schematic. I layed them out in a 14 x 5 grid, then deleted switches from the rows with fewer keys: 
![Schematic Version 1](assets/Schematic_V1.png)

*1.5h* Once I figured out how to move the symbols on the right grid (drag them from the center pad), moving these around was pretty easy. Unfortunately I turned off the ratnest, and when I turned it back on realized the numbering was off. KiCad numbered my switches oddly when I copied and pasted on the schematic, so the last three rows of keys are all messed up. Problem for next time. ![PCB Version 1 ](assets/PCB_V1.png)

---

#### 7_19_2025 Schematic + PCB V2

*20m* Rewrote the schematic of the switches with the right numbering. I also realized I needed one more switch in the top row, so added that. Now that I know what I'm doing, it took a lot less time.
![Schematic Version 2](assets/Schematic_V2.png)

*4m* Updated the PCB and every switch moved to the right place! Only 13 and 53 needed to be placed. In this process I realized my original schematic was also missing switch 53, so placed that.

*20m* Change the key sizes  
I went through the schematic and changed the footprint key sizes. That's when I [found out](https://hirosarts.com/blog/keycap-dimensions-guide-for-beginners/?) that a 2.5u Shift and Caps Lock key is very hard to come by for ANSI keyboard keycap sets. I still want this pretty small, but I'll need a place for the Nano anyway, so I'm going to add the Nano to the PCB and see how the spacing works out.

*54m* Research controller boards  
This board needs bluetooth (esp32), enough pins, well-documented, and cheap. I could try a SEEED board but I'd like some arduino experience so I'm doing the Nano Esp32 with a step-up. There's also this image on one of the [docs](https://docs.arduino.cc/tutorials/nano-esp32/cheat-sheet/) showing a possible direct power from battery option. It needs EXACTLY 3.3v, though, and disables the usb-c power, so I guess I'd need a step-down in my schematic. I'll figure this out after - I know the Nano is the board I want.

![Arduino docs screencap](assets/Nano_battery_option.png)

#### 7_20_2025 Schematic + PCB V3

*1.5h* Many of my keys are non-standard sizes, like the enter and caps lock which I made 2.5u. It's cheaper to buy ANSI keycaps, so I rewrote the board based on ANSI sizes. The arrows stick out, but I need a place for the board anyway so it's fine. New layout:
![New ANSI Safe layout](assets/ANSI_layout.png)

*1h* Researched some more, and found out the Nice!Nano V2 is a very popular chip for wireless boards. Read for a while about connecting it to batteries and such.

*3h* Sooo the Nice nano only has 18 GPIO pins and I have 14 columns + 5 rows = 19 pins needed. However, I only need 65 keys: 13*5. So I'm deleting the final row and moving the keys where I need them.
![Schematic Version 3, now 13x5](assets/Schematic_V3.png)

With 13 columns and 5 rows, I use all the pins. It took a while to route the individual keys, and tomorrow I'll finish by connecting lines to the board. Might need to shuffle around things to keep the rat's nest simpler.
![PCB editor screenshot with col and rows routed](assets/PCB_V3.png)

#### 7_23_2025

*20min* Connected ratsnest to the board. It's a bit messy - might be worth shifting around pins and things.

#### 7_23_2025 Finish PCB

*1h* Fixed the ratsnest. Gave the wires correct clearance and tightened up the edges of the PCB. The stabilizer holes on the backspace button are in a really annoying position, but got around them eventually.
![Completed PCB Wiring](Assets/PCB_V4.png)

#### 7_27_2025 Finish CAD

*2h* Fought with the switch model for a while, trying to figure out configurations. The final switch model has a configuration for each size of keycap, which makes it easy to switch them around on the board design. Next time I try this it will go faster
![Switch Configurations](Assets/SwitchCADConfigurations_Screenshot.png)

*1.5h* Making the base and lid was straightforward. Deciding on a height for the base took a bit - I used my completed macropad to estimate how high on the switch the base should be, then extruded it to that plane in F3D. The PCB sits on a little ledge + has 5 mounting holes.
![Case Base w/ PCB](Assets/CaseAndPCB.png)

#### 7_28_2025 Completing

*1h* Realized the support ledge interfered with the Nano pins and a stabilizer, so went back and changed the sketch. Sometimes Fusion's history is very useful. Also added mounting holes: I'm using all M3 heatset mounts everywhere.

Added a ground plane (not connected to anything tho bc this is battery powered)

*1h* Recheck board, generate gerbers, put all my files in the repo

*45m* Create BOM and find all the parts.

*30m* Write Firmware

*45m* Finish Journal + Readme + submit project

#### 7_31_2025

*2h* Switched the case design to something that looks more like the original typewriters. Picked a set of tan keycaps to match.
Most of the work was getting the spline to extrude nicely over the supports. 
![Side Profile](Assets/side_profile.png)

I tilted the board 7 degrees to make typing easier.
![Tilted Board](Assets/tilted.png)