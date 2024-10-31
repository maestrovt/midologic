# midologic
Test sending MIDI to Logic using mido.
The idea is to sonify the maze solver, using the [Python MIDI Interface mido](https://github.com/mido/mido), to send MIDI messages to Logic Pro X. To function on Mac OS, [the `rtmidi` module is required](https://spotlightkid.github.io/python-rtmidi/installation.html). Running `python3 -m pip install python-rtmidi` worked fine for me.
