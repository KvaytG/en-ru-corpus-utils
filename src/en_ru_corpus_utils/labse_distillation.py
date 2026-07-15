from model2vec.distill import distill
import os


def save_distilled_labse(output_model_path: str, pca_dims: int = 384):
    if os.path.exists(os.path.join(output_model_path, 'model.safetensors')):
        print(f"Model already exists at: {output_model_path}")
        return
    print(f"Starting distillation of LaBSE model with pca_dims={pca_dims}...")
    m2v_model = distill(model_name='sentence-transformers/LaBSE', pca_dims=pca_dims)
    m2v_model.save_pretrained(output_model_path)
    print(f"Model saved to {output_model_path}")
