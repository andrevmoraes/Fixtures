"""Análise musical para shows DMX — LISA / SaWaDiKa."""
import json
from pathlib import Path
import librosa
import numpy as np
from scipy.ndimage import median_filter

AUDIO=Path("youtube-audio.mp3")
OUTPUT=Path("analysis_sawadika.json")

def norm(x):
    lo=np.percentile(x,5); hi=np.percentile(x,95)
    return np.clip((x-lo)/(hi-lo+1e-9),0,1)

def section(t):
    if t<28:return "intro_build"
    if t<69:return "groove_a"
    if t<83:return "break"
    if t<110:return "groove_b"
    if t<138:return "groove_c"
    if t<151:return "bridge"
    if t<168:return "final_build"
    return "finale"

y,sr=librosa.load(AUDIO,sr=None,mono=True)
tempo,frames=librosa.beat.beat_track(y=y,sr=sr,units="frames",trim=False)
tempo=float(np.atleast_1d(tempo)[0]); beats=librosa.frames_to_time(frames,sr=sr)
hop=512
rms=librosa.feature.rms(y=y,hop_length=hop)[0]
onset=librosa.onset.onset_strength(y=y,sr=sr,hop_length=hop)
rt=librosa.frames_to_time(np.arange(len(rms)),sr=sr,hop_length=hop)
ot=librosa.frames_to_time(np.arange(len(onset)),sr=sr,hop_length=hop)
energy=norm(np.interp(beats,rt,rms)); trans=norm(np.interp(beats,ot,onset))
baseline=median_filter(energy,size=9,mode="nearest")
contrast=.55*trans+.45*np.maximum(0,energy-baseline)
threshold=np.percentile(contrast,88)
acc=[]
for i in np.argsort(contrast)[::-1]:
    if contrast[i]<threshold: break
    if all(abs(int(i)-j)>=2 for j in acc): acc.append(int(i))
    if len(acc)>=45: break
acc=set(acc)
out={"song":"LISA - SaWaDiKa","duration":round(len(y)/sr,3),"tempo":round(tempo,3),
     "beat_count":len(beats),"analysis":[
      {"time":round(float(t),3),"energy":round(float(energy[i]),3),
       "onset":round(float(trans[i]),3),"accent":i in acc,"section":section(float(t))}
      for i,t in enumerate(beats)]}
OUTPUT.write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding="utf-8")
print(f"{len(beats)} beats | {tempo:.2f} BPM | {len(acc)} acentos")
