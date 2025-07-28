from tqdm import tqdm
from .internal.file_line_utils import count_lines


def remove_matching_lines(check_path: str,
                          filter_path: str,
                          output_path: str):
    print(f"Loading lines from filter file: {filter_path}")
    with open(filter_path, 'r', encoding='utf-8') as f:
        check_lines = set(line.strip() for line in f)
    print(f"Loaded {len(check_lines)} lines to filter out.")
    total_lines = count_lines(check_path)
    print(f"Processing {total_lines} lines from {check_path}...")
    with (open(check_path, 'r', encoding='utf-8') as f_in,
          open(output_path, 'w', encoding='utf-8') as f_out):
        for line in tqdm(f_in, total=total_lines):
            line = line.strip()
            if line not in check_lines:
                f_out.write(line + '\n')
    print(f"Filtered lines written to {output_path}")
