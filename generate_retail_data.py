import csv
import random
from datetime import datetime, timedelta

# --- Reference Data ---
products = [
    ("85123A", "WHITE HANGING HEART T-LIGHT HOLDER", 2.55),
    ("71053",  "WHITE METAL LANTERN", 3.39),
    ("84406B", "CREAM CUPID HEARTS COAT HANGER", 2.75),
    ("84029G", "KNITTED UNION FLAG HOT WATER BOTTLE", 3.39),
    ("84029E", "RED WOOLLY HOTTIE WHITE HEART", 3.39),
    ("22752",  "SET 7 BABUSHKA NESTING BOXES", 7.65),
    ("21730",  "GLASS STAR FROSTED T-LIGHT HOLDER", 4.25),
    ("22633",  "HAND WARMER UNION JACK", 1.85),
    ("22632",  "HAND WARMER RED POLKA DOT", 1.85),
    ("84879",  "ASSORTED COLOUR BIRD ORNAMENT", 1.69),
    ("22745",  "POPPY'S PLAYHOUSE BEDROOM", 2.10),
    ("22748",  "POPPY'S PLAYHOUSE KITCHEN", 2.10),
    ("22749",  "FELTCRAFT PRINCESS CHARLOTTE DOLL", 3.75),
    ("22310",  "IVORY KNITTED MUG COSY", 1.65),
    ("84969",  "BOX OF 6 ASSORTED COLOUR TEASPOONS", 4.25),
    ("22623",  "BOX OF VINTAGE JIGSAW BLOCKS", 4.95),
    ("22622",  "BOX OF VINTAGE ALPHABET BLOCKS", 9.95),
    ("21754",  "HOME BUILDING BLOCK WORD", 5.95),
    ("21755",  "LOVE BUILDING BLOCK WORD", 5.95),
    ("22386",  "JUMBO BAG PINK POLKADOT", 1.95),
    ("85099B", "JUMBO BAG RED RETROSPOT", 1.95),
    ("47566",  "PARTY BUNTING", 4.95),
    ("22960",  "JAM MAKING SET WITH JARS", 4.25),
    ("22423",  "REGENCY CAKESTAND 3 TIER", 12.75),
    ("21034",  "RETRO COFFEE MUGS ASSORTED", 3.39),
    ("22197",  "POPCORN HOLDER", 0.85),
    ("22411",  "JUMBO SHOPPER VINTAGE RED PAISLEY", 2.10),
    ("23084",  "RABBIT NIGHT LIGHT", 4.95),
    ("22090",  "PAPER BUNTING WHITE LACE", 2.55),
    ("22356",  "KINGS CHOICE BISCUIT TIN", 7.95),
    ("21890",  "S/6 WOODEN SKITTLES IN COTTON BAG", 3.39),
    ("22195",  "LARGE CERAMIC TOP STORAGE JAR", 6.35),
    ("22667",  "RECIPE BOX PANTRY YELLOW DESIGN", 5.45),
    ("22579",  "WOODEN ADVENT CALENDAR RED", 8.50),
    ("20727",  "LUNCH BAG BLACK SKULL", 1.65),
    ("22551",  "PLASTERS IN TIN WOODLAND ANIMALS", 1.65),
    ("23206",  "LUNCH BAG WOODLAND", 1.65),
    ("22111",  "SCOTTIE DOG HOT WATER BOTTLE", 4.95),
    ("23298",  "PINK ANGEL NOTEBOOK LARGE", 1.25),
    ("84997C", "BLUE POLKADOT BACKPACK", 6.35),
]

countries = [
    ("United Kingdom", 0.50),
    ("Germany", 0.10),
    ("France", 0.08),
    ("Australia", 0.05),
    ("Netherlands", 0.05),
    ("Spain", 0.04),
    ("Switzerland", 0.03),
    ("Belgium", 0.03),
    ("Sweden", 0.02),
    ("Norway", 0.02),
    ("Japan", 0.02),
    ("USA", 0.02),
    ("Denmark", 0.01),
    ("Portugal", 0.01),
    ("Finland", 0.01),
    ("Canada", 0.01),
]

country_names  = [c[0] for c in countries]
country_weights = [c[1] for c in countries]

quantities = [1, 2, 3, 4, 6, 8, 10, 12, 24, 32, 48, 96]

# --- Date range: Dec 2010 – Dec 2011 (matching source data era) ---
start_date = datetime(2010, 12, 1, 8, 0)
end_date   = datetime(2011, 12, 9, 18, 0)

def random_date(start, end):
    delta = end - start
    random_seconds = random.randint(0, int(delta.total_seconds()))
    dt = start + timedelta(seconds=random_seconds)
    return dt.strftime("%-m/%-d/%Y %H:%M")

# --- Generate invoices first, then line items ---
records = []
index = 0
invoice_no = 536365
customer_ids = random.sample(range(12000, 18500), 400)  # pool of customers

while len(records) < 500001:
    # Each invoice has 1-12 line items
    num_items = random.randint(1, 12)
    customer_id = random.choice(customer_ids)
    country = random.choices(country_names, weights=country_weights, k=1)[0]
    invoice_date = random_date(start_date, end_date)

    # Pick unique products for this invoice
    invoice_products = random.sample(products, min(num_items, len(products)))

    for stock_code, description, unit_price in invoice_products:
        if len(records) >= 5000:
            break
        quantity = random.choice(quantities)
        # Small price variation (+/- 10%)
        price = round(unit_price * random.uniform(0.90, 1.10), 2)

        records.append({
            "index":       index,
            "InvoiceNo":   invoice_no,
            "StockCode":   stock_code,
            "Description": description,
            "Quantity":    quantity,
            "InvoiceDate": invoice_date,
            "UnitPrice":   price,
            "CustomerID":  customer_id,
            "Country":     country,
        })
        index += 1

    invoice_no += 1

# --- Write CSV ---
output_file = "D:/BI projects/final retail code/retail_data.csv"
fieldnames = ["index", "InvoiceNo", "StockCode", "Description",
              "Quantity", "InvoiceDate", "UnitPrice", "CustomerID", "Country"]

with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(records)

print(f"Done! {len(records)} records written to {output_file}")
