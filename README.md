# Ngontrak.com Word Sense Disambiguator
Yudhistira Erlandinata, et. al

## Setup
- Download dataset from drive https://drive.google.com/drive/folders/1t-2ZHbGocvGdzGK_SqW5o4IGgDkxbt7U?usp=sharing
- Install requirements from requirements.txt
```
pip install -r requirements.txt
```
## How to use
- Put all required dataset in parent directory
- Execute data preprocessing using Supervised WSD Preprocessing.ipynb and SUpervised NER Preprocessing.ipynb
- Get MWE corpus from MWE.ipynb, make sure to output mwe.json
- Use Hybrid WSD.ipynb to train both Supervised WSD and Supervised NER
- Also, use Hybrid WSD.ipynb to label new untagged dataset (e.g. test dataset)
- Use Evaluation Metrics.ipynb to measure the performance

# References
All papers here:
- https://drive.google.com/drive/folders/1t-2ZHbGocvGdzGK_SqW5o4IGgDkxbt7U?usp=sharing
