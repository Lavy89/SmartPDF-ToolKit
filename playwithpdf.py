import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from tkinter.scrolledtext import ScrolledText
from PyPDF2 import PdfReader, PdfWriter
from pdf2image import convert_from_path
from PIL import Image
from reportlab.pdfgen import canvas
import os

# Initialize the application
root = tk.Tk()
root.title("SmartPdf ToolKit")
root.geometry("1000x700")
root.resizable(False, False)

# App Data
app_data = {"pdf_path": None, "output_folder": os.getcwd()}

# Functions
def upload_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        lbl_file.config(text=f"Selected: {os.path.basename(file_path)}")
        app_data["pdf_path"] = file_path

# Extract Text
def extract_text():
    if not app_data["pdf_path"]:
        messagebox.showerror("Error", "Please upload a PDF first!")
        return

    reader = PdfReader(app_data["pdf_path"])
    choice = simpledialog.askstring(
        "Extract Text",
        "Type 'full' to extract all text or provide a page number (e.g., '2'):",
    )

    try:
        if choice.lower() == "full":
            text = "".join(page.extract_text() for page in reader.pages)
        else:
            page_number = int(choice) - 1
            text = reader.pages[page_number].extract_text()

        txt_display.delete("1.0", tk.END)
        txt_display.insert(tk.END, text)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Merge PDFs
def merge_pdfs():
    first_pdf = filedialog.askopenfilename(title="Select 1st file",filetypes=[("PDF Files", "*.pdf")])
    if not first_pdf:
        return

    second_pdf = filedialog.askopenfilename(title="Select 2nd file",filetypes=[("PDF Files", "*.pdf")])
    if not second_pdf:
        return

    output_file = filedialog.asksaveasfilename(
        title="Save Merged PDF",
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")],
    )
    if not output_file:
        return

    writer = PdfWriter()
    for file in [first_pdf, second_pdf]:
        reader = PdfReader(file)
        for page in reader.pages:
            writer.add_page(page)

    with open(output_file, "wb") as f:
        writer.write(f)

    messagebox.showinfo("Success", f"Merged PDF saved as {output_file}")

# Split PDF
def split_pdf():
    if not app_data["pdf_path"]:
        messagebox.showerror("Error", "Please upload a PDF first!")
        return

    page_number = simpledialog.askinteger(
        "Split PDF", "Enter the page number to split at:"
    )
    if not page_number:
        return

    reader = PdfReader(app_data["pdf_path"])
    writer1, writer2 = PdfWriter(), PdfWriter()

    for i, page in enumerate(reader.pages):
        if i < page_number - 1:
            writer1.add_page(page)
        else:
            writer2.add_page(page)

    output_file1 = filedialog.asksaveasfilename(
        title="Save First Part",
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")],
    )
    output_file2 = filedialog.asksaveasfilename(
        title="Save Second Part",
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")],
    )

    with open(output_file1, "wb") as f1, open(output_file2, "wb") as f2:
        writer1.write(f1)
        writer2.write(f2)

    messagebox.showinfo("Success", "PDF split successfully!")

# Compress PDF
def compress_pdf():
    if not app_data["pdf_path"]:
        messagebox.showerror("Error", "Please upload a PDF first!")
        return

    output_file = filedialog.asksaveasfilename(
        title="Save Compressed PDF",
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")],
    )
    if not output_file:
        return

    reader = PdfReader(app_data["pdf_path"])
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    with open(output_file, "wb") as f:
        writer.write(f)

    messagebox.showinfo("Success", f"Compressed PDF saved as {output_file}")

# Convert PDF to Images
def pdf_to_images():
    if not app_data["pdf_path"]:
        messagebox.showerror("Error", "Please upload a PDF first!")
        return

    output_folder = filedialog.askdirectory(title="Select Output Folder")
    if not output_folder:
        return

    images = convert_from_path(app_data["pdf_path"], dpi=150)
    for i, image in enumerate(images):
        image.save(os.path.join(output_folder, f"page_{i + 1}.png"), "PNG")

    messagebox.showinfo("Success", f"PDF pages converted to images in {output_folder}")

# Convert Images to PDF
def images_to_pdf():
    image_files = filedialog.askopenfilenames(
        title="Select Images to Convert",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")],
    )
    if not image_files:
        return

    output_file = filedialog.asksaveasfilename(
        title="Save PDF",
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")],
    )
    if not output_file:
        return

    images = [Image.open(img).convert("RGB") for img in image_files]
    images[0].save(output_file, save_all=True, append_images=images[1:])

    messagebox.showinfo("Success", f"Images converted to PDF saved as {output_file}")

# Convert Text to PDF
def text_to_pdf():
    text_file = filedialog.askopenfilename(
        title="Select a Text File",
        filetypes=[("Text Files", "*.txt")],
    )
    if not text_file:
        return

    output_file = filedialog.asksaveasfilename(
        title="Save PDF",
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")],
    )
    if not output_file:
        return

    c = canvas.Canvas(output_file)
    with open(text_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        y = 800
        for line in lines:
            c.drawString(50, y, line.strip())
            y -= 15
            if y < 50:
                c.showPage()
                y = 800
    c.save()

    messagebox.showinfo("Success", f"Text file converted to PDF saved as {output_file}")

# UI Elements
lbl_title = tk.Label(root, text="PDF Utility Tool", font=("Arial", 24, "bold"))
lbl_title.pack(pady=10)

btn_upload = tk.Button(root, text="Upload PDF", width=20, command=upload_pdf)
btn_upload.pack(pady=5)

lbl_file = tk.Label(root, text="No file selected", font=("Arial", 12))
lbl_file.pack(pady=5)

btn_extract_text = tk.Button(root, text="Extract Text", width=20, command=extract_text)
btn_extract_text.pack(pady=5)

btn_merge_pdfs = tk.Button(root, text="Merge PDFs", width=20, command=merge_pdfs)
btn_merge_pdfs.pack(pady=5)

btn_split_pdf = tk.Button(root, text="Split PDF", width=20, command=split_pdf)
btn_split_pdf.pack(pady=5)

btn_compress_pdf = tk.Button(root, text="Compress PDF", width=20, command=compress_pdf)
btn_compress_pdf.pack(pady=5)

btn_pdf_to_images = tk.Button(root, text="PDF to Images", width=20, command=pdf_to_images)
btn_pdf_to_images.pack(pady=5)

btn_images_to_pdf = tk.Button(root, text="Images to PDF", width=20, command=images_to_pdf)
btn_images_to_pdf.pack(pady=5)

btn_text_to_pdf = tk.Button(root, text="Text to PDF", width=20, command=text_to_pdf)
btn_text_to_pdf.pack(pady=5)

txt_display = ScrolledText(root, width=120, height=20, font=("Arial", 12))
txt_display.pack(pady=10)

# Start the application
root.mainloop()
