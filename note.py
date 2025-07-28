from mido import Message
import mido
import time

class Note:
    def __init__(self):
        self._pitch = None
        self._duration = None
        self._channel = None
        self._msg_on = None
        self._msg_off = None
        self._pan = None
        self._cc_pan_msg = None


    def play(self, pitch, duration, channel, pan):
        with mido.open_output('Logic Pro Virtual In') as outport:  
            self._pitch = pitch
            self._duration = duration
            self._channel = channel
            self._pan = pan
            self._cc_pan_msg = Message('control_change', channel = self._channel, control = 10, value = self._pan)
            self._msg_on = Message('note_on', note = self._pitch, channel = self._channel)
            self._msg_off = Message('note_off', note = self._pitch, channel = self._channel)
            outport.send(self._cc_pan_msg)
            outport.send(self._msg_on)
            time.sleep(self._duration)
            outport.send(self._msg_off)
            time.sleep(self._duration)
