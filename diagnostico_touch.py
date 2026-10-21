import os
import sys
import tkinter as tk
import customtkinter as ctk

# Comprobar tipo de sesión gráfica en Linux
session_type = os.environ.get("XDG_SESSION_TYPE", "desconocido").lower()

app = ctk.CTk()
app.title("Diagnóstico de Pantalla Táctil - KOSTAL")
app.geometry("600x480")

frame = ctk.CTkFrame(app, corner_radius=12)
frame.pack(padx=20, pady=20, fill="both", expand=True)

lbl_title = ctk.CTkLabel(
    frame,
    text="PRUEBA DE TÁCTIL (TOUCH)",
    font=("Arial", 20, "bold"),
    text_color="#1E3A8A"
)
lbl_title.pack(pady=(16, 8))

# Estado de la sesión Wayland vs X11
es_wayland = "wayland" in session_type
color_sesion = "#DC2626" if es_wayland else "#059669"
txt_sesion = (
    f"⚠️ Sesión Actual: WAYLAND (Causa del problema)\n"
    "En Wayland, Ubuntu no envía toques táctiles a Python Tkinter.\n"
    "Solución: Cambiar a 'Ubuntu on Xorg' en el inicio de sesión."
    if es_wayland else
    f"✓ Sesión Actual: X11 / XORG (Correcto)\n"
    "En X11, Ubuntu traduce todos los toques a clics de ratón para Python."
)

lbl_info = ctk.CTkLabel(
    frame,
    text=txt_sesion,
    font=("Arial", 12, "bold"),
    text_color=color_sesion,
    justify="center"
)
lbl_info.pack(pady=10)

contador_toques = 0
lbl_counter = ctk.CTkLabel(
    frame,
    text="Toques detectados: 0",
    font=("Arial", 18, "bold"),
    text_color="#334155"
)
lbl_counter.pack(pady=10)

lbl_detalle = ctk.CTkLabel(
    frame,
    text="Toca el botón grande abajo con tu dedo para probar.",
    font=("Arial", 12),
    text_color="#64748B"
)
lbl_detalle.pack(pady=5)

def al_tocar(origen="BOTÓN"):
    global contador_toques
    contador_toques += 1
    lbl_counter.configure(
        text=f"¡TOQUE DETECTADO! Total: {contador_toques}",
        text_color="#059669"
    )
    lbl_detalle.configure(
        text=f"✓ Último toque recibido desde: {origen}",
        text_color="#059669"
    )
    print(f"[{origen}] Toque detectado #{contador_toques}")

btn_prueba = ctk.CTkButton(
    frame,
    text="👉 TOCA AQUÍ CON TU DEDO 👈",
    font=("Arial", 16, "bold"),
    height=80,
    corner_radius=16,
    fg_color="#2563EB",
    hover_color="#1D4ED8",
    command=lambda: al_tocar("BOTÓN CTK")
)
btn_prueba.pack(padx=30, pady=20, fill="x")

# Canvas directo para probar coordenadas táctiles
canvas_test = tk.Canvas(frame, bg="#F1F5F9", height=80, highlightthickness=1, highlightbackground="#CBD5E1")
canvas_test.pack(padx=30, pady=10, fill="x")
canvas_test.create_text(250, 40, text="O toca dentro de este recuadro gris", font=("Arial", 11), fill="#64748B")

def al_tocar_canvas(event):
    al_tocar(f"CANVAS en X={event.x}, Y={event.y}")

canvas_test.bind("<Button-1>", al_tocar_canvas)
canvas_test.bind("<ButtonRelease-1>", al_tocar_canvas)

app.mainloop()
