import requests
from bs4 import BeautifulSoup
import pandas as pd


GRIDS = [
    2096,2097,2098,2116,2117,2118,2119,2120,2121,2122,2123,
    2138,2139,2140,2141,2142,2143,2144,2145,2146,
    2170,2171,2172,2173,2174,2175,2176,2177,2178,
    2211,2212,2213,2214,2215,2216,2217,2218,2219,
    2248,2249,2250,2251
]

BULAN = ["Jan","Feb","Mar","Apr","Mei","Jun","Jul",
         "Agu","Sep","Okt","Nov","Des","Tahunan"]


def scrape_grid(grid_id: int) -> dict | None:
    """Scrape data rata-rata curah hujan dari 1 grid."""
    url = f"https://hidrologi.net/hujanbulanantrmm/{grid_id}"
    try:
        resp = requests.get(url, timeout=15)
        resp.raise_for_status()
    except Exception as e:
        print(f"Gagal akses TRMM-{grid_id}: {e}")
        return None

    soup = BeautifulSoup(resp.text, "html.parser")
    rows = soup.find_all("tr")

    for row in rows:
        cells = [c.get_text(strip=True) for c in row.find_all("td")]
        if cells and cells[0].startswith("Rata-rata"):
            if len(cells[1:]) >= 13:
                return {"Grid": f"TRMM-{grid_id}", **dict(zip(BULAN, cells[1:]))}

    print(f"Tidak menemukan data rata-rata untuk TRMM-{grid_id}")
    return None


def main():
    data_all = []
    for grid in GRIDS:
        result = scrape_grid(grid)
        if result:
            data_all.append(result)

    df = pd.DataFrame(data_all)
    filename = "data/curah_hujan_rata2.csv"
    df.to_csv(filename, index=False)
    print(f"Hasil scraping disimpan di {filename}")
    print(df.head())


if __name__ == "__main__":
    main()
