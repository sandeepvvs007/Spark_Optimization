import tabula
import pandas as pd
from fpdf import FPDF
# Path to your PDF file
file_path = 'your_pdf_file.pdf'

# Read tables from PDF into a list of DataFrames
tables = tabula.read_pdf("/Users/sandeep/Downloads/hosp_list.pdf", pages='all', multiple_tables=True)
# print(tables)
combined_df = pd.concat(tables, ignore_index=True)

# Display the combined DataFrame
print(combined_df.columns)
filtered_df = combined_df[combined_df['CITY'].str.contains('visakhapatnam', case=False) | combined_df['ADDRESS'].str.contains('visakhapatnam', case=False)]
print(filtered_df)

filtered_df.to_csv("/Users/sandeep/Downloads/vizag_hosp_list.csv", index=False)
# Convert each table into a Pandas DataFrame or do further processing
# for idx, table in enumerate(tables):
#     df = pd.DataFrame(table)
#     # Process or work with each DataFrame as needed
#     print(f"Table {idx + 1}:")
#     print(df)
# def df_to_pdf(df, output_file):
#     pdf = FPDF()
#     pdf.set_auto_page_break(auto=True, margin=15)
#     pdf.add_page()

#     # Set font and size
#     pdf.set_font("Arial", size=12)

#     # Write DataFrame content to PDF
#     for _, row in df.iterrows():
#         for col in df.columns:
#             pdf.cell(50, 10, str(row[col]), ln=True)

#     # Save the PDF file
#     pdf.output(output_file)
# df_to_pdf(combined_df, "vizag_list")

