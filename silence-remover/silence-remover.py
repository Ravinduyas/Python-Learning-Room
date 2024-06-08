import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pydub import AudioSegment

# Set the path to the FFmpeg binary
AudioSegment.converter = "‪C:\Users\Insight\Downloads\ffmpeg-6.1.1.tar.xz"

class AudioGapTrimmerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Audio Gap Trimmer")
        
        self.file_path = tk.StringVar()
        self.file_path.set("No file selected")
        
        self.create_widgets()
        
    def create_widgets(self):
        tk.Label(self.master, text="Select audio file:").grid(row=0, column=0, sticky='w', padx=10, pady=10)
        tk.Entry(self.master, textvariable=self.file_path, width=40).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.master, text="Browse", command=self.browse_file).grid(row=0, column=2, padx=10, pady=10)
        
        tk.Button(self.master, text="Trim Gaps", command=self.trim_gaps).grid(row=1, column=1, padx=10, pady=10)
    
    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp4;*.wav;*.ogg;*.flac")])
        if file_path:
            self.file_path.set(file_path)
    
    def trim_gaps(self):
        file_path = self.file_path.get()
        if not file_path or not os.path.exists(file_path):
            messagebox.showerror("Error", "Please select a valid audio file")
            return
        
        try:
            audio = AudioSegment.from_file(file_path)
            trimmed_audio = self.remove_silence(audio)
            save_path = os.path.splitext(file_path)[0] + "_trimmed.wav"
            trimmed_audio.export(save_path, format="wav")
            messagebox.showinfo("Success", "Audio gaps trimmed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        
    def remove_silence(self, audio):
        # Simple silence removal logic
        non_silence = audio.strip_silence()
        return non_silence

def main():
    root = tk.Tk()
    app = AudioGapTrimmerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
