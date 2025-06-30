import os
import re
import pytesseract
import spacy
from pdf2image import convert_from_path
import json

nlp = spacy.load("fr_core_news_sm")

def ocr_from_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    text = "\n".join(pytesseract.image_to_string(img, lang="fra") for img in images)
    return text

def extract_entities(text):
    doc = nlp(text)
    dates = re.findall(r"\d{2}/\d{2}/\d{4}", text)
    montants = re.findall(r"\d+[.,]?\d*\s?(EUR|€)", text, re.IGNORECASE)
    num_facture = re.findall(r"FAC[- ]?\d+", text, re.IGNORECASE)
    noms = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
    return {
        "dates": dates,
        "montants": montants,
        "numero_facture": num_facture,
        "noms_entreprise": noms
    }

def traiter_factures(dossier):
    extractions = {}
    for fichier in os.listdir(dossier):
        if fichier.endswith(".pdf"):
            chemin = os.path.join(dossier, fichier)
            texte = ocr_from_pdf(chemin)
            infos = extract_entities(texte)
            extractions[fichier] = infos
    return extractions

if __name__ == "__main__":
    dossier_factures = "./factures_pdf"
    resultats = traiter_factures(dossier_factures)
    print(json.dumps(resultats, indent=2, ensure_ascii=False))
