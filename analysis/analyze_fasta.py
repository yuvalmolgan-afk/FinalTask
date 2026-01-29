import sys
import os
import csv
import matplotlib.pyplot as plt

def main():
    if len(sys.argv) < 3:
        print("Usage: python analyze_fasta.py <fasta_file> <unused_name> <motif>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    motif = sys.argv[3] # We skip argv[2] (the name) because we read names from file
    
    print(f"Analyzing {fasta_file} for motif {motif}...")

    if not os.path.exists("output"):
        os.makedirs("output")

    # Dictionary to store counts per virus
    results = {}
    current_header = None
    current_sequence = []

    # Manual FASTA parsing
    with open(fasta_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            
            if line.startswith(">"):
                # Save previous if exists
                if current_header:
                    full_seq = "".join(current_sequence)
                    results[current_header] = full_seq.count(motif)
                
                # Start new
                current_header = line[1:] # Remove >
                current_sequence = []
            else:
                current_sequence.append(line)
        
        # Don't forget the last one
        if current_header:
            full_seq = "".join(current_sequence)
            results[current_header] = full_seq.count(motif)

    # Save CSV
    csv_path = "output/motif_counts_local.csv"
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Sequence", "Motif", "Count"])
        for name, count in results.items():
            writer.writerow([name, motif, count])
        
    print(f"Results saved to {csv_path}")

    # Create Plot
    names = list(results.keys())
    counts = list(results.values())

    plt.figure(figsize=(10, 6)) # A bit wider
    plt.bar(names, counts, color='blue')
    plt.title(f"Motif Count: {motif} (Comparison)")
    plt.ylabel("Count")
    plt.xticks(rotation=45) # Rotate names so they don't overlap
    plt.tight_layout()
    plt.savefig("output/python_motif_hist_local.png")
    print("Plot saved.")

if __name__ == "__main__":
    main()