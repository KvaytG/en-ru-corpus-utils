# en-ru-corpus-utils

![Python 3.10](https://img.shields.io/badge/Python-3.10-blue?logo=python) ![MIT License](https://img.shields.io/badge/License-MIT-green) [![Sponsor](https://img.shields.io/badge/Sponsor-%E2%9D%A4-red)](https://kvaytg.ru/donate.php?lang=en)

Utilities for preparing and cleaning English-Russian parallel corpora

## 📚 Usage
```python
from en_ru_corpus_utils import clean_corpus_from_unpaired_quotes_and_brackets, \
    save_distilled_labse, filter_by_labse, remove_matching_lines, merge_parallel_files, \
    remove_duplicates, filter_single_words, filter_corpus, generate_months_corpus

# 1. Basic cleaning
filter_corpus('data/corpus.txt', 'data/1.txt')

# 2. Additional corpus generation
generate_months_corpus('data/months.txt')

# 3. Semantic filtering (higher threshold)
save_distilled_labse('data/labse_m2v_384')
filter_by_labse('data/labse_m2v_384', 'data/1.txt', 'data/2.txt', 0.7)

# 4. Structural cleanup
clean_corpus_from_unpaired_quotes_and_brackets('data/2.txt', 'data/3.txt')

# 5. Test set filtering
remove_matching_lines('data/3.txt', 'data/FLORES200/flores_200.dev_test.txt', 'data/4.txt')

# 6. Merging and deduplication
merge_parallel_files(['data/4.txt', 'data/months.txt', 'data/dictionary.txt'], 'data/5.txt')
remove_duplicates('data/5', 'data/6')

# 7. Final fine filtering
filter_single_words('data/6.txt', 'data/final.txt',
                    ['data/stop-words/ru-stop-words.txt',
                     'data/stop-words/en-stop-words.txt'])
```

## ⚙️ Installation
```bash
pip install git+https://github.com/KvaytG/en-ru-corpus-utils.git
```

## 📜 License
en-ru-corpus-utils is licensed under the **[MIT license](https://opensource.org/license/mit)**.

This project uses open-source components. For license details see **[pyproject.toml](pyproject.toml)** and dependencies' official websites.
