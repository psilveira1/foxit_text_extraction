# Foxit PDF to Text Automation Script

This Python script automates the conversion of PDF files to Plain Text (`.txt`) using **Foxit PDF Editor**. instead of using external libraries for conversion, it utilizes Foxit's native engine via GUI Automation (Robotic Process Automation) to ensure maximum fidelity.

## 🚀 Features

* **Automated Navigation:** Crawls through a directory tree recursively.
* **Smart Filtering:** Specifically targets the main PDF in a folder structure while ignoring utility folders like `pdf_parts/` and `pdf_images/`.
* **OCR/Image Detection:** Pre-scans files using `pypdf`. If a PDF is detected as "Image Based" (scanned without text), it is skipped to save time.
* **Native Conversion:** Uses Foxit's "Save As Text" feature via keyboard shortcuts.
* **Safety Mechanisms:** Includes timeouts and secure file closing logic to prevent memory leaks or frozen windows.

## 🛠️ Prerequisites

1.  **Foxit PDF Editor** (installed and set as the default PDF viewer).
2.  **Python 3.x**.
3.  **Required Python Libraries:**
    ```bash
    pip install pyautogui pyperclip pypdf
    ```

## ⚙️ Configuration

### 1. Set up Foxit Custom Shortcut (Crucial)
The script relies on a custom keyboard shortcut (`Alt + T`) to trigger the "Convert to Plain Text" command.

**How to set it up in Foxit PDF Editor:**

1.  Open Foxit PDF Editor.
2.  Right-click anywhere on the top Ribbon/Toolbar and select **Customize Quick Access Toolbar...** (or go to `File` > `Preferences` > `Customize Ribbon`).
3.  Click on the **Keyboard** button (bottom of the window) to open the "Customize Keyboard" dialog.
4.  In the **Categories** list, select **Convert**.
5.  In the **Commands** list, look for **To Plain Text** (or similar, depending on your version).
6.  Click inside the **Press new shortcut key** box.
7.  Press **Alt + T** on your keyboard.
8.  Click **Assign**.
9.  Click **OK** / **Close**.

### 2. Configure the Target Folder
Open the python script (`converter.py`) and locate the configuration section at the top:

```python
# --- YOUR SPECIFIC DIRECTORY ---
DIRETORIO_RAIZ = r"write\your\own\path"

```

Change the path inside the quotes to the root folder you want to analyze.

### 3. Adjust Timeouts (Optional)

If your computer is older or the PDF files are very large (100+ pages), increase the sleep timers in the script to prevent errors:

```python
TEMPO_ABRIR_PDF = 3.5      # Seconds to wait for Foxit to open
TEMPO_CONVERSAO = 2.5      # Seconds to wait for the conversion process

```

## 📂 Folder Structure Logic

The script is designed for the following specific structure. It will process the **Root PDF** but ignore the contents of specific subfolders:

```text
Root_Folder/
├── Document_Folder/
│   ├── Document.pdf           <-- PROCESSED
│   ├── pdf_images/            <-- IGNORED (Skipped)
│   └── pdf_parts/             <-- IGNORED (Skipped)

```

## ▶️ How to Run

1. **Close all running instances of Foxit PDF Editor.**
2. Open your terminal or command prompt.
3. Navigate to the script folder.
4. Run the script:
```bash
python foxit_text_extraction.py

```


5. **⚠️ IMPORTANT:** Once the script starts, **DO NOT TOUCH THE MOUSE OR KEYBOARD**. The script controls your cursor to operate Foxit.
6. To **Abort/Stop** the script in an emergency: Quickly move your mouse cursor to the top-left corner of the screen.

## 📝 Output

* The converted text files will be saved in the **same directory** as the original PDF.
* The filename will match the original PDF (e.g., `Document.pdf` -> `Document.txt`).
* The console will display a log of:
* `[PROCESSANDO]`: Files being converted.
* `[IGNORADO]`: Files skipped (Image-based or already exist).
* `[PULAR]`: Files previously converted.



## ⚠️ Disclaimer

This script uses `pyautogui` to control your mouse and keyboard. Ensure no sensitive windows are open in the background. The author is not responsible for any unintended data modification if the user interferes with the automation process while it is running.

