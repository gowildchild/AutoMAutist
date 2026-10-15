## AutoMAutist
* Digital Auti/ADHD-Coach, Assistant and Caretaker.
* Copyright (c) 2009-2026 Gunther Voet. All Rights Reserved.
* This program is free software: you can redistribute/modify it under the terms
* of the GNU Affero General Public License v3.0 (AGPLv3) as published by the FSF.
* Closed-source integration, corporate deployment, SaaS monetization licensing rules below the text!

# 1991 - Turbo Pascal - Velleman RS-232 relay cards
The idea started as a Turbo Pascal program around 1991 when I was trying to communicate over a DB-9
serial port with a Velleman relay board with 8 relays, but which was upgraded to 16 relays by soldering
the extra relays to it.. That thing was a workhorse and it reacted swift, errorless. The reaction time
had sometimes lags when there were multiple tasks happening on MS-DOR, but that was my first true love
with automating .. just.. things! 

# 1994 - Turbo Pascal - Searching for ways
Well, there was not so much available on the market back then, so I was also busy with other things. One
of the things which I was busy with was with growing a true love with OS/2 Warp beta. I was already an OS/2
user since v2.1, people around that time know how Windows was. If there was an internet issue, it was usually
Winsock. At that time I started to know the power of true multitasking. A few years later there were plugs
which again gave me that boost of using them with my own software. These were 433Mhz plugs with an attitude.
I managed to solve that with a small relay board, making a bridge on the keys and controlling that through
serial port. That worked great for a few years. OS/2 was great for that back then.

# 1997 - C++ - 433MHz and X10
The relay-board had however one big problem. It was one plate, it needed wires and it needed to be mounted
somewhere separate for it to reach all the plugs. For automating things through a house, it was not really
very useful, unless I would create multiple boards, but they had much smaller devices available on the 
market with 433Mhz and X10 remote control. At that moment I was also very busy learning Linux Slackware. 

# 2000 - Bash - X10
The journey went very strange, I was having problems with getting those things work reliable in C++ had
polling problems and and literally went from issue to issue. In that time there wasn't so much available 
on the internet as now. I was busy falling in love with Linux, which ended up to be used for my job with
a company I've created back then, which I was doing all the ICT work, programming, server administration,
design, solving Courier IMAP compilation errors (was that a pain in the *) and much more. At that moment
Linux Bible was for me the only book that mattered. I ended up creating Bash scripts which were controlling
the X10 remote plugs. It was probably one of the smallest programs because it was a little shell script.

