# Usa una imagen base que tenga soporte para CUDA
FROM nvidia/cuda:11.8.0-runtime-ubuntu20.04

# Establecer el directorio de trabajo
WORKDIR /app

# Instala las dependencias necesarias
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    git \
    wget \
    && apt-get clean

# Instala doctr y ocrmypdf
RUN pip3 install python-doctr[torch,viz]@git+https://github.com/mindee/doctr.git \
    && pip3 install ocrmypdf PyPDF2

# Instalar TensorFlow
# RUN pip install python-doctr[tf,viz]@git+https://github.com/mindee/doctr.git \
#     && pip3 install ocrmypdf PyPDF2

# Copia tu script al contenedor
COPY ocr_script.py /app/ocr_script.py

# Comando para ejecutar tu script
CMD ["python3", "ocr_script.py", "/books"]


# docker build -t ocrd-gpu .
# docker run --gpus all -v $(pwd)/books:/books ocrd-gpu
