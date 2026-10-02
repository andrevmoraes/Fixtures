"""
Gera o XML do Show Principal para o projeto.qxw
com base nas batidas reais detectadas pelo librosa.
"""

beats = [
    0.325, 0.697, 1.138, 1.579, 2.020, 2.438, 2.879, 3.274, 3.715, 4.133,
    4.574, 4.992, 5.433, 5.851, 6.293, 6.711, 7.129, 7.570, 7.988, 8.429,
    8.847, 9.265, 9.706, 10.124, 10.565, 11.006, 11.424, 11.842, 12.283,
    12.701, 13.142, 13.560, 13.978, 14.420, 14.861, 15.279, 15.697, 16.138,
    16.579, 16.997, 17.415, 17.856, 18.297, 18.715, 19.133, 19.574, 19.992,
    20.410, 20.852, 21.293, 21.711, 22.129, 22.570, 22.988, 23.429, 23.847,
    24.288, 24.706, 25.147, 25.565, 25.983, 26.424, 26.865, 27.283, 27.701,
    28.119, 28.537, 28.979, 29.396, 29.838, 30.256, 30.697, 31.138, 31.556,
    31.997, 32.415, 32.856, 33.274, 33.715, 34.133, 34.551, 34.992, 35.410,
    35.852, 36.270, 36.711, 37.129, 37.547, 37.988, 38.406, 38.824, 39.265,
    39.706, 40.147, 40.565, 40.983, 41.424, 41.842, 42.284, 42.701, 43.119,
    43.561, 43.979, 44.420, 44.861, 45.279, 45.697, 46.138, 46.556, 46.974,
    47.415, 47.833, 48.274, 48.715, 49.133, 49.551, 49.993, 50.411, 50.852,
    51.270, 51.711, 52.129, 52.570, 52.988, 53.406, 53.847, 54.265, 54.706,
    55.147, 55.565, 56.007, 56.424, 56.842, 57.284, 57.702, 58.096, 58.561,
    59.002, 59.420, 59.838, 60.279, 60.697, 61.115, 61.556, 61.997, 62.415,
    62.856, 63.274, 63.716, 64.134, 64.575, 64.993, 65.434, 65.852, 66.270,
    66.711, 67.129, 67.570, 67.988, 68.406, 68.847, 69.265, 69.706, 70.124,
    70.565, 70.983, 71.424, 71.842, 72.284, 72.702, 73.143, 73.561, 74.002,
    74.420, 74.861, 75.279, 75.697, 76.138, 76.579, 76.997, 77.415, 77.857,
    78.274, 78.692, 79.134, 79.575, 79.993, 80.411, 80.852, 81.270, 81.711,
    82.129, 82.570, 82.988, 83.429, 83.847, 84.265, 84.706, 85.124, 85.566,
    85.983, 86.425, 86.866, 87.284, 87.702, 88.143, 88.561, 88.979, 89.420,
    89.838, 90.279, 90.697, 91.138, 91.556, 91.997, 92.415, 92.857, 93.275,
    93.716, 94.134, 94.552, 94.993, 95.411, 95.852, 96.270, 96.711, 97.152,
    97.570, 97.988, 98.429, 98.847, 99.265, 99.706, 100.148, 100.566, 100.984,
    101.425, 101.866, 102.284, 102.702, 103.143, 103.561, 104.002, 104.420,
    104.838, 105.279, 105.697, 106.115, 106.556, 106.998, 107.416, 107.857,
    108.275, 108.669, 109.134, 109.552, 109.993, 110.411, 110.852, 111.270,
    111.711, 112.129, 112.570, 112.988, 113.406, 113.847, 114.265, 114.683,
    115.125, 115.566, 115.984, 116.402, 116.843, 117.261, 117.702, 118.120,
    118.561, 119.002, 119.420, 119.838, 120.279, 120.697, 121.115, 121.556,
    121.974, 122.416, 122.857, 123.275, 123.716, 124.134, 124.575, 124.993,
    125.434, 125.852, 126.270, 126.688, 127.129, 127.570, 127.988, 128.430,
    128.848, 129.289, 129.707, 130.125, 130.566, 130.984, 131.425, 131.843,
    132.284, 132.702, 133.120, 133.561, 133.979, 134.420, 134.861, 135.279,
    135.697, 136.139, 136.557, 136.998, 137.416, 137.857, 138.275, 138.693,
    139.134, 139.552, 139.993, 140.411, 140.852, 141.293, 141.711, 142.129,
    142.571, 143.012, 143.430, 143.848, 144.266, 144.707, 145.148, 145.566,
    145.984, 146.425, 146.843, 147.284, 147.702, 148.143, 148.561, 149.002,
    149.420, 149.838, 150.280, 150.698, 151.139, 151.557, 151.998, 152.416,
    152.834, 153.275, 153.716, 154.134, 154.552, 154.993, 155.434, 155.852,
    156.270, 156.711, 157.129, 157.547, 157.989, 158.430, 158.848, 159.266,
    159.707, 160.148, 160.566, 160.984, 161.425, 161.843, 162.284, 162.702,
    163.120, 163.561, 164.003, 164.420, 164.838, 165.280, 165.721, 166.139,
    166.557, 166.998, 167.439, 167.857, 168.252, 168.670, 169.041, 169.413,
    169.784, 170.202, 170.643, 171.061, 171.503, 171.921, 172.362, 172.780,
    173.198, 173.639, 174.057, 174.498, 174.916, 175.357, 175.775, 176.216,
    176.634, 177.052, 177.493, 177.935, 178.352, 178.770, 179.212,
]

