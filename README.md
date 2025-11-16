# 📱 Google Play Store Apps - Exploratory Data Analysis

<div align="center">

**A comprehensive data analysis project exploring Google Play Store apps dataset**

[📊 Dataset](#-dataset) • [🚀 Features](#-features) • [📦 Installation](#-installation) • [💻 Usage](#-usage) • [📈 Results](#-results) • [📁 Project Structure](#-project-structure)

</div>

---

## 📋 Table of Contents

- [About the Project](#-about-the-project)
- [Dataset](#-dataset)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Data Cleaning Process](#-data-cleaning-process)
- [Results](#-results)
- [Visualizations](#-visualizations)
- [Technologies Used](#-technologies-used)
- [Key Insights](#-key-insights)

---

## 🎯 About the Project

This project performs a comprehensive **Exploratory Data Analysis (EDA)** on the Google Play Store Apps dataset. The analysis includes data cleaning, transformation, statistical analysis, and visualization to uncover insights about app performance, categories, ratings, and user engagement.

### 🎨 What You'll Find:

- ✅ Complete data cleaning pipeline
- 📊 8+ interactive visualizations
- 🔍 Statistical analysis and insights
- 📈 Category-wise performance analysis
- 🧹 Cleaned dataset ready for further analysis

---

## 📊 Dataset

The dataset contains information about **10,841 Google Play Store apps** with the following attributes:

| Column | Description |
|--------|-------------|
| **App** | Application name |
| **Category** | Category the app belongs to |
| **Rating** | Overall user rating (1-5) |
| **Reviews** | Number of user reviews |
| **Size** | Size of the app |
| **Installs** | Number of app installations |
| **Type** | Free or Paid |
| **Price** | Price of the app |
| **Content Rating** | Target audience rating |
| **Genres** | App genre(s) |
| **Last Updated** | Date of last update |
| **Current Ver** | Current version |
| **Android Ver** | Minimum Android version required |

### 📥 Dataset Files:

- `googleplaystore.csv` - Original dataset
- `googleplaystore_user_reviews.csv` - User reviews dataset
- `googleplaystore_cleaned.csv` - **Cleaned and processed dataset** ✨

---

## 🚀 Features

### 🔧 Data Cleaning
- ✅ Removed problematic rows
- ✅ Handled missing values intelligently
- ✅ Converted data types (Reviews, Installs, Size, Price)
- ✅ Removed duplicates (483 duplicates removed)
- ✅ Created derived features (Size_MB, Installs_category)

### 📊 Analysis Performed
- 📈 Category-wise app distribution
- 📊 Top categories by installs, reviews, and ratings
- 🔍 Correlation analysis between variables
- 📉 Distribution analysis of ratings
- 📱 Performance metrics by install category

### 🎨 Visualizations Created
1. **Rating Distribution** - Histogram showing app rating distribution
2. **Category Count** - Top 15 categories by number of apps
3. **Category Installs** - Top 15 categories by total installs
4. **Category Reviews** - Top 15 categories by total reviews
5. **Category Ratings** - Top 15 categories by average rating
6. **Correlation Heatmap** - Relationships between numeric variables
7. **Rating by Installs Category** - Boxplot showing rating distribution
8. **Reviews vs Installs** - Scatter plot with regression line

---

## 📦 Installation

### Prerequisites

Make sure you have Python 3.7+ installed on your system.

### Step 1: Clone the Repository

```bash
git clone <your-repo-url>
cd Project-6
```

### Step 2: Install Required Packages

```bash
pip install pandas numpy matplotlib seaborn scipy
```

Or use the requirements file:

```bash
pip install -r requirements.txt
```

### Step 3: Place Dataset Files

Ensure the following files are in the project directory:
- `googleplaystore.csv`
- `googleplaystore_user_reviews.csv` (optional)

---

## 💻 Usage

### Running the Analysis

Simply execute the main analysis script:

```bash
python google_play_store_analysis.py
```

### What the Script Does:

1. **📥 Loads** the dataset
2. **🔍 Explores** basic statistics and structure
3. **🧹 Cleans** the data (missing values, duplicates, type conversion)
4. **📊 Analyzes** category-wise metrics
5. **📈 Creates** visualizations
6. **💾 Saves** cleaned dataset

### Output Files Generated:

```
📁 Project Directory
├── 📊 googleplaystore_cleaned.csv          # Cleaned dataset
├── 📈 rating_distribution.png             # Rating histogram
├── 📊 category_count.png                  # Category bar chart
├── 📈 category_installs.png               # Installs by category
├── 📊 category_reviews.png                # Reviews by category
├── 📈 category_ratings.png                # Ratings by category
├── 🔥 correlation_heatmap.png            # Correlation matrix
├── 📦 rating_by_installs_category.png     # Boxplot
└── 📈 reviews_vs_installs.png            # Scatter plot
```

---

## 🧹 Data Cleaning Process

### Steps Performed:

1. **🗑️ Removed Problematic Row**
   - Removed row 10472 (causing data issues)

2. **🔄 Data Type Conversion**
   - `Reviews`: String → Integer
   - `Installs`: String (with +, commas) → Integer
   - `Size`: String (M/k/Varies) → Bytes & MB
   - `Price`: String ($) → Float

3. **📊 Feature Engineering**
   - Created `Size_MB` column
   - Created `Installs_category` (8 categories)

4. **🔍 Missing Value Handling**
   - Removed rows with missing critical columns
   - Filled missing ratings based on installs category
   - Size missing values kept (for "Varies with device")

5. **🔁 Duplicate Removal**
   - Removed 483 duplicate rows

### Final Dataset Stats:

- **Rows**: 10,346 (cleaned)
- **Columns**: 15
- **Missing Values**: Only in Size_MB (expected)
- **Duplicates**: 0

---

## 📈 Results

### Top Categories by Number of Apps:

| Rank | Category | Count |
|------|----------|-------|
| 🥇 | FAMILY | 1,939 |
| 🥈 | GAME | 1,121 |
| 🥉 | TOOLS | 841 |

### Top Categories by Total Installs:

| Rank | Category | Installs |
|------|----------|----------|
| 🥇 | GAME | 31.5 Billion |
| 🥈 | COMMUNICATION | 24.2 Billion |
| 🥉 | SOCIAL | 12.5 Billion |

### Top Categories by Average Rating:

| Rank | Category | Rating |
|------|----------|--------|
| 🥇 | EVENTS | 4.39 |
| 🥈 | EDUCATION | 4.37 |
| 🥉 | ART_AND_DESIGN | 4.37 |

### Key Statistics:

- 📱 **Total Apps Analyzed**: 10,346
- 📂 **Categories**: 33
- ⭐ **Average Rating**: 4.20
- 📥 **Total Installs**: 146.6 Billion
- 💬 **Total Reviews**: 4.2 Billion

---

## 🎨 Visualizations

<details>
<summary>📈 Click to see visualization descriptions</summary>

#### 1. Rating Distribution
- Shows the distribution of app ratings
- Most apps have ratings between 4.0-4.5

#### 2. Category Analysis
- Bar charts showing top categories by various metrics
- Helps identify popular and high-performing categories

#### 3. Correlation Heatmap
- Shows relationships between numeric variables
- Reviews and Installs have strong positive correlation (0.64)

#### 4. Rating by Installs Category
- Boxplot showing rating distribution across install categories
- Higher install categories tend to have better ratings

#### 5. Reviews vs Installs
- Scatter plot with regression line
- Strong positive correlation between reviews and installs

</details>

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| 🐍 **Python 3.7+** | Programming language |
| 📊 **Pandas** | Data manipulation and analysis |
| 🔢 **NumPy** | Numerical computations |
| 📈 **Matplotlib** | Basic plotting and visualization |
| 🎨 **Seaborn** | Statistical data visualization |
| 📐 **SciPy** | Statistical functions |

---

## 🔍 Key Insights

### 💡 Discoveries:

1. **🎮 Gaming Dominance**
   - Games have the highest number of installs (31.5B)
   - Also lead in total reviews (1.4B)

2. **⭐ Rating Patterns**
   - Average app rating is 4.20 (quite high!)
   - Higher install categories correlate with better ratings

3. **📱 Category Distribution**
   - FAMILY apps are most numerous (1,939 apps)
   - GAME category is second (1,121 apps)

4. **🔗 Strong Correlations**
   - Reviews and Installs show strong positive correlation (R² = 0.39)
   - More installs generally mean more reviews

5. **💰 Pricing**
   - Vast majority of apps are free
   - Paid apps are a small fraction of the market

---

## 📝 Notes

- The cleaned dataset (`googleplaystore_cleaned.csv`) is ready for further analysis or machine learning
- All visualizations are saved as high-resolution PNG files (300 DPI)
- The analysis follows best practices for EDA and data cleaning
---