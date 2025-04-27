# Ship of Harkinian CRC Patcher for Audio Modding

This tool simplifies the process of creating a CRC patch for audio modding when using the **Decomp** method in *Ship of Harkinian*. It automates the steps necessary to patch your ROM and prepare it for modding, all in a simple click-and-run executable.

## Important Notes

- **Back Up Your Files**: The executable will delete all `.z64` files and `oot.otr` in the folder, so make sure to back up any important files before running it.
- **This Tool Simplifies Step 6** of the guide found on [GameBanana](https://gamebanana.com/tuts/18686).

## Setup

1. **Download the Latest Release**  
   Get the latest release from the [GitHub Releases Page](https://github.com/Jepvid/CRCPatcher-for-Ship-Custom-Audio/releases). Download the appropriate version for your system:
   - **Windows**: `patched_rom_windows.exe`
   - **Linux**: `patched_rom_linux`
   - **macOS**: `patched_rom_macos`

2. **Place the Executable in Your Ship of Harkinian Folder**  
   Ensure that the downloaded executable is placed in the same folder as the **soh.exe** and **soh.otr** files.

3. **Required Files**  
   The script requires the following files to be present in the folder:
   - **soh.exe**  
   - **soh.otr**

   The executable will check for these files before proceeding.

4. **For Linux and macOS Users**  
   This tool needs to be run from the terminal. Instructions are provided below for each OS.

## Usage

### For Windows Users:
1. Simply double-click the `patched_rom_windows.exe` executable.  
2. The script will open in a command window and guide you through the necessary steps.

### For Linux and macOS Users:
1. Open a terminal window.
2. Navigate to the folder where the executable is located.
3. This tool needs to be run from the terminal. Instructions are provided below for each OS. Additionally, you may need to give the executable permission to run by using the following command:
   **Linux**
   ```bash
   chmod +x patched_rom_linux
   ```
   **macOS**
   ```bash
   chmod +x patched_rom_macos
   ```
5. Run the executable:
   - **Linux**:  
     ```bash
     ./patched_rom_linux
     ```
   - **macOS**:  
     ```bash
     ./patched_rom_macos
     ```

4. Follow the on-screen prompts to enter the required paths.

## How It Works

When you run the executable for the first time, the following steps will occur:

1. **Check for Required Files**:  
   The executable will check if `soh.exe` and `soh.otr` are present in the folder. If these files are missing, it will display an error and exit.

2. **Request ROM Paths**:  
   The script will prompt you for the following inputs:
   - Path to a **Clean ROM**:  
     Enter the path to the clean version of the ROM (`rom.z64`).
   - Path to a **Decomp Build ROM**:  
     Enter the path to the decompiled ROM (`rom.z64`).

3. **Warning about File Deletion**:  
   The executable will display a warning that it will **delete all `.z64` files** and `oot.otr` in the folder before patching. You must confirm your understanding by typing "Yes" to continue or "No" to cancel.

4. **Patch the ROM**:  
   Once you've confirmed the deletion, the executable will patch the ROM with the CRC values from the decompiled ROM and save it as a new patched ROM (`patched_rom.z64`).
