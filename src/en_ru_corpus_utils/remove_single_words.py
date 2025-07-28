from collections import Counter
import re


def _get_stop_words(stop_words_paths: list[str]) -> set[str]:
    stop_words = set()
    for path in stop_words_paths:
        with open(path, 'r', encoding='utf-8') as f:
            stop_words.update(line.strip() for line in f)
    return stop_words


_words_pattern = re.compile(r'\b\w+\b')


def _split_text(text: str,
                stop_words: set[str],
                remove_stop_words: bool) -> list[str]:
    words = _words_pattern.findall(text.lower())
    if remove_stop_words:
        words = [word for word in words if word not in stop_words]
    return words


def _get_single_words(file_path: str,
                      stop_words: set[str]) -> set[str]:
    frequency = Counter()
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and line.count('\t') == 1:
                frequency.update(_split_text(line, stop_words, True))
    return {word for word, count in frequency.items() if count == 1}


def _is_bad_text(text: str,
                 single_words: set[str],
                 stop_words: set[str]) -> bool:
    words = _split_text(text, stop_words, False)
    return any(word in single_words for word in words)


def filter_single_words(input_path: str,
                        output_path: str,
                        stop_words_paths: list[str]):
    stop_words = _get_stop_words(stop_words_paths)
    single_words = _get_single_words(input_path, stop_words)
    print('Found single words:', len(single_words))
    with open(input_path, 'r', encoding='utf-8') as file_in, \
            open(output_path, 'w', encoding='utf-8') as file_out:
        for line in file_in:
            text = line.strip()
            if text and text.count('\t') == 1:
                if not _is_bad_text(text, single_words, stop_words):
                    file_out.write(text + '\n')
