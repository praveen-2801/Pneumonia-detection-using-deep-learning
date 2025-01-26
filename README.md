# Pneumonia Detection Using Deep Learning Models

## Overview
This project aims to detect pneumonia using deep learning models on chest X-ray images. A dataset from Kaggle with 7,189 images was used to classify X-rays as normal or pneumonia-affected. The objective was to develop a high-performing model for accurate and efficient pneumonia detection.

## Methodology
- **Dataset Preprocessing**: Resized, normalized, and augmented images to enhance model performance.
- **Deep Learning Models Used**:
  - VGG16 and VGG19 (pretrained on ImageNet).
  - ResNet-50 and ResNet-101 for deeper architecture experiments.
- **Training and Testing**: Models were evaluated using accuracy as the primary metric.

## Results
- VGG19 achieved the best accuracy: **93.12%**.
- Comparison with prior research methods showed competitive performance:
  - Proposed method: 93.12%
  - Other methods: 76.5%–82%.

## Technologies Used
- **Frameworks and Libraries**: TensorFlow, Keras, NumPy, Matplotlib.
- **Models**: VGG16, VGG19, ResNet-50, ResNet-101.
- **Tools**: Jupyter Notebook, Kaggle for dataset access.

## Features
- Automated classification of X-ray images as normal or pneumonia-affected.
- Scalable and robust models leveraging deep neural networks.
- Performance visualization with accuracy graphs for comparative analysis.

## Conclusion
VGG19 outperformed other models with 93.12% accuracy, demonstrating its effectiveness for pneumonia detection. This project highlights the power of deep learning in aiding medical diagnostics.

## References
- Dataset: Kaggle (https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)
