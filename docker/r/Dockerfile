FROM r-base

WORKDIR /app

# העתקת הסקריפט פנימה
COPY analysis/plot_results.R /app/analysis/

# הרצת הסקריפט בעת הפעלת הקונטיינר
CMD ["Rscript", "/app/analysis/plot_results.R"]
