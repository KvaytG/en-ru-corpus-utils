from tqdm import tqdm
from .internal.file_line_utils import count_lines


def _remove_unpaired_quotes_and_brackets(line: str):
    if (line.count('“') + line.count('”')) % 2 != 0:
        line = line.replace('“', '')
        line = line.replace('”', '')
    if (line.count('«') + line.count('»')) % 2 != 0:
        line = line.replace('«', '')
        line = line.replace('»', '')
    while line.count('"') % 2 != 0:
        line = line.replace('"', '', 1)
    while line.count('[') != line.count(']'):
        if '[' in line:
            line = line.replace('[', '', 1)
        if ']' in line:
            line = line.replace(']', '', 1)
    while line.count('(') != line.count(')'):
        if '(' in line:
            line = line.replace('(', '', 1)
        if ')' in line:
            line = line.replace(')', '', 1)
    while line.count('{') != line.count('}'):
        if '{' in line:
            line = line.replace('{', '', 1)
        if '}' in line:
            line = line.replace('}', '', 1)
    return line


def clean_corpus_from_unpaired_quotes_and_brackets(input_path: str,
                                                   output_path: str):
    with (open(input_path, "r", encoding="utf-8") as file_in,
          open(output_path, "w", encoding="utf-8") as file_out):
        for line in tqdm(file_in, total=count_lines(input_path), desc="Cleaning quotes and brackets"):
            line = line.strip()
            if line and line.count('\t') == 1:
                line = _remove_unpaired_quotes_and_brackets(line)
                file_out.write(f'{line}\n')
