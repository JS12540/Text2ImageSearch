from chromadb import Documents, EmbeddingFunction, Embeddings

from PIL import Image
import torch
from torchvision.transforms import Compose, Resize, CenterCrop, ToTensor, Normalize
from tqdm import tqdm
from transformers import CLIPProcessor, CLIPModel # CLIPTokenizer, CLIPTokenizerFast


# Install necessary packages
# !pip install torch torchvision transformers tqdm Pillow


class ImageEmbedder(EmbeddingFunction):
    """
    	Initialize the class with the device set to CUDA if available, or CPU. 
        Load the CLIP model and processor from the 'openai/clip-vit-base-patch32' pretrained model. 
        Define image transformations using Resize, CenterCrop, ToTensor, and Normalize.
    """
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"Using device: {self.device}")

        # Load model and processor
        self.processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
        self.model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(self.device)

        # Define image transformations
        self.transform = Compose([
            Resize([224, 224]), 
            CenterCrop(224), 
            ToTensor(),
            Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
        ])

    def __call__(self, image_filenames: Documents) -> Embeddings:
        """
        Function to process a list of image filenames and return their embeddings.

        Args:
            image_filenames (Documents): A list of image filenames to process.

        Returns:
            Embeddings: A list of embeddings corresponding to the input image filenames.
        """
        embeddings = []

        if len(image_filenames) > 1:
            iterator = tqdm(image_filenames)
        else:
            iterator = image_filenames

        for image_path in iterator:
            # Open image as RGB
            image = Image.open(image_path).convert('RGB')
            # Process image
            image = self.transform(image).unsqueeze(0)
            
            # Move image to device
            image = image.to(self.device)

            # Vectorize
            with torch.no_grad():
                image_features = self.model.get_image_features(pixel_values=image)
                embeddings.append(
                    image_features
                    .cpu()
                    .numpy()
                    [0]
                    .tolist()
                )
            
        return embeddings
    
class LanguageEmbedder:
    def __init__(self):
        """
        Initialize the class with the device set to CUDA if available, else CPU. 
        Load the CLIP model and processor from the 'openai/clip-vit-base-patch32' pretrained model and move them to the initialized device.
        """
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"Using device: {self.device}")

        # Load model and processor
        self.model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(self.device)
        self.processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
        # Consider: CLIPTokenizerFast

    def __call__(self, texts):
        """
        Call the function with a list of texts, process the inputs, get text features, and return the output as a list.
        """
        inputs = self.processor(texts, return_tensors="pt", padding=True) # truncation=True
        inputs = inputs.to(self.device)

        with torch.no_grad():
            outputs = self.model.get_text_features(**inputs)

        return outputs \
                .cpu() \
                .numpy() \
                [0] \
                .tolist()