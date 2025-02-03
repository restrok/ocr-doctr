import os
import re
from tempfile import TemporaryDirectory
from PyPDF2 import PdfMerger, PdfReader
from doctr.io import DocumentFile
from doctr.models import ocr_predictor, from_hub
from PIL import Image
from ocrmypdf.hocrtransform import HocrTransform
import sys

# Verificar que se ha pasado el argumento de la carpeta
if len(sys.argv) != 2:
    print("Uso: python ocr_script.py <ruta_a_libros>")
    sys.exit(1)

books_folder = sys.argv[1]

# Obtener todos los archivos PDF en la carpeta especificada
pdf_files = [f for f in os.listdir(books_folder) if f.endswith('.pdf')]

# Procesar cada archivo PDF
for pdf_file in pdf_files:
    pdf_path = os.path.join(books_folder, pdf_file)
    docs = DocumentFile.from_pdf(pdf_path)

    # Usar un modelo multilingüe
    reco_model = from_hub("Felix92/doctr-torch-parseq-multilingual-v1")
    model = ocr_predictor(det_arch='fast_base', reco_arch=reco_model, pretrained=True)

    # Procesar el documento
    result = model(docs)
    result.show()

    # Exportar como PDF/A
    xml_outputs = result.export_as_xml()

    # Guardar como PDF/A
    output_pdf_name = f"{os.path.splitext(pdf_file)[0]}-ocr.pdf"
    with TemporaryDirectory() as tmpdir:
        merger = PdfMerger()
        for i, (xml, img) in enumerate(zip(xml_outputs, docs)):
            Image.fromarray(img).save(os.path.join(tmpdir, f"{i}.jpg"))
            with open(os.path.join(tmpdir, f"{i}.xml"), "w") as f:
                f.write(xml_outputs[i][0].decode())
            hocr = HocrTransform(hocr_filename=os.path.join(tmpdir, f"{i}.xml"), dpi=300)
            hocr.to_pdf(out_filename=os.path.join(tmpdir, f"{i}.pdf"), image_filename=os.path.join(tmpdir, f"{i}.jpg"))
            merger.append(os.path.join(tmpdir, f"{i}.pdf"))

        # Guardar como PDF combinado
        merger.write(os.path.join(books_folder, output_pdf_name))

    print(f"Procesado {pdf_file} y guardado como {output_pdf_name}.")
