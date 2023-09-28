import tkinter as tk
from tkinter import scrolledtext
import subprocess


# Fonction appelée lorsque le bouton "Inject" est cliqué
def inject_script():
    script = script_text.get("1.0", "end-1c")  # Obtenez le script Lua du champ de texte
    try:
        # Créez un fichier temporaire pour stocker le script Lua
        with open("temp_script.lua", "w") as temp_file:
            temp_file.write(script)

        # Utilisez subprocess pour exécuter le script Lua dans Roblox
        subprocess.Popen(["", "--script", "temp_script.lua"])

        result_label.config(text="Injection réussie!")
    except Exception as e:
        result_label.config(text=f"Erreur d'injection : {str(e)}")


# Créez une fenêtre Tkinter
window = tk.Tk()
window.title("Roblox Script Injector")
window.configure(bg="black")  # Définissez le fond de la fenêtre en noir

# Créez un champ de texte pour le script Lua
script_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=15, bg="black", fg="white")
script_text.pack(pady=10)

# Créez un bouton "Inject" pour exécuter le script
inject_button = tk.Button(window, text="Inject", command=inject_script, bg="green", fg="white")
inject_button.pack()

# Créez une étiquette pour afficher le résultat de l'injection
result_label = tk.Label(window, text="", bg="black", fg="white")
result_label.pack(pady=10)

# Lancez l'interface utilisateur
window.mainloop()
