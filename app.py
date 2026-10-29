import io
import pandas as pd
import streamlit as st
from extractor import extract_text, parse_invoice

st.set_page_config(page_title="Invoice to Excel", page_icon="📄")
st.title("📄 Invoice PDF → Excel Extractor")
st.write("Upload invoice PDFs and download a clean Excel file. "
         "Works with text-based PDFs (not scanned images).")

files = st.file_uploader("Upload PDF invoices", type="pdf",
                         accept_multiple_files=True)

if files:
    rows = []
    for f in files:
        try:
            row = parse_invoice(extract_text(f))
        except Exception:
            row = {"status": "Needs review: could not read file"}
        row["file"] = f.name
        rows.append(row)

    df = pd.DataFrame(rows)
    st.success(f"Processed {len(df)} file(s)")
    st.dataframe(df, use_container_width=True)

    buffer = io.BytesIO()
    df.to_excel(buffer, index=False, engine="openpyxl")
    st.download_button(
        "⬇️ Download Excel",
        data=buffer.getvalue(),
        file_name="invoices.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )