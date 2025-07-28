import os
from removedup import rdup
from .combine import uncombine_to_parallel_files, combine_parallel_files


def remove_duplicates(input_base_path: str,
                      output_base_path: str):
    print(f'Removing duplicates...')
    input_path = f'{input_base_path}.txt'
    source_path = f'{input_base_path}-source.txt'
    target_path = f'{input_base_path}-target.txt'
    output_path = f'{output_base_path}.txt'
    uncombine_to_parallel_files(input_path=input_path, source_path=source_path, target_path=target_path)
    _, _, removed = rdup(source_path, target_path)
    print(f'Removed duplicates: {removed} items')
    os.remove(source_path)
    os.remove(target_path)
    source_dedup = f'{source_path}.dedup'
    target_dedup = f'{target_path}.dedup'
    combine_parallel_files(source_path=source_dedup, target_path=target_dedup, output_path=output_path)
    os.remove(source_dedup)
    os.remove(target_dedup)
