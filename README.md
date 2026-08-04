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
pip install demon-cry-python-sdk
```

---

## 🚀 Быстрый старт

```python
import asyncio
from demon_cry_python_sdk import DemonCryClient


async def main():
    async with DemonCryClient(base_url="http://localhost:8000") as client:
        result = await client.investigations.create(target="fazzyt")
        print(result.result)


asyncio.run(main())
```

---

## 💰 Расчёт стоимости запроса

Тарифы взяты из [документации DeepSeek](https://api-docs.deepseek.com/quick_start/pricing/).

```python
result = await client.investigations.create(target="example.com")

tokens = result.tokens

# Тарифы DeepSeek (за 1 токен)
INPUT_COST_PER_TOKEN = 0.14 / 1_000_000       # cache miss
INPUT_CACHED_COST = 0.0028 / 1_000_000        # cache hit
OUTPUT_COST_PER_TOKEN = 0.28 / 1_000_000

input_cost = tokens.cache_hit * INPUT_CACHED_COST + tokens.cache_miss * INPUT_COST_PER_TOKEN
output_cost = tokens.completion * OUTPUT_COST_PER_TOKEN
total_cost = input_cost + output_cost

print(f"Всего токенов: {tokens.total}")
print(f"  Prompt:      {tokens.prompt}")
print(f"  Completion:  {tokens.completion}")
print(f"  Cache hit:   {tokens.cache_hit}")
print(f"  Cache miss:  {tokens.cache_miss}")
print(f"Стоимость:     ${total_cost:.6f}")
```

---

## 📄 Лицензия

[MIT](LICENSE) © [Mooncore Inc](https://github.com/Mooncore-inc)
