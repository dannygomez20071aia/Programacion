import segno

# 1. ENLACE: Aquí debes poner el link de tu página, WhatsApp o Formulario 
# donde la gente verá el mensaje y el botón de contratar.
enlace_nanys = "https://keep.google.com/?source=gemini#home" 

# 2. Generar el QR con diseño personalizado
qr = segno.make_qr(enlace_nanys)

qr.save(
    "qr_nanys_home.png",
    scale=10,
    dark="#4B0082",  # Un color elegante (Púrpura/Indigo)
    data_dark="#FF69B4", # Detalles en rosa para que sea llamativo
    light="#FFFFFF"  # Fondo blanco
)

print("¡QR de Nanys Home generado con éxito como 'qr_nanys_home.png'!")