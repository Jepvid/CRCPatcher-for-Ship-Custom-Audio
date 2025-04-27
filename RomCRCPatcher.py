import sys
import os
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SETTINGS_FILE = SCRIPT_DIR / "settings.txt"
OUTPUT_ROM = SCRIPT_DIR / "patched_rom.z64"

def check_required_files():
    required_files = ["soh.exe", "soh.otr"]
    missing = []

    for filename in required_files:
        if not (SCRIPT_DIR / filename).exists():
            missing.append(filename)

    if missing:
        print("❌ ERROR: This script must be placed in a folder that contains:")
        for file in required_files:
            print(f" - {file}")
        print("\nMissing files:", ', '.join(missing))
        input("\n⏳ Press ENTER to exit...")
        sys.exit(1)
    else:
        print("✅ Correct folder detected.")

def load_or_create_settings():
    settings = {}

    if SETTINGS_FILE.exists():
        print(f"ℹ️ Loading settings from {SETTINGS_FILE}...")
        with open(SETTINGS_FILE, 'r') as f:
            for line in f:
                key, value = line.strip().split('=', 1)
                settings[key] = value
    else:
        print("⚙️ Settings file not found. Let's set it up.")
        settings['clean_rom'] = input("Enter path to Clean ROM: ").strip()
        settings['decomp_rom'] = input("Enter path to Decomp Build ROM: ").strip()

    return settings

def save_settings(settings):
    with open(SETTINGS_FILE, 'w') as f:
        for key, value in settings.items():
            f.write(f"{key}={value}\n")

def sanity_warning(settings):
    warned_mode = settings.get('warned_mode', 'partial')

    if warned_mode == 'full':
        return  # Already fully confirmed before

    print("\n⚠️  WARNING! ⚠️")
    print("This script will DELETE all .z64 files and oot.otr in this folder before patching.")
    print("Make sure you have backups of anything important.")
    print("\n✅ To continue but keep seeing this warning every time, type: yes")
    print("✅ To continue and NEVER see this warning again, type exactly:")
    print("   Yes, I understand the warning and want to not have the warnings\n")

    confirm = input("Your response: ").strip()

    if confirm == "Yes, I understand the warning and to want not have the warnings":
        settings['warned_mode'] = 'full'
        save_settings(settings)
        print("\n✅ Full confirmation saved. You will not see this warning again.")
    elif confirm.lower() == "yes":
        settings['warned_mode'] = 'partial'
        save_settings(settings)
        print("\nℹ️ Continuing, but you will be warned again next time.")
    else:
        print("\n❌ Invalid response. Aborting for your safety.")
        input("⏳ Press ENTER to exit...")
        sys.exit(1)


def delete_roms_and_otr():
    deleted_files = []

    for file in SCRIPT_DIR.glob("*.z64"):
        try:
            file.unlink()
            deleted_files.append(file.name)
        except Exception as e:
            print(f"⚠️ Failed to delete {file.name}: {e}")

    otr_file = SCRIPT_DIR / "oot.otr"
    if otr_file.exists():
        try:
            otr_file.unlink()
            deleted_files.append("oot.otr")
        except Exception as e:
            print(f"⚠️ Failed to delete oot.otr: {e}")

    if deleted_files:
        print(f"🧹 Deleted files: {', '.join(deleted_files)}")
    else:
        print("ℹ️ No files deleted.")

def patch_n64_rom(source_rom, target_rom, output_rom):
    with open(source_rom, 'rb') as f:
        f.seek(0x10)
        patch_bytes = f.read(8)

    with open(target_rom, 'rb') as f:
        rom_data = bytearray(f.read())

    rom_data[0x10:0x10+8] = patch_bytes

    with open(output_rom, 'wb') as f:
        f.write(rom_data)

    print(f"✅ Patched ROM saved as: {output_rom}")

if __name__ == "__main__":
    check_required_files()      # 🛑 Check soh.exe and soh.otr first
    settings = load_or_create_settings()

    if not SETTINGS_FILE.exists():
        save_settings(settings)

    clean_rom = settings['clean_rom']
    decomp_rom = settings['decomp_rom']

    sanity_warning(settings)    # ⚡ Warn about deletes
    delete_roms_and_otr()       # 🧹 Clean up files
    patch_n64_rom(clean_rom, decomp_rom, OUTPUT_ROM)  # ✨ Patch rom

