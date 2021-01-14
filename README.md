# discord-audio-pipe
Simple program to send stereo audio (microphone, stereo mix, virtual audio cable, etc) into a discord bot.

Removed the GUI to make it work on a Raspberry PI.

- If you are using the source code, install the dependencies and start the program using ``main.py``

## Setting up a Bot account
1. Follow the steps [**here**](https://discordpy.readthedocs.io/en/latest/discord.html) to setup and invite a discord bot
2. To link the program to your bot, create a file ``token.txt`` in the same directory as ``main.py`` and save the bot token inside

## Dependencies
Requires Python 3.5+. Install dependencies by running ``pip3 install -r requirements.txt``

In some cases PortAudio and xcb libraries may be missing on linux. On Ubuntu they can be installed with
```
    $ sudo apt-get install libportaudio2
    $ sudo apt-get install libxcb-xinerama0
```

## CLI
discord-audio-pipe can be run from the command line and contains some tools to query system audio devices and accessible channels.
```
usage: main.py [-h] [-t TOKEN] [-v] [-c CHANNEL] [-d DEVICE] [-D] [-C]

Discord Audio Pipe

optional arguments:
  -h, --help            show this help message and exit
  -t TOKEN, --token TOKEN
                        The token for the bot
  -v, --verbose         Enable verbose logging

Command Line Mode:
  -c CHANNEL, --channel CHANNEL
                        The channel to connect to as an id
  -d DEVICE, --device DEVICE
                        The device to listen from as an index

Queries:
  -D, --devices         Query compatible audio devices
  -C, --channels        Query servers and channels (requires token)
```