def ms(sec):
    return int(round(sec * 1000))

def beat_duration(beats, i):
    if i + 1 < len(beats):
        return max(50, ms(beats[i+1]) - ms(beats[i]))
    return 428

# ─── Cenas disponíveis ───────────────────────────────────────────────────────
# ID6  = Fade In Vermelho (FadeIn 4000)
# ID7  = Vermelho Forte   (FadeIn 100, FadeOut 100)
# ID8  = Chase A: fix1 vermelho, fix2 off
# ID9  = Chase B: fix1 off, fix2 azul
# ID10 = Azul Frio        (FadeIn 800)
# ID11 = Ciano            (FadeIn 800)
# ID12 = Gradiente Auto
# ID13 = Pulso Roxo
# ID14 = Strobe Branco fix1
# ID15 = Strobe Branco fix2
# ID16 = Climax Total (branco)
# ID17 = Fade Out
# ID18 = Apagado
# ID19 = Verde

# Novas cenas que vamos adicionar:
# ID21 = Laranja quente suave (calmaria quente)
# ID22 = Amarelo quente suave
# ID23 = Flash Vermelho instantâneo (dimmer 255, R 255, FadeIn 0 FadeOut 0)
# ID24 = Flash Branco instantâneo
# ID25 = Magenta beat
# ID26 = Verde beat
# ID27 = Roxo beat
# ID28 = Laranja beat
# ID29 = Strobe vermelho rápido (CH6 efeito strobe, CH7 velocidade alta)
# ID30 = Climax Auge - strobe total branco
# ID31 = Climax Auge - vermelho total
# ID32 = Climax Auge - azul total

# ─── Definição das seções ────────────────────────────────────────────────────
# 0s   - 4s    : Fade in vermelho (intro)
# 4s   - 14s   : Beat vermelho forte (batidas reais)
# 14s  - 18s   : Calmaria quente (laranja/amarelo suave)
# 18s  - 28s   : Beat colorido alternado (verde/magenta/roxo)
# 28s  - 44s   : Chase alternado fix1/fix2 (vermelho/azul)
# 43.979s      : Flash vermelho (batida 1 de 2)
# 44.420s      : Flash vermelho (batida 2 de 2) — as duas batidas fortes
# 44.861s - 58s: Beat colorido (magenta/ciano alternado)
# 58s  - 71s   : Calmaria (azul frio suave)
# 71.424s      : Flash branco (batida 1 de 2)
# 71.842s      : Flash branco (batida 2 de 2)
# 72s  - 168s  : Show livre (roxo/verde/ciano/gradiente)
# 168s - 179s  : AUGE — strobe/climax total

