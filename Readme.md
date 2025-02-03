1. Detección de Texto (det_arch):
Este parámetro se refiere a la arquitectura utilizada para detectar texto en las imágenes. Algunas de las opciones disponibles son:

    - fast_base: Una arquitectura rápida y ligera para la detección de texto.
    - db_resnet50: Basada en la arquitectura ResNet-50, es más precisa pero también más pesada en términos de recursos.
    - db_mobilenetv3: Una opción ligera y rápida basada en MobileNetV3, ideal para entornos con recursos limitados.
    - db_resnet101: Similar a db_resnet50, pero con una arquitectura más profunda, lo que puede mejorar la precisión.

2. Reconocimiento de Texto (reco_arch):
Este parámetro se refiere a la arquitectura utilizada para reconocer el texto detectado. Algunas de las opciones son:

    - crnn: Una arquitectura basada en CRNN (Convolutional Recurrent Neural Network) que es adecuada para el reconocimiento de texto en imágenes.
    - parseq: Una arquitectura basada en Transformers que es más reciente y puede ofrecer mejores resultados en algunos casos.
    - trie: Utiliza un enfoque basado en un trie para el reconocimiento de texto, aunque esta opción puede no estar disponible en todas las versiones de docTR.
