import sys
import subprocess
import os

def ensure_installed(package):
    try:
        __import__(package.replace("-", "_"))
    except ImportError:
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# We use mlx-whisper which is highly optimized for Apple Silicon (M1/M2/M3)
ensure_installed("mlx-whisper")

import mlx_whisper

files = [
    ("How_the_Vagus_Nerve_Controls_Inflammation.m4a", "Medical terminology: Fibromyalgia, Vagus Nerve, Inflammation, central sensitization, neuroimmune, neuroinflammation."),
    ("Fibromyalgia_is_a_measurable_computational_disorder.m4a", "Medical terminology: Fibromyalgia, measurable, computational disorder, neurology, diagnostic markers."),
    ("Why_Fibromyalgia_Is_a_Data_Corruption_Problem.m4a", "Medical terminology: Fibromyalgia, data corruption problem, central nervous system, sensory processing.")
]

for audio_file, prompt in files:
    if not os.path.exists(audio_file):
        print(f"File not found: {audio_file}. Skipping.")
        continue
        
    print(f"\n--- Transcribing {audio_file} ---")
    
    # We use the mlx-community Whisper base (or change to small/medium for higher accuracy)
    result = mlx_whisper.transcribe(
        audio_file,
        path_or_hf_repo="mlx-community/whisper-base-mlx",
        initial_prompt=prompt
    )
    
    out_file = audio_file.replace(".m4a", ".txt")
    with open(out_file, "w") as f:
        f.write(result["text"])
    print(f"Saved transcription to {out_file}")

print("\nAll transcriptions complete!")
