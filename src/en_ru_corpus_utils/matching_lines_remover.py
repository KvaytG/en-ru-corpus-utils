from tqdm import tqdm
from .internal.file_line_utils import count_lines


def remove_matching_lines(check_path: str,
                          filter_path: str,
                          output_path: str):
    with open(filter_path, 'r', encoding='utf-8') as f:
        check_lines = set(line.strip() for line in f)
    with (open(check_path, 'r', encoding='utf-8') as f_in,
          open(output_path, 'w', encoding='utf-8') as f_out):
        for line in tqdm(f_in, total=count_lines(check_path)):
            line = line.strip()
            if line not in check_lines:
                f_out.write(line + '\n')
