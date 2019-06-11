# Ngontrak.com Word Sense Disambiguator
Yudhistira Erlandinata, et. al

## Setup
- Download dataset from drive https://drive.google.com/drive/folders/1t-2ZHbGocvGdzGK_SqW5o4IGgDkxbt7U?usp=sharing
- Install requirements from requirements.txt

## Progress so far
### Preprocessing
- Lowercasing
- Punctuation removal
- Repeated-words removal
- Stemming
- Numbers normalization
- Money normalization
- Passive/active voice verbs normalization
- Too common part of speech normalization
- Rare sense removal
- POS tagging

### Feature Extraction
- Bag of Words
- TF-IDF
- Unigram-Bigram TF-IDF
- Latent Semantic Analysis
- Collocation Vectors
- Binary bag of words
- Singular Value Decomposition

### Machine Learning Algorithm
- Linear SVM: always fastest and most accurate

### Model Selection
- K-Fold Cross Validation
- Hyperparameter Tuning

### Evaluation Metrics
- Macro Average Accuracy
- Macro Average F1-Score

### Best Approach
Iacobacci, et. al (2010) replication: It makes sense + word embedding wikipedia

# References
All papers here:
- https://drive.google.com/drive/folders/1t-2ZHbGocvGdzGK_SqW5o4IGgDkxbt7U?usp=sharing
