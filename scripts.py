import os
import re
import socket
from collections import Counter

# Define file paths
input_files = ["/home/data/IF-1.txt", "/home/data/AlwaysRememberUsThisWay-1.txt"]
output_file = "/home/data/output/result.txt"

def count_words(text):
    words = re.findall(r"\b\w+(?:'\w+)?\b", text.lower())  # Handles contractions
    return len(words), Counter(words)

def get_top_words(counter, n=3):
    return counter.most_common(n)

def get_ip_address():
    return socket.gethostbyname(socket.gethostname())

results = []
total_words = 0

for file in input_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
        word_count, word_freq = count_words(content)
        total_words += word_count
        top_words = get_top_words(word_freq)

        results.append(f"File: {os.path.basename(file)} - Total Words: {word_count}")
        results.append(f"Top 3 words: {top_words}")

# Get machine IP
ip_address = get_ip_address()
results.append(f"Container IP Address: {ip_address}")

# Write results to output file
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(results))

# Print results to console
print("\n".join(results))
