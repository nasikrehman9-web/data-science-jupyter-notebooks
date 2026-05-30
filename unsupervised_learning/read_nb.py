
import os

file_path = r'd:\python_for_data_science\unsupervised_learning\05_pca.ipynb'
if os.path.exists(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            print("File content length:", len(content))
            print("First 2000 chars:")
            print(content[:2000])
    except Exception as e:
        print(f"Error reading file: {e}")
else:
    print(f"File not found: {file_path}")
