FROM python:3.9-slim

WORKDIR /app

# התקנת ספריית הגרפים
RUN pip install matplotlib

# העתקת הקוד והנתונים לתוך הקונטיינר
COPY analysis/ /app/analysis/
COPY data/ /app/data/

# פקודת ברירת המחדל שתרוץ כשהקונטיינר עולה
CMD ["python3", "analysis/analyze_fasta.py", "data/fasta/virus_hiv.fasta", "HIV_CONTAINER", "ATG"]
