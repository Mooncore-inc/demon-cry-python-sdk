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
    async with DemonCryClient(base_url="http://localhost:8000") as client:
        result = await client.investigations.create(target="fazzyt")
        print(result.result)


asyncio.run(main())
```


## 📄 Лицензия

[MIT](LICENSE) © [Mooncore Inc](https://github.com/Mooncore-inc)
