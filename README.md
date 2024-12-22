# Concept Level Sentiment Analysis of Bengali Text

## Overview
This project explores the concept-level sentiment analysis of Bengali text, focusing on restaurant reviews, comments, and blogs. Unlike traditional feature-based sentiment analysis, this research introduces a concept-level approach using custom-built dictionaries to identify and classify sentiments more accurately.

![Concept Level Sentiment Analysis](https://github.com/snsamia/Concept_Level_Sentiment_Analysis/blob/main/image.jpg)

---

## Key Features
- **Data Collection**: 
  - Collected 2,700 Bengali text reviews, comments, and blogs from Facebook.
  - Labeled data manually into positive, negative, and neutral sentiment categories.

- **Preprocessing Workflow**:
  - **Punctuation Removal**: Removed unnecessary symbols and spaces.
  - **Tokenization & Detokenization**: Processed text using `nltk` for splitting and rejoining meaningful words.
  - **Stopword Removal**: Eliminated uninformative words like "অথচ," "অথবা," and "এটি."
  - **Concept Construction**: Built custom dictionaries for nouns, adjectives, verbs, and adverbs to extract sentiment-bearing concepts.

- **Machine Learning Models**:
  - Evaluated algorithms: Naïve Bayes, Support Vector Machine (SVM), Random Forest, Decision Tree, and K-Nearest Neighbor.
  - Compared model performance on feature-based and concept-level datasets.

---

## Methodology
1. **Concept Extraction**:
   - Created self-made dictionaries to identify sentiment-rich concepts.
   - Mapped these concepts to **BanglaSenticNet** for sentiment matching.

2. **Data Processing**:
   - Cleaned data and transformed text into concepts using custom algorithms.
   - Generated two datasets: one for feature-based analysis and another for concept-level analysis.

3. **Evaluation Metrics**:
   - Used metrics such as accuracy, precision, recall, and F1-score for model performance evaluation.
   - Confusion matrix to analyze predictions.

---

## Results
1. **Feature-Based Approach**:
   - SVM achieved the highest accuracy: **84%**.
   - Other models' accuracy: Random Forest (**73%**), Decision Tree (**72%**), Naïve Bayes (**66%**).

2. **Concept-Level Approach**:
   - SVM achieved the highest accuracy: **96%**.
   - Other models' accuracy: Random Forest (**75%**), Decision Tree (**71%**), Naïve Bayes (**68%**), K-Nearest Neighbor (**68%**).

3. **Performance Comparison**:
   - The concept-level approach outperformed feature-based models across all metrics, showcasing its efficacy in sentiment analysis for Bengali text.

---

## Conclusion
- The proposed concept-level approach improves sentiment detection by incorporating domain-specific knowledge from dictionaries.
- SVM consistently outperformed other models, validating its robustness in both feature-based and concept-level approaches.
- The research highlights the challenges of extracting meaningful concepts from Bengali text and the effectiveness of custom-built dictionaries.

---

## Future Directions
1. **Advanced Concept Extraction**:
   - Implement dependency-based semantic parsing for improved results.
2. **Expanding Sentiment Labels**:
   - Move beyond positive, negative, and neutral to include emotions like joy, anger, and sadness.
3. **Larger Datasets**:
   - Work with a more extensive and diverse dataset to generalize findings.
4. **Multi-language Support**:
   - Apply the methodology to other languages using R or Python.

---

## References
Key references include:
- BanglaSenticNet for concept matching.
- SentiWordNet for sentiment classification.
- Various research papers on multilingual sentiment analysis and dependency parsing.

For more details, please refer to the research paper attached in this repository.
