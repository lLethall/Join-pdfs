import os
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_files, output_filename):
    merger = PdfMerger()
    for pdf_file in pdf_files:
        merger.append(pdf_file)
    merger.write(output_filename)
    merger.close()

def main():
    directory = "./pdfs"
    pdf_files = []

    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            pdf_files.append(os.path.join(directory, filename))

    pdf_files.sort()
    group_size = 200
    num_documents = len(pdf_files)
    num_groups = (num_documents + group_size - 1) // group_size
    for i in range(num_groups):
        start_index = i * group_size
        end_index = min((i + 1) * group_size, num_documents)
        output_filename = f"group_{i+1}.pdf"
        merge_pdfs(pdf_files[start_index:end_index], output_filename)

    print("Fusión de PDFs completada.")

if __name__ == "__main__":
    main()
