#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import sys
import os
import wave
import json

if not os.path.exists("model"):
    print ("Please download the model from https://github.com/alphacep/vosk-api/blob/master/doc/models.md and unpack as 'model' in the current folder.")
    exit (1)

wf = wave.open(sys.argv[1], "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print ("Audio file must be WAV format mono PCM.")
    exit (1)

model = Model("model")
# You can also specify the possible word list
# rec = KaldiRecognizer(model, wf.getframerate(), "zero oh one two three four five six seven eight nine [unk]")
rec = KaldiRecognizer(model, wf.getframerate(), '["oh one two three four five six seven eight nine zero", "[unk]"]')

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        break
        print(rec.Result())
        resultRaw = str(rec.Result())
        result = json.loads(rec.Result())
    else:
        print(rec.PartialResult())
print('FINAL RESULT')

finalResult = str(rec.FinalResult())
print(finalResult)
jsonDict = json.loads(finalResult)
textFound = jsonDict['text']
print('text found: ',textFound)
try:
    f = open('zip_codes.txt', 'x')
except FileExistsError:
    f = open('zip_codes.txt', 'a')
f.write(textFound + '\n')
