import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

# Translation Application Class
class TranslationApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Translation Application")
        self.geometry("600x400")
        self.configure(bg='#181818')  # Dark background

        # Initialize the translator
        self.translator = Translator()

        self.create_widgets()

    def create_widgets(self):
        # Source Language Label
        src_lang_label = tk.Label(self, text="Source Language:", bg="#181818", fg="white", font=("Arial", 12))
        src_lang_label.pack(pady=10)

        # Source Language Dropdown
        self.src_lang_combo = ttk.Combobox(self, state="readonly", values=list(LANGUAGES.values()), font=("Arial", 12))
        self.src_lang_combo.set("English")
        self.src_lang_combo.pack(pady=10)
        
        # Target Language Label
        tgt_lang_label = tk.Label(self, text="Target Language:", bg="#181818", fg="white", font=("Arial", 12))
        tgt_lang_label.pack(pady=10)

        # Target Language Dropdown
        self.tgt_lang_combo = ttk.Combobox(self, state="readonly", values=list(LANGUAGES.values()), font=("Arial", 12))
        self.tgt_lang_combo.set("Spanish")
        self.tgt_lang_combo.pack(pady=10)

        # Translate Button
        translate_button = tk.Button(self, text="Translate", font=("Arial", 12, "bold"), bg="#FF0000", fg="white", command=self.translate_text)
        translate_button.pack(pady=10)
        
        # Textbox for Source Text
        self.src_textbox = tk.Text(self, height=5, font=("Arial", 12), wrap="word", bg="#282828", fg="white", insertbackground='white')  # Dark textbox
        self.src_textbox.pack(padx=20, pady=10)

        # Textbox for Translated Text
        self.tgt_textbox = tk.Text(self, height=5, font=("Arial", 12), wrap="word", state="disabled", bg="#282828", fg="white")  # Dark textbox
        self.tgt_textbox.pack(padx=20, pady=10)

    def translate_text(self):
        try:
            src_lang = self.get_language_code(self.src_lang_combo.get())
            tgt_lang = self.get_language_code(self.tgt_lang_combo.get())
            src_text = self.src_textbox.get("1.0", tk.END).strip()

            if not src_text:
                messagebox.showwarning("Input Error", "Please enter some text to translate.")
                return

            # Translate text
            translated = self.translator.translate(src_text, src=src_lang, dest=tgt_lang)
            self.show_translation(translated.text)

        except Exception as e:
            messagebox.showerror("Translation Error", f"An error occurred: {str(e)}")

    def get_language_code(self, language_name):
        # Find the language code based on the language name selected
        for code, lang in LANGUAGES.items():
            if lang == language_name:
                return code
        return 'en'

    def show_translation(self, translated_text):
        # Enable the target textbox to update the text, then disable again
        self.tgt_textbox.config(state="normal")
        self.tgt_textbox.delete("1.0", tk.END)
        self.tgt_textbox.insert(tk.END, translated_text)
        self.tgt_textbox.config(state="disabled")

# Run the application
if __name__ == "__main__":
    app = TranslationApp()
    app.mainloop()
