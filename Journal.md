---
title: "Remington 1.1"
author: "Stephen McAllister"
description: "Custom keyboard layout: 60% with arrow keys. BT and battery-powered."
created_at: "2025-07-03"
---

#### 7_3_2025 Design key layout

*1.2h* I want this to be a very small, bluetooth enabled, battery powered keyboard. I like the Drop Alt board design, so I'm aiming for something like that.

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