# 2013 - Diagnose of autism
You can read everything about that on my blog, for me it was an eyeopener. I knew already since 2002. My
mom was already giving me quite some advice how to get even with the chaos, but, I knew back then that it
wasn't only the ADHD which was fighting so hard in me, I just didn't know it was autism till I got my
diagnosis in 2013. I got more info about that at my blog about autism: AutiBoi(https://autiboi.be/2013/03/27/finally-the-diagnose-begins/)

# 2014 - Perl - Maginon/Edimax plugs
Embedded technologies started to get on the market and oh boy, it changed the world entirely! You could 
literally jump behind your computer, start creating code and put it on devices which were for many years
mostly limited to remote power plugs and remote lightning. The plugs ran on Busybox but that was enough to
have a hook from the master software towards the slave clients, through a very old REST interface if I am
not mistaken. Those plugs changed my life. I started programming it in Perl and it worked quite good, but
I had the issue that they were not always so reliable of being on the network, so, very often they were
blinking their red light and unable to be switched because they couldn't connect in the concrete house
which I was living at. It was perhaps the least responsive system in my life while being state-of-the-art
hardware with processor and possibilities. Too bad, really, because else I would have been much earlier
with AutoMAutist.

# 2016 - Perl - AutoMAutist v5 was born
I had 8 plugs in the house and it was a gamechanger. I wanted to use the plugs to alert me for certain
thinks by using the light. I already had a blink-script ready which could blink 1x, 2x and 3x extra fast.
With that I could warn that I had to be on time somewhere. Also showering was suddenly a lot easier, the
first "Shower Timer" was created at that time. It had no display, but it had a voice and it had a switch
between the boiler to turn off the warm water. It also helped me to warn when things had to happen, because
if there is something which I am having issues with, with AuDHD it is procrastination. 

At that moment I've automated a lot in my life with automations with my paperwork and other issues I was
having on a daily basis. It certainly gave me the cheapest electricity bill, that I've ever had, which
gave me another incentive! I also had a camera that warned me when I had to do the dishes, with an algorithm
that took screenshots and checked for how much white there was in the sink.

# 2018 - Perl - Milight lightbulbs and LED-strips
This even changed more, because now the signals were not limited to the lightbulbs that were being switched
on and off in a repetitive rate, but there were RGB colors! I have chosen blue for medical things, like an
appointment with a doctor of having to take medicine, green for giving the plants water because they really
had a tough life with me and red for any other meetings. It also helped me waking up easier, it gave me a
shower timer that was more interactive. It gave a lot of help in doing things easier, stress-free and to
keep everything maintained without ripping my pants on it. 

# 2020 - Home Assistant - Tuya lightbulbs and so..
I had enough of Perl, really and went into the trenches of Python. Where Perl offers you to define the
sharpness of the blade to kill the tiger, Python offers simplicity of having it that way. Python restricts
stylistic choices, which makes a programmer from Japan have the same style of as a programmer of Ghent. But,
sometimes it is good to have that in a programming language. It also brought me in touch with Home Assistant,
which meant I could run my Perl and Python REST daemons on a server and let the domotica connect to it to use
its parameters for where it matters. That, changed my life entirely. It grew out to a Shower Timer, 
a Bedroom Timer, a Kitchen Prince, it controls the humidity in the house against mold, it tells when the windows
have to be opened, the plants tell when they need water, I get a notification when I turn on the stove, go to
another room and forget about it. It turns everything off and alerts at critical situations. It warns me there
is food waiting in the microwave, it even did the electronic lock through another (are 5 REST servers too much?)
daemon, which was doing the communication and encryption between a keypad and a card reader, based on the SesamID
protocol. 

It is not only saving money, because power outlets get turned off when devices are not in use and/or stand-by
state, but it is also a comfort to have an assistant looking behind the light switches. The advice of pulling out
stand-by equipment is already for longer time not really valid anymore, because most machines needed power to
keep their clock running, but, anything that doesn't get used, gets disconnected from the power. The REST servers
were written the same way that I started to know bitmasks in Turbo Pascal, but with Python it is so much more fun!

It now grew out towards not only switches, lightbulbs, but also sensors, heating sensors, energy-on-demand, with
HMI displays showing the status around the house. I've done so much experience with ESP-32 processors, that I started
creating my own little things, which is connected to the REST servers and ESPHome, with Home Assistant. What will be
released here on this repo will 3 REST servers which I try to put in 1, now that I am porting it to the public world.
Since I made an EMS (Energy Manager Software) in the REST server based on bitshifting, it had no issues running on 
very low system specifications. We saved about 40-70% on our electricity bill back then. Now, I got to reinstall
Home Assistant soon, because I want to clean house, I will be sharing the bundles, automations, scripts and 
algorithms here too, but the build will be more or less oriented towards an assistive device which tries to make my
life easier for as far as I can.

Now, you got the story behind everything here, I hope it will help more neurodivergent people with getting structure
through computer automation. If you got questions, feel free to ask or open an issue and I will respond.

Enjoy, Gunther!

## AutoMAutist
* Digital Auti/ADHD-Coach, Assistant and Caretaker.
* Copyright (c) 2009-2026 Gunther Voet. All Rights Reserved.
* This program is free software: you can redistribute/modify it under the terms
* of the GNU Affero General Public License v3.0 (AGPLv3) as published by the FSF.

## ⚖️ Licensing & Commercial Policy

**Community & Caregivers (AGPLv3):** Free to use, self-host, and modify for personal, educational, and non-commercial assistance. Any network/SaaS deployment of *modified* code must publicly share its source under Section 13.

**Commercial & Enterprise:** Closed-source integration, corporate deployment, or SaaS monetization without open-sourcing modifications requires a paid **Commercial License**. 

Inquiries: `github.gowildchild.com@xsrv.net` (or open an issue)
