# 🔍 Demon Cry Python SDK

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)

Python SDK для [Demon Cry](https://github.com/Mooncore-inc/demon-cry) — автономного OSINT-агента, который использует LLM для проведения расследований в открытых источниках.

---

## ✨ Возможности

- 🔎 Автоматический сбор данных из открытых источников
- 🧠 Использование LLM для анализа и построения гипотез
- 🛠️ Динамический выбор инструментов для расследования
- 📊 Детальная статистика по использованным токенам и инструментам

---

## 📦 Установка

```bash
pip install git+https://github.com/Mooncore-inc/demon-cry-python-sdk.git
```

---

## 🚀 Быстрый старт

```python
import asyncio
from demon_cry_python_sdk import DemonCryClient


async def main():
    async with DemonCryClient("http://localhost:8000") as client:
        result = await client.investigate("цель")
        print(result.result)


asyncio.run(main())
```

---

## 📖 API Reference

### `DemonCryClient(base_url: str)`

Клиент для взаимодействия с Demon Cry API.

| Метод | Параметры | Возврат | Описание |
|-------|-----------|---------|----------|
| `investigate()` | `target: str`, `max_tokens: int = 15000` | `OSINTResponse` | Запуск расследования |
| `aclose()` | — | `None` | Закрытие соединения |

### `OSINTResponse`

| Поле | Тип | Описание |
|------|-----|----------|
| `status` | `str` | Статус расследования |
| `result` | `str \| None` | Результат расследования |
| `tools_used` | `list[dict]` | Использованные инструменты |
| `total_tokens` | `int` | Количество использованных токенов |

---

## 📄 Лицензия

[MIT](LICENSE) © [Mooncore Inc](https://github.com/Mooncore-inc)
