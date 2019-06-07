# Ngontrak.com Word Sense Disambiguator
Yudhistira Erlandinata, et. al

## Setup
- Download dataset from SCeLE
- Install requirements from requirements.txt
- Run Preprocessing.ipynb
- Train with WSD.ipynb

## Progress so far
### Preprocessing
- Lowercasing
- Punctuation removal
- Repeated-words removal
- Stemming
- Numbers normalization
- Money normalization
- Rare sense removal

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
It Makes Sense's local collocations SVD + Surrounding words SVD features with Linear SVM classifier, macro avg. accuarcy: .74, macro avg. f1-score: .533, cross-validated.
