from mido import Message
import mido
import time

msg = Message('note_on', note = 60)
print(msg)
msg_2 = Message('note_off', note = 60)
print(msg_2)

outport = mido.open_output('Logic Pro Virtual In')
outport.send(msg)
time.sleep(0.5)
outport.send(msg_2)

print(mido.get_output_names())