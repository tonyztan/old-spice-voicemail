# Old Spice Voicemail Generator
A Python-based Old Spice Voicemail Generator.

Final Project for the Information and Computer Security course at the University of Southern California Summer Program.

Information about the assignment can be found at:
https://tonyztan.github.io/static/old-spice-voicemail/itp125 - python programming project.docx

## About

This program can operate in two modes: interactive and passive. The mode is automatically selected based on whether arguments are passed on to the program when it is run.

### Interactive mode
For most users, it is recommended to use the interactive mode by simplying running "oldspice-voicemail.py". In this mode, the user is guided through all the possible options for the voicemail via a series of questions. The user is prompted to enter a phone number, select a gender, and choose the reasons and endings to be included in the voicemail.

After the user confirms the settings and enters a desired name for the output file, the program downloads the necessary spliced mp3 files from GitHub using a secure HTTPS connection and parses them. It will output the final voicemail message in the mp3 format, along with "mp3list.txt", which lists all of the files used to produce the message.

### Passive mode
For advanced users, it is also possible to pass arguments directly to the program through the command-line.

The syntax is:

oldspice-voicemail.py --gender <m/f> --phone <10-digit number without separators> --reasons <reason letters> --endings <ending letters> --out <output filename>

An example would be:

oldspice-voicemail.py --gender m --phone 8881234567 --reasons acd --endings abde --out JohnDoe

The reasons and endings that can be selected are:

Male reasons:
[a] Building an orphanage for children with their bare hands while playing a sweet,
    sweet lullaby for those children with two mallets against their abs xylophone. 
[b] Cracking walnuts with their man mind. 
[c] Polishing their monocle smile. 
[d] Ripping out mass loads of weights.

Male endings:
[a] I'm on a horse. 
[b] Do do do doot doo do do dooot. 
[c] I'm on a phone. 
[d] SWAN DIVE. 
[e] This voicemail is now diamonds.

Female reasons:
[a] Ingesting my delicious Old Spice man smell. 
[b] Listening to me read romantic poetry while I make a bouquet of paper flowers
    from each read page. 
[c] Enjoying a lobster dinner I prepared just for her while carrying her on my back
    safely through piranha infested waters. 
[d] Being serenaded on the moon with the view of the earth while surviving off
    the oxygen in my lungs via a passionate kiss. 
[e] Riding a horse backwards with me.

Female endings:
[a] But she'll get back to you as soon as she can. 
[b] Thanks for calling.

When the correct arguments are passed on to the program, the program will list the settings selected and download the necessary spliced mp3 files from GitHub using a secure HTTPS connection. It will parse them and output the final voicemail message in the mp3 format, along with "mp3list.txt", which lists all of the files used to produce the message.

## Audio
All audio used is originally from the following videos by Old Spice:

Male version: https://www.youtube.com/watch?v=-8JsvwUcok0

Female version: https://www.youtube.com/watch?v=Kx-78v6WLN8

The spliced files were provided by the instructor, available at http://www-bcf.usc.edu/~chiso/itp125/project_version_1/.

## License
The MIT License (MIT)

Copyright (c) 2015 Tony Zhaocheng Tan <tony@tonytan.io>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.