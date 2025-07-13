# dfflow

Lightweight pandas DataFrame logging and flow pipeline tracker.

---

## 📌 What is this?

**dfflow** is a simple, easy-to-use Python package for:
- Logging pandas DataFrame transformations step by step
- Saving logs in text or JSON format
- Building reusable pipeline-style data flows

---

## 📌 Features

✅ Automatic DataFrame transformation logging  
✅ Text and JSON log formats supported  
✅ Easy pipeline-style processing  
✅ Customizable logging  

---

## 📌 Installation

```bash
pip install dfflow
```

---

## 📌 Requirements

- Python >=3.7
- pandas >=1.3

To install requirements:

```bash
pip install -r requirements.txt
```

---

## 📌 Usage Example

```python
import pandas as pd
from dfflow import DFLogger, FlowPipeline, drop_nulls
import os
os.makedirs('examples', exist_ok=True)

logger = DFLogger()
pipe = FlowPipeline(logger=logger)

pipe.add_step("Drop Nulls", drop_nulls)

df = pd.DataFrame({
    'name': ['Suresh', None, 'Jerry', 'Sunil', 'Linga'],
    'age': [23, 26, None, 23, 24]
})

pipe.run(df)

```

---

## 📌 Project Structure

```
dfflow/              # Main package folder
│
├── __init__.py
├── logger.py        # Core logging class (DFLogger)
├── decorators.py    # log_step decorator
├── flow.py          # FlowPipeline logic
├── cleaning.py      # Cleaning steps (drop_nulls, lowercase_columns)
├── profile.py       # Profile utilities
├── utils.py         # Helper functions
│
examples/            # Usage demos
│   ├── dfflow_log.txt
│   └── flow_demo.py
│
tests/               # Unit tests
│   ├── __init__.py
│   ├── test_cleaning.py
│   ├── test_flow.py
│   ├── test_logger.py
│   └── test_profile.py
│
LICENSE              # MIT License
README.md            # Project description
requirements.txt     # Dependencies
setup.py             # Packaging configuration
```


---

## 📌 Author

Maintained by **Suresh K**  
📧 Email: sureshstr38@gmail.com  
🌐 GitHub: [suressssz](https://github.com/suressssz)

---

## 📌 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
