import qrcode
import tkinter as tk

class QRCodeGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("QR Code Generator")
        self.root.geometry("400x185")
        self.root.resizable(False, False)

        self.label = tk.Label(self.root, text="Enter the text to generate QR Code", font=("Helvetica", 15))
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.root, font=("Helvetica", 15))
        self.entry.pack(pady=10)

        self.button = tk.Button(self.root, text="Generate QR Code", font=("Helvetica", 15), command=self.generate)
        self.button.pack(pady=10)

        self.root.mainloop()

    def generate(self):
        data = self.entry.get()
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")
        img.save("QRCode.png")


if __name__ == "__main__":
    QRCodeGenerator()

