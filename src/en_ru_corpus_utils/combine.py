from typing import List


def _get_line(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as source:
        for line in source:
            line = line.strip()
            if line:
                yield line


def combine_parallel_files(output_path: str,
                           source_path: str = 'data/source',
                           target_path: str = 'data/target'):
    with open(output_path, 'w', encoding='utf-8') as f:
        for en_text, ru_text in zip(_get_line(source_path), _get_line(target_path)):
            f.write(f'{en_text}\t{ru_text}\n')


def uncombine_to_parallel_files(input_path: str,
                                source_path: str = 'data/source',
                                target_path: str = 'data/target'):
    with (open(input_path, 'r', encoding='utf-8') as f_in,
          open(source_path, 'w', encoding='utf-8') as f_source,
          open(target_path, 'w', encoding='utf-8') as f_target):
        for line in f_in:
            line = line.strip()
            if line and line.count('\t') == 1:
                en_text, ru_text = line.split('\t', 1)
                f_source.write(f'{en_text}\n')
                f_target.write(f'{ru_text}\n')


def merge_parallel_files(input_paths: List[str],
                         output_path: str):
    with open(output_path, 'a', encoding='utf-8') as f_out:
        for path in input_paths:
            with open(path, 'r', encoding='utf-8') as f_in:
                for line in f_in:
                    line = line.strip()
                    if line and line.count('\t') == 1:
                        f_out.write(line + '\n')
