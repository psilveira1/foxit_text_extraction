# Automated Foxit PDF to Text Converter

A Python RPA tool designed to automate the batch conversion of PDF documents to Plain Text (`.txt`) using **Foxit PDF Editor**.

> **⚠️ IMPORTANT:** This script requires the **Paid/Premium Version** of Foxit PDF Editor. It will **not** work with the free "Foxit Reader", as the specific conversion tools and menus are part of the paid suite.

## 📖 Overview

This script navigates through a complex directory structure to find specific PDF files. It performs a "pre-flight check" to ensure the file contains selectable text (skipping scanned/image-based files) and then automates the Foxit GUI to save the file as text.

By using Foxit's native conversion engine via GUI automation, this tool ensures higher fidelity in text extraction while eliminating manual repetitive work.

## ✨ Key Features

* **Smart Recursive Scanning:** Traverses the root directory but strictly ignores specific utility subfolders (e.g., `pdf_parts`, `pdf_images`) to process only the main documents.
* **OCR/Image Detection:** Uses `pypdf` to quickly scan the first 3 pages of a file. If no text is found (indicating a scanned document/image), the script skips the file to save processing time.
* **GUI Automation:** Controls the mouse and keyboard to open the PDF, trigger the conversion via a custom shortcut (`Alt+T`), and enforce saving the output in the source directory.
* **Stability:** Includes logic to handle "Save Changes" dialogs and force-close tabs to prevent memory leaks during large batch operations.

## 🚀 Quick Usage

1.  **Requirements:**
    * **Foxit PDF Editor (Paid Version)**.
    * Python 3.x.
    * Libraries: `pip install pyautogui pyperclip pypdf`.
2.  **Setup:** Map the keyboard shortcut **Alt + T** to the *"Convert to Plain Text"* command inside Foxit.
3.  **Run:** Configure your target path in the script and run. The script will automatically open, convert, and close files.

> **Note:** This script takes control of the mouse and keyboard. Do not use the computer while the automation is running.
