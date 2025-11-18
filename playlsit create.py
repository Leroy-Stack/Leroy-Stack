import os
import json

# CONFIG
MUSIC_FOLDER = "assets/music"
OUTPUT_FILE = "assets/playlist.json"

tracks = []

print(f"📂 Scanning {MUSIC_FOLDER}...")

# Get all files
if os.path.exists(MUSIC_FOLDER):
    files = sorted(os.listdir(MUSIC_FOLDER))
    
    for filename in files:
        if filename.lower().endswith(('.mp3', '.wav', '.m4a', '.ogg')):
            # Create a "pretty" name (remove .mp3 and underscores)
            display_name = os.path.splitext(filename)[0].replace("_", " ").replace("-", " ")
            
            tracks.append({
                "title": display_name,
                "file": filename
            })
            print(f"  - Found: {filename}")

    # Save to JSON file
    with open(OUTPUT_FILE, "w") as f:
        json.dump(tracks, f, indent=2)
        
    print(f"\n✅ Success! Found {len(tracks)} tracks.")
    print(f"📝 Playlist saved to {OUTPUT_FILE}")
else:
    print(f"❌ Error: Folder '{MUSIC_FOLDER}' not found.")
