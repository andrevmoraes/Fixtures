import librosa
# Carrega a música
y, sr = librosa.load('youtube-audio.mp3')
# Extrai as batidas
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
beat_times = librosa.frames_to_time(beat_frames, sr=sr)
# Imprime a lista de tempos
print(list(beat_times))