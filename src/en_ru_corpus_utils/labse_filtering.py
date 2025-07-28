from model2vec import StaticModel
import torch.nn.functional as F
from torch import Tensor, tensor
from tqdm import tqdm
from .internal.file_line_utils import count_lines


def _cosine_similarity(vector1: Tensor, vector2: Tensor) -> float:
    vector1 = tensor(vector1).unsqueeze(0)
    vector2 = tensor(vector2).unsqueeze(0)
    return F.cosine_similarity(vector1, vector2).item()


def _process_batch(model,
                   en_texts: list[str],
                   ru_texts: list[str],
                   threshold: float) -> set[str]:
    en_embeds = model.encode(en_texts, convert_to_tensor=True, device='cuda', normalize_embeddings=True)
    ru_embeds = model.encode(ru_texts, convert_to_tensor=True, device='cuda', normalize_embeddings=True)
    return {
        f"{en}\t{ru}" for i, (en, ru) in enumerate(zip(en_texts, ru_texts))
        if _cosine_similarity(en_embeds[i], ru_embeds[i]) >= threshold
    }


def filter_by_labse(model_path: str,
                    input_path: str,
                    output_path: str,
                    threshold: float,
                    batch_size: int = 64):
    model = StaticModel.from_pretrained(model_path)
    buffer = set()
    with (open(input_path, 'r', encoding='utf-8') as f_in,
          open(output_path, 'w', encoding='utf-8', newline='\n') as f_out):
        en_batch, ru_batch = [], []
        for line in tqdm(f_in, total=count_lines(input_path), desc="LaBSE filtering"):
            parts = line.strip().split('\t', 1)
            if len(parts) == 2:
                en, ru = parts
                en_batch.append(en)
                ru_batch.append(ru)
                if len(en_batch) >= batch_size:
                    buffer.update(_process_batch(model, en_batch, ru_batch, threshold))
                    en_batch, ru_batch = [], []
                    if len(buffer) >= 1_000_000:
                        f_out.write("\n".join(buffer) + "\n")
                        buffer.clear()
        if en_batch:
            buffer.update(_process_batch(model, en_batch, ru_batch, threshold))
        if buffer:
            f_out.write("\n".join(buffer) + "\n")
