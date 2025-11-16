import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Set display options
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

print("="*80)
print("GOOGLE PLAY STORE APPS - EXPLORATORY DATA ANALYSIS")
print("="*80)

# Step 1: Load the dataset
print("\n1. LOADING DATASET...")
df = pd.read_csv('googleplaystore.csv')
print(f"Dataset loaded successfully!")
print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")

# Step 2: Basic Data Exploration
print("\n2. BASIC DATA EXPLORATION...")
print("\nFirst few rows:")
print(df.head())
print("\nDataset Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())
print("\nColumn Names:")
print(df.columns.tolist())

# Step 3: Remove problematic row (row 10472 as mentioned in PDF)
print("\n3. REMOVING PROBLEMATIC ROW...")
if len(df) > 10472:
    df.drop(10472, axis=0, inplace=True)
    print("Row 10472 removed")
print(f"Shape after removal: {df.shape}")

# Step 4: Data Cleaning - Convert Reviews to int
print("\n4. CLEANING DATA...")
print("4.1 Converting Reviews to int...")
df['Reviews'] = df['Reviews'].astype(int)
print("Reviews converted to int")

# Step 5: Convert Size to bytes
print("\n4.2 Converting Size to bytes...")
def convert_to_bytes(size_str):
    if isinstance(size_str, str):
        if 'k' in size_str.lower():
            return float(size_str.replace('k', '').replace('K', '')) * 1024
        elif 'M' in size_str:
            return float(size_str.replace('M', '')) * 1024 * 1024
        elif 'Varies with device' in size_str:
            return np.nan
    return size_str

df['Size_in_bytes'] = df['Size'].apply(convert_to_bytes)
df['Size_MB'] = df['Size_in_bytes'] / (1024 * 1024)
print("Size converted to bytes and MB")

# Step 6: Convert Installs to int
print("\n4.3 Converting Installs to int...")
def clean_installs(install_str):
    if isinstance(install_str, str):
        # Remove + and commas
        install_str = install_str.replace('+', '').replace(',', '')
        return int(install_str)
    return install_str

df['Installs'] = df['Installs'].apply(clean_installs)
print("Installs converted to int")

# Step 7: Create Installs_category
print("\n4.4 Creating Installs_category...")
bins = [-1, 0, 10, 1000, 10000, 100000, 1000000, 10000000, 10000000000]
labels = ['no', 'Very low', 'Low', 'Moderate', 'More than moderate', 'High', 'Very High', 'Top Notch']
df['Installs_category'] = pd.cut(df['Installs'], bins=bins, labels=labels)
print("Installs_category created")

# Step 8: Convert Price to float
print("\n4.5 Converting Price to float...")
def clean_price(price_str):
    if isinstance(price_str, str):
        return float(price_str.replace('$', ''))
    return price_str

df['Price'] = df['Price'].apply(clean_price)
print("Price converted to float")

# Step 9: Handle missing values
print("\n4.6 Handling missing values...")
print("Missing values before cleaning:")
print(df.isnull().sum().sort_values(ascending=False))

# Remove rows with missing values in critical columns
df.dropna(subset=['Current Ver', 'Android Ver', 'Category', 'Type', 'Genres'], inplace=True)
print(f"Shape after removing critical missing values: {df.shape}")

# Fill missing ratings based on Installs_category
print("\n4.7 Filling missing ratings based on Installs_category...")
rating_by_category = df.groupby('Installs_category')['Rating'].mean()

def fill_missing_ratings(row):
    if pd.isna(row['Rating']):
        category = row['Installs_category']
        if pd.notna(category) and category in rating_by_category.index:
            return rating_by_category[category]
        # If category is also missing, use overall mean
        return df['Rating'].mean()
    return row['Rating']

df['Rating'] = df.apply(fill_missing_ratings, axis=1)
# Fill any remaining NaN values with overall mean
df['Rating'].fillna(df['Rating'].mean(), inplace=True)
print("Missing ratings filled")
print(f"Missing values after filling: {df['Rating'].isnull().sum()}")

# Step 10: Remove duplicates
print("\n4.8 Removing duplicates...")
duplicates_count = df.duplicated().sum()
print(f"Number of duplicates found: {duplicates_count}")
df.drop_duplicates(inplace=True)
print(f"Shape after removing duplicates: {df.shape}")

# Step 11: Final dataset info
print("\n5. FINAL DATASET INFO...")
print(f"Final shape: {df.shape}")
print("\nMissing values:")
print(df.isnull().sum().sort_values(ascending=False))
print("\nData types:")
print(df.dtypes)

# Step 12: Data Analysis
print("\n6. DATA ANALYSIS...")

# 6.1 Category with highest number of apps
print("\n6.1 Top 10 Categories by Number of Apps:")
top_categories = df['Category'].value_counts().head(10)
print(top_categories)

# 6.2 Category with highest installs
print("\n6.2 Top 10 Categories by Total Installs:")
top_installs = df.groupby('Category')['Installs'].sum().sort_values(ascending=False).head(10)
print(top_installs)

# 6.3 Category with highest reviews
print("\n6.3 Top 10 Categories by Total Reviews:")
top_reviews = df.groupby('Category')['Reviews'].sum().sort_values(ascending=False).head(10)
print(top_reviews)

# 6.4 Category with highest rating
print("\n6.4 Top 10 Categories by Average Rating:")
top_ratings = df.groupby('Category')['Rating'].mean().sort_values(ascending=False).head(10)
print(top_ratings)

# Step 13: Visualizations
print("\n7. CREATING VISUALIZATIONS...")

# 7.1 Distribution of Ratings
plt.figure(figsize=(10, 6))
sns.histplot(df['Rating'], bins=20, kde=True)
plt.title('Distribution of App Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('rating_distribution.png', dpi=300, bbox_inches='tight')
print("Saved: rating_distribution.png")
plt.close()

# 7.2 Count of Apps by Category
plt.figure(figsize=(12, 8))
category_counts = df['Category'].value_counts().head(15)
sns.barplot(y=category_counts.index, x=category_counts.values)
plt.title('Top 15 Categories by Number of Apps')
plt.xlabel('Number of Apps')
plt.ylabel('Category')
plt.tight_layout()
plt.savefig('category_count.png', dpi=300, bbox_inches='tight')
print("Saved: category_count.png")
plt.close()

# 7.3 Top Categories by Installs
plt.figure(figsize=(12, 8))
top_installs_plot = df.groupby('Category')['Installs'].sum().sort_values(ascending=False).head(15)
sns.barplot(y=top_installs_plot.index, x=top_installs_plot.values)
plt.title('Top 15 Categories by Total Installs')
plt.xlabel('Total Installs')
plt.ylabel('Category')
plt.tight_layout()
plt.savefig('category_installs.png', dpi=300, bbox_inches='tight')
print("Saved: category_installs.png")
plt.close()

# 7.4 Top Categories by Reviews
plt.figure(figsize=(12, 8))
top_reviews_plot = df.groupby('Category')['Reviews'].sum().sort_values(ascending=False).head(15)
sns.barplot(y=top_reviews_plot.index, x=top_reviews_plot.values)
plt.title('Top 15 Categories by Total Reviews')
plt.xlabel('Total Reviews')
plt.ylabel('Category')
plt.tight_layout()
plt.savefig('category_reviews.png', dpi=300, bbox_inches='tight')
print("Saved: category_reviews.png")
plt.close()

# 7.5 Top Categories by Average Rating
plt.figure(figsize=(12, 8))
top_ratings_plot = df.groupby('Category')['Rating'].mean().sort_values(ascending=False).head(15)
sns.barplot(y=top_ratings_plot.index, x=top_ratings_plot.values)
plt.title('Top 15 Categories by Average Rating')
plt.xlabel('Average Rating')
plt.ylabel('Category')
plt.tight_layout()
plt.savefig('category_ratings.png', dpi=300, bbox_inches='tight')
print("Saved: category_ratings.png")
plt.close()

# 7.6 Correlation Heatmap
plt.figure(figsize=(10, 8))
numeric_cols = ['Rating', 'Reviews', 'Size_in_bytes', 'Installs', 'Price', 'Size_MB']
corr = df[numeric_cols].corr()
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', center=0, square=True)
plt.title('Correlation Matrix of Numeric Variables')
plt.tight_layout()
plt.savefig('correlation_heatmap.png', dpi=300, bbox_inches='tight')
print("Saved: correlation_heatmap.png")
plt.close()

# 7.7 Boxplot of Ratings by Installs Category
plt.figure(figsize=(14, 8))
# Order categories properly
category_order = ['no', 'Very low', 'Low', 'Moderate', 'More than moderate', 'High', 'Very High', 'Top Notch']
df_plot = df[df['Installs_category'].isin(category_order)].copy()
df_plot['Installs_category'] = pd.Categorical(df_plot['Installs_category'], categories=category_order, ordered=True)

sns.boxplot(x='Installs_category', y='Rating', data=df_plot, palette='viridis')
# Add mean line
means = df_plot.groupby('Installs_category')['Rating'].mean()
for i, (cat, mean_val) in enumerate(means.items()):
    plt.plot([i-0.4, i+0.4], [mean_val, mean_val], 'r--', linewidth=2, alpha=0.7, label='Mean' if i == 0 else '')

plt.title('Distribution of Ratings by Installs Category', fontsize=14, fontweight='bold')
plt.xlabel('Installs Category', fontsize=12)
plt.ylabel('Rating', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.ylim(0, 5.5)
plt.grid(axis='y', alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig('rating_by_installs_category.png', dpi=300, bbox_inches='tight')
print("Saved: rating_by_installs_category.png")
plt.close()

# 7.8 Scatter plot: Reviews vs Installs (log scale) with regression line
plt.figure(figsize=(12, 8))
df_clean = df.dropna(subset=['Reviews', 'Installs'])
df_clean = df_clean[(df_clean['Reviews'] > 0) & (df_clean['Installs'] > 0)]

# Use log scale
x_log = np.log10(df_clean['Reviews'] + 1)
y_log = np.log10(df_clean['Installs'] + 1)

# Create scatter plot with density coloring
plt.scatter(x_log, y_log, alpha=0.3, s=10, c='steelblue', edgecolors='none')

# Add regression line
slope, intercept, r_value, p_value, std_err = stats.linregress(x_log, y_log)
line_x = np.array([x_log.min(), x_log.max()])
line_y = slope * line_x + intercept
plt.plot(line_x, line_y, 'r-', linewidth=2, label=f'Regression Line (R²={r_value**2:.3f})')

# Add text annotation for correlation
plt.text(0.05, 0.95, f'Correlation: {r_value:.3f}\nR²: {r_value**2:.3f}', 
         transform=plt.gca().transAxes, fontsize=11,
         verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.title('Relationship between Reviews and Installs (Log Scale)', fontsize=14, fontweight='bold')
plt.xlabel('Log10(Reviews + 1)', fontsize=12)
plt.ylabel('Log10(Installs + 1)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=10)
plt.tight_layout()
plt.savefig('reviews_vs_installs.png', dpi=300, bbox_inches='tight')
print("Saved: reviews_vs_installs.png")
plt.close()

# Step 14: Save cleaned dataset
print("\n8. SAVING CLEANED DATASET...")
# Remove helper columns that were created during analysis
columns_to_save = ['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 
                   'Type', 'Price', 'Content Rating', 'Genres', 'Last Updated', 
                   'Current Ver', 'Android Ver', 'Size_MB', 'Installs_category']
df_clean_final = df[columns_to_save].copy()
df_clean_final.to_csv('googleplaystore_cleaned.csv', index=False)
print("Saved: googleplaystore_cleaned.csv")
print(f"Final cleaned dataset shape: {df_clean_final.shape}")

print("\n" + "="*80)
print("ANALYSIS COMPLETE!")
print("="*80)
print("\nSummary:")
print(f"- Total apps analyzed: {len(df_clean_final)}")
print(f"- Categories: {df_clean_final['Category'].nunique()}")
print(f"- Average rating: {df_clean_final['Rating'].mean():.2f}")
print(f"- Total installs: {df_clean_final['Installs'].sum():,}")
print(f"- Total reviews: {df_clean_final['Reviews'].sum():,}")
print("\nFiles created:")
print("- googleplaystore_cleaned.csv (cleaned dataset)")
print("- rating_distribution.png")
print("- category_count.png")
print("- category_installs.png")
print("- category_reviews.png")
print("- category_ratings.png")
print("- correlation_heatmap.png")
print("- rating_by_installs_category.png")
print("- reviews_vs_installs.png")

