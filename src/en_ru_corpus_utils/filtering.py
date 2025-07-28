import string
import re
from tqdm import tqdm
from .internal.file_line_utils import count_lines

_html_tag_pattern = re.compile(r'<[^>]+>')
_excessive_char_pattern = re.compile(r'(.)\1{4,}')

_punctuation_set = set(string.punctuation).union({'–', '«', '»'})

_common_punctuation = re.escape(''.join(_punctuation_set))
_en_letter_pattern = re.compile(fr'^[a-zA-Z\s\d{_common_punctuation}]+$')
_ru_letter_pattern = re.compile(fr'^[а-яА-ЯёЁ\s\d{_common_punctuation}]+$')

_numbers_pattern = re.compile(r'\d')
_space_pattern = re.compile(r'\s+')


def _clean_text(text: str) -> str:
    return _space_pattern.sub(' ', text).strip()


def _has_abnormal_length(en_text: str,
                         ru_text: str,
                         min_length: int = 5,
                         max_length: int = 500) -> bool:
    return not (min_length <= len(en_text) <= max_length) or \
        not (min_length <= len(ru_text) <= max_length)


def _has_mostly_digits_or_punctuation(en_text: str,
                                      ru_text: str,
                                      percent: float = 0.4) -> bool:

    def _is_mostly_digits_or_punctuation(text: str) -> bool:
        count = sum(1 for char in text if char in _punctuation_set or char.isdigit())
        return (count / len(text)) > percent

    return _is_mostly_digits_or_punctuation(en_text) or _is_mostly_digits_or_punctuation(ru_text)


def _contains_html(text: str) -> bool:
    return bool(_html_tag_pattern.search(text))


def _has_excessive_repetitions(en_text: str,
                               ru_text: str) -> bool:
    return (bool(_excessive_char_pattern.search(en_text))) or (bool(_excessive_char_pattern.search(ru_text)))


def _has_punctuation_mismatch(en_text: str,
                              ru_text: str,
                              threshold: int = 5) -> bool:
    en_punctuation_count = sum(1 for char in en_text if char in _punctuation_set)
    ru_punctuation_count = sum(1 for char in ru_text if char in _punctuation_set)
    return abs(en_punctuation_count - ru_punctuation_count) > threshold


def _has_invalid_language(en_text: str,
                          ru_text: str) -> bool:
    return not (_en_letter_pattern.match(en_text)) or not (_ru_letter_pattern.match(ru_text))


def _have_numbers_mismatch(en_text: str,
                           ru_text: str) -> bool:
    en_digits = _numbers_pattern.findall(en_text)
    ru_digits = _numbers_pattern.findall(ru_text)
    return sorted(en_digits) != sorted(ru_digits)


def _have_abnormal_length_difference(
        en_text: str,
        ru_text: str,
        threshold: float = 12.17) -> bool:
    length1, length2 = len(en_text), len(ru_text)
    if length1 == length2:
        return False
    length_difference = abs(length1 - length2) * 100 / max(length1, length2)
    return length_difference >= threshold


def _is_valid_pair(enText: str, ruText: str) -> bool:
    enText = _clean_text(enText)
    ruText = _clean_text(ruText)
    if enText == ruText:
        return False
    if _has_abnormal_length(enText, ruText):
        return False
    if _has_mostly_digits_or_punctuation(enText, ruText):
        return False
    if _contains_html(enText) or _contains_html(ruText):
        return False
    if _has_excessive_repetitions(enText, ruText):
        return False
    if _has_invalid_language(enText, ruText):
        return False
    if _has_punctuation_mismatch(enText, ruText):
        return False
    if _have_numbers_mismatch(enText, ruText):
        return False
    if _have_abnormal_length_difference(enText, ruText, threshold=50.0):
        return False
    return True


def filter_corpus(input_path: str, output_path: str):
    with (open(input_path, "r", encoding="utf-8") as file_in,
          open(output_path, "w", encoding="utf-8") as file_out):
        for line in tqdm(file_in, total=count_lines(input_path), desc="Filtering"):
            line = line.strip()
            if line and line.count('\t') == 1:
                en_text, ru_text = line.split('\t', 1)
                if _is_valid_pair(en_text, ru_text):
                    file_out.write(f'{en_text}\t{ru_text}\n')