# ─── Helpers ─────────────────────────────────────────────────────────────────
def sf(func_id, start_sec, end_sec, color):
    start = ms(start_sec)
    dur = max(50, ms(end_sec) - ms(start_sec))
    return f'    <ShowFunction ID="{func_id}" StartTime="{start}" Duration="{dur}" Color="{color}"/>'

def sf_ms(func_id, start_ms_val, dur_ms_val, color):
    return f'    <ShowFunction ID="{func_id}" StartTime="{start_ms_val}" Duration="{dur_ms_val}" Color="{color}"/>'

# ─── Gera tracks ─────────────────────────────────────────────────────────────
lines = []

# ── Track 0: Audio ────────────────────────────────────────────────────────────
lines.append('   <Track ID="0" Name="Audio" isMute="0">')
lines.append('    <ShowFunction ID="4" StartTime="0" Duration="188569" Color="#608053"/>')
lines.append('   </Track>')

# ── Track 1: Intro fade in (0 - 4s) ──────────────────────────────────────────
lines.append('   <Track ID="1" Name="Intro" isMute="0">')
lines.append(sf(6, 0, 4.0, "#CC3300"))
lines.append('   </Track>')

# ── Track 2: Beat vermelho 4s - 14s (batidas reais) ──────────────────────────
lines.append('   <Track ID="2" Name="Beat Vermelho 4-14s" isMute="0">')
beat_section = [(b, i) for i, b in enumerate(beats) if 4.0 <= b < 14.0]
for idx, (b, i) in enumerate(beat_section):
    func = 7 if idx % 2 == 0 else 18
    color = "#FF0000" if func == 7 else "#222222"
    dur = beat_duration(beats, i)
    lines.append(sf_ms(func, ms(b), dur, color))
lines.append('   </Track>')

# ── Track 3: Calmaria quente 14s - 18s ───────────────────────────────────────
lines.append('   <Track ID="3" Name="Calmaria Quente 14-18s" isMute="0">')
# Laranja suave por 2s, depois amarelo suave por 2s
lines.append(sf(21, 14.0, 16.0, "#FF6600"))
lines.append(sf(22, 16.0, 18.0, "#FFAA00"))
lines.append('   </Track>')

# ── Track 4: Beat colorido 18s - 28s ─────────────────────────────────────────
lines.append('   <Track ID="4" Name="Beat Colorido 18-28s" isMute="0">')
colors_cycle = [
    (25, "#FF00AA"),  # Magenta
    (26, "#00FF44"),  # Verde
    (27, "#8800FF"),  # Roxo
    (28, "#FF6600"),  # Laranja
]
beat_section = [(b, i) for i, b in enumerate(beats) if 18.0 <= b < 28.0]
for idx, (b, i) in enumerate(beat_section):
    func_id, color = colors_cycle[idx % len(colors_cycle)]
    dur = beat_duration(beats, i)
    lines.append(sf_ms(func_id, ms(b), dur, color))
lines.append('   </Track>')

# ── Track 5: Chase alternado 28s - 43.979s ───────────────────────────────────
lines.append('   <Track ID="5" Name="Chase 28-44s" isMute="0">')
beat_section = [(b, i) for i, b in enumerate(beats) if 28.0 <= b < 43.979]
for idx, (b, i) in enumerate(beat_section):
    func = 8 if idx % 2 == 0 else 9
    color = "#FF4400" if func == 8 else "#0044FF"
    dur = beat_duration(beats, i)
    lines.append(sf_ms(func, ms(b), dur, color))
lines.append('   </Track>')

# ── Track 6: Flash vermelho nas 2 batidas fortes ~44s ────────────────────────
lines.append('   <Track ID="6" Name="Flash Vermelho 44s" isMute="0">')
# Batidas: 43.979s e 44.420s
# Flash = 80ms aceso, resto apagado até próxima batida
flash_beats = [43.979, 44.420]
for i, b in enumerate(flash_beats):
    lines.append(sf_ms(23, ms(b), 80, "#FF0000"))          # flash vermelho 80ms
    next_b = flash_beats[i+1] if i+1 < len(flash_beats) else b + 0.441
    gap = ms(next_b) - ms(b) - 80
    if gap > 0:
        lines.append(sf_ms(18, ms(b) + 80, gap, "#111111"))  # apagado entre flashes
