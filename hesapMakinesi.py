import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title('Hesap Makinesi')

        self.current_value = 0
        self.history = []

        self.result_var = tk.StringVar()
        self.result_var.set(str(self.current_value))

        self.input_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Hesaplanan değeri gösteren etiket
        self.result_label = tk.Label(self.master, textvariable=self.result_var, font=("Arial", 24))
        self.result_label.pack()

        # Kullanıcı girdisi için metin alanı
        self.input_entry = tk.Entry(self.master, textvariable=self.input_var, font=("Arial", 24))
        self.input_entry.pack()

        # Hesapla butonu
        self.calculate_button = tk.Button(self.master, text="Hesapla", command=self.calculate, font=("Arial", 18))
        self.calculate_button.pack()

        # Geri al butonu
        self.undo_button = tk.Button(self.master, text="Geri Al", command=self.undo, font=("Arial", 18))
        self.undo_button.pack()

    def calculate(self):
        try:
            # Kullanıcı girişini al ve hesaplama yap
            calculation = self.input_var.get()
            if calculation.startswith('+') or calculation.startswith('-'):
                self.current_value += int(calculation)
                self.history.append(self.current_value)
                self.result_var.set(str(self.current_value))
                self.input_var.set('')
        except ValueError:
            self.input_var.set('Hatalı Giriş!')

    def undo(self):
        if self.history:
            self.history.pop()  # Son değeri kaldır
            self.current_value = self.history[-1] if self.history else 0
            self.result_var.set(str(self.current_value))

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
