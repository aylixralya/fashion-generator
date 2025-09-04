import numpy as np
import matplotlib.pyplot as plt
import json
def load_mnist_images_labels(images_path, labels_path, num=5):
    import gzip
    with gzip.open(labels_path, 'rb') as lbpath:
        lbpath.read(8)
        labels = np.frombuffer(lbpath.read(), dtype=np.uint8)
    with gzip.open(images_path, 'rb') as imgpath:
        imgpath.read(16)
        images = np.frombuffer(imgpath.read(), dtype=np.uint8).reshape(-1, 28, 28)
    return images[:num], labels[:num]

def show_mnist_images(images, labels):
    fig, axes = plt.subplots(1, len(images), figsize=(10,2))
    for i, ax in enumerate(axes):
        ax.imshow(images[i], cmap='gray')
        ax.set_title(f'Label: {labels[i]}')
        ax.axis('off')
    plt.show()

def show_deepfashion_captions(captions_json, n=3):
    with open(captions_json, 'r') as f:
        captions = json.load(f)
    for i, (img, meta) in enumerate(list(captions.items())[:n]):
        print(f"Bild: {img}\nBeschreibung: {meta}\n")

def show_modanet_annotations(json_path, n=2):
    with open(json_path, 'r') as f:
        modanet = json.load(f)
    for i, ann in enumerate(modanet['annotations'][:n]):
        print(f"Bild-ID: {ann['image_id']}")
        print(f"Kategorien: {ann['category_id']}")
        print(f"Segmente: {ann['segmentation'][:1]}\n")
