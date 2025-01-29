import PyPDF2

def separar_pdf(input_pdf):
    # Abrir el archivo PDF original
    with open(input_pdf, "rb") as archivo_pdf:
        lector = PyPDF2.PdfReader(archivo_pdf)

        # Iterar sobre cada página
        for pagina_num in range(len(lector.pages)):
            escritor = PyPDF2.PdfWriter()
            escritor.add_page(lector.pages[pagina_num])

            # Guardar cada página como un archivo PDF individual
            with open(f"pagina_{pagina_num + 1}.pdf", "wb") as salida:
                escritor.write(salida)

# Usar la función con el archivo PDF en la carpeta de trabajo
input_pdf = "Pavement-Analysis-and-Design-by-Yang-H-Huang.pdf"  # Reemplaza con la ruta de tu archivo PDF
separar_pdf(input_pdf)
