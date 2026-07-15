
# en-ru-corpus-utils

[![US](https://kvaytg.ru/common/flags/us-21x16.svg) English](README.md) | ![RU](https://kvaytg.ru/common/flags/ru-21x16.svg) **Русский**

![Python 3.10](https://img.shields.io/badge/Python-3.10-blue?logo=python) ![PolyForm License](https://img.shields.io/badge/License-PolyForm-blue)

Утилиты для подготовки и очистки параллельных англо-русских корпусов.

## 📚 Использование
```python
from en_ru_corpus_utils import clean_corpus_from_unpaired_quotes_and_brackets, \
    save_distilled_labse, filter_by_labse, remove_matching_lines, merge_parallel_files, \
    remove_duplicates, filter_single_words, filter_corpus, generate_months_corpus

# 1. Базовая очистка
filter_corpus('data/corpus.txt', 'data/1.txt')

# 2. Дополнительная генерация корпуса
generate_months_corpus('data/months.txt')

# 3. Семантическая фильтрация (более высокий порог)
save_distilled_labse('data/labse_m2v_384')
filter_by_labse('data/labse_m2v_384', 'data/1.txt', 'data/2.txt', 0.7)

# 4. Структурная очистка
clean_corpus_from_unpaired_quotes_and_brackets('data/2.txt', 'data/3.txt')

# 5. Фильтрация тестового набора
remove_matching_lines('data/3.txt', 'data/FLORES200/flores_200.dev_test.txt', 'data/4.txt')

# 6. Объединение и удаление дубликатов
merge_parallel_files(['data/4.txt', 'data/months.txt', 'data/dictionary.txt'], 'data/5.txt')
remove_duplicates('data/5', 'data/6')

# 7. Финальная точная фильтрация
filter_single_words('data/6.txt', 'data/final.txt',
                    ['data/stop-words/ru-stop-words.txt',
                     'data/stop-words/en-stop-words.txt'])
```

## ⚙️ Установка
```bash
pip install git+https://github.com/KvaytG/en-ru-corpus-utils.git
```

## ⚠️ Важно
Этот проект **архивирован** и больше не поддерживается.

Новые функции и исправления ошибок не будут добавляться.

Используйте на свой страх и риск.

## 📜 Лицензия
Распространяется по лицензии **[PolyForm Noncommercial](LICENSE.md)**.

Проект использует компоненты с открытым исходным кодом. Сведения о лицензиях см. в **[pyproject.toml](pyproject.toml)** и на официальных ресурсах зависимостей.
