# Popular Movies Analysis

A menu-driven, command-line project that analyses the **10,000 most popular movies** from [TMDB](https://www.themoviedb.org/) using **Python, Pandas and Matplotlib**.

The dataset was fetched through the TMDB API and contains some null values (missing fields in the TMDB database), which makes it a good exercise in handling messy data.

## Features

The program is split into four parts, each navigated through menus:

| Part | What it does |
|------|--------------|
| **Reading** | Load and display the CSV dataset |
| **Analysis** | View rows/columns, add / delete records and columns, rating-wise and language-wise reports, statistical summary |
| **Visualization** | Language-wise movie counts as line, bar and horizontal bar graphs |
| **Export** | Save the data to a text / CSV file |

### Menu overview

```
MAIN MENU
1. Read CSV File
2. Data Analysis Menu
3. Graph Menu
4. Export Data
5. Exit
```

**Data Analysis Menu:** show whole DataFrame, columns, top/bottom rows, a specific column, add/delete record, add/delete column, rating-wise report (top 20), language-wise report (top 20), data summary.

## Requirements

- Python 3.8+
- pandas
- numpy
- matplotlib

Install dependencies:

```bash
pip install pandas numpy matplotlib
```

## Project Structure

```
.
├── Popular_movies.py     # main program
├── imbd_updated.csv      # dataset (must be in the same folder as the script)
└── README.md
```

## How to Run

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```
2. Make sure `imbd_updated.csv` is in the same folder as `Popular_movies.py`.
3. Run the program:
   ```bash
   python Popular_movies.py
   ```
4. Follow the on-screen menus.

## Dataset

- Source: [TMDB](https://www.themoviedb.org/) (The Movie Database), fetched via its read API.
- Columns used include `title`, `overview`, `language`, `vote_count` and `vote_average`.
- Data is attributed to TMDB as required by their API terms.

## Known Issues / Future Improvements

- **Export paths are hard-coded** to `C:/Users/hp/Project Export/`; change these to a path that exists on your machine.
- **Export menu:** the "Exit" option is shown as `4` but the code checks for `3`; the Excel option currently writes a `.csv` rather than a true `.xlsx` (use `df.to_excel()` with `openpyxl`).
- **Add a New Record** uses `DataFrame.append()`, which was removed in pandas 2.0. Use `pd.concat()` instead.
- **Update a Record** currently deletes the row instead of updating it.
- Changes made in the Data Analysis menu are held in memory only and are not saved back to the CSV.
- Input is not validated (e.g. non-numeric menu choices will raise an error).

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib

## Acknowledgements

Movie data provided by [TMDB](https://www.themoviedb.org/). This product uses the TMDB API but is not endorsed or certified by TMDB.

## License

Add your preferred license here (e.g. MIT).