lines.append('   </Track>')

# ── Track 7: Beat magenta/ciano 44.861s - 58s ────────────────────────────────
lines.append('   <Track ID="7" Name="Beat Magenta-Ciano 45-58s" isMute="0">')
beat_section = [(b, i) for i, b in enumerate(beats) if 44.861 <= b < 58.0]
for idx, (b, i) in enumerate(beat_section):
    func = 25 if idx % 2 == 0 else 11
    color = "#FF00AA" if func == 25 else "#00CCCC"
    dur = beat_duration(beats, i)
    lines.append(sf_ms(func, ms(b), dur, color))
lines.append('   </Track>')

# ── Track 8: Calmaria azul 58s - 71.424s ─────────────────────────────────────
lines.append('   <Track ID="8" Name="Calmaria Azul 58-71s" isMute="0">')
lines.append(sf(10, 58.0, 64.0, "#0000CC"))
lines.append(sf(11, 64.0, 71.424, "#00CCCC"))
lines.append('   </Track>')

# ── Track 9: Flash branco nas 2 batidas ~71.4s ───────────────────────────────
lines.append('   <Track ID="9" Name="Flash Branco 71s" isMute="0">')
flash_beats_w = [71.424, 71.842]
for i, b in enumerate(flash_beats_w):
    lines.append(sf_ms(24, ms(b), 80, "#FFFFFF"))
    next_b = flash_beats_w[i+1] if i+1 < len(flash_beats_w) else b + 0.418
    gap = ms(next_b) - ms(b) - 80
    if gap > 0:
        lines.append(sf_ms(18, ms(b) + 80, gap, "#111111"))
lines.append('   </Track>')

# ── Track 10: Show livre 72s - 168s ──────────────────────────────────────────
# Divide em blocos de 8 beats, alternando paletas
lines.append('   <Track ID="10" Name="Show Livre 72-168s" isMute="0">')
beat_section = [(b, i) for i, b in enumerate(beats) if 72.0 <= b < 168.0]

palettes = [
    # (func_par, func_impar, cor_par, cor_impar)
    (27, 11,  "#8800FF", "#00CCCC"),   # roxo / ciano
    (26, 10,  "#00FF44", "#0000CC"),   # verde / azul
    (25, 19,  "#FF00AA", "#00CC44"),   # magenta / verde
    (28, 27,  "#FF6600", "#8800FF"),   # laranja / roxo
    (7,  10,  "#FF0000", "#0000CC"),   # vermelho / azul
    (11, 25,  "#00CCCC", "#FF00AA"),   # ciano / magenta
]
block_size = 8
for idx, (b, i) in enumerate(beat_section):
    block = (idx // block_size) % len(palettes)
    fp, fi, cp, ci = palettes[block]
    func = fp if idx % 2 == 0 else fi
    color = cp if idx % 2 == 0 else ci
    dur = beat_duration(beats, i)
    lines.append(sf_ms(func, ms(b), dur, color))
lines.append('   </Track>')

# ── Track 11: AUGE 168s - 179.212s ───────────────────────────────────────────
# Strobe/climax total nas batidas, alternando branco/vermelho/azul
lines.append('   <Track ID="11" Name="AUGE 168-179s" isMute="0">')
beat_section = [(b, i) for i, b in enumerate(beats) if 168.0 <= b <= 179.212]
auge_funcs = [
    (16, "#FFFFFF"),  # branco total
    (23, "#FF0000"),  # flash vermelho
    (24, "#FFFFFF"),  # flash branco
    (31, "#FF0000"),  # vermelho total
    (16, "#FFFFFF"),
    (32, "#0000FF"),  # azul total
]
for idx, (b, i) in enumerate(beat_section):
    func_id, color = auge_funcs[idx % len(auge_funcs)]
    dur = beat_duration(beats, i)
    lines.append(sf_ms(func_id, ms(b), dur, color))
lines.append('   </Track>')

# ─── Imprime resultado ────────────────────────────────────────────────────────
print("\n".join(lines))
