# Running the Code

This guide explains how to prepare the dataset, execute the sentiment analysis script, and interpret the results.

---

## Step 1: Prepare the Dataset

1. **Create or Use an Existing Dataset**:
   - Ensure your dataset is a CSV file named `comments.csv`.
   - It should be stored in the `data/` folder of the repository.
   - The file should contain at least two columns:
     - `comment`: The YouTube comment text.
     - `sentiment`: The sentiment label (positive, negative, neutral).

2. **Dataset Format Example**:
   ```csv
   comment,sentiment
   "This video is amazing!",positive
   "I didn't like this video.",negative
   "It's okay, not great.",neutral
