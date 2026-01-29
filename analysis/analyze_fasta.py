import sys
import os
import csv
import matplotlib.pyplot as plt

def main():
    if len(sys.argv) < 3:
        print("Usage: python analyze_fasta.py <fasta_file> <output_name> <motif>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    name = sys.argv[2]
    motif = sys.argv[3]
    
    print(f"Analyzing {name} for motif {motif}...")

    if not os.path.exists("output"):
        os.makedirs("output")

    count = 0
    sequence = ""
    
    try:
        with open(fasta_file, 'r') as f:
            for line in f:
                if not line.startswith(">"):
                    sequence += line.strip()
    except FileNotFoundError:
        print(f"Error: File {fasta_file} not found.")
        sys.exit(1)
    
    count = sequence.count(motif)
    
    # Save CSV
    csv_path = "output/motif_counts_local.csv"
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Sequence", "Motif", "Count"])
        writer.writerow([name, motif, count])
        
    print(f"Results saved to {csv_path}")

    # Create Plot
    plt.figure(figsize=(8, 6))
    plt.bar([name], [count], color='blue')
    plt.title(f"Motif Count: {motif}")
    plt.ylabel("Count")
    plt.savefig("output/python_motif_hist_local.png")
    print("Plot saved to output/python_motif_hist_local.png")

if __name__ == "__main__":
    main()
