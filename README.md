# Facture_extractor
🧾 Automatic Information Extraction from PDF Invoices

This project demonstrates how to automatically extract key information from PDF invoices using a combination of OCR, Natural Language Processing (NLP), and regex-based heuristics. It supports both text-based and scanned PDFs.
🎯 Project Goals

Automatically extract the following fields from invoice documents:

    🆔 Invoice number

    📅 Invoice date

    🏢 Issuer name

    💰 Total amount (TTC)

Supports both:

    Text-based PDFs (native)

    Scanned PDFs (image-based with OCR)

🧰 Tech Stack
Component	Purpose
Tesseract OCR	Text recognition from scanned invoices
pdf2image	Converts PDF pages into images for OCR
spaCy	Named Entity Recognition (organization, date)
Regex	Pattern matching for invoice number, amount
Python	Core scripting language
Streamlit (optional)	Interactive UI for testing
🧪 Key Features

    🔍 Automatic OCR for image-based PDFs (fra language supported)

    ✂️ Named entity extraction using spaCy and regular expressions

    📊 Structured output (JSON or table)

    ✅ Evaluation on a small batch of synthetic invoice data

    📂 Easily extensible to other document types
