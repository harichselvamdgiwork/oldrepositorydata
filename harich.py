# %%time
# from pdf2image import convert_from_path
# import os

# # Path to the folder containing PDF files
# pdf_folder = "dataset"

# # Output folder to save images
# output_parent_folder = "data"

# # Path to the Poppler executable
# poppler_path = r"C:/poppler-24.02.0/Library/bin"


# # Create the output parent folder if it doesn't exist
# os.makedirs(output_parent_folder, exist_ok=True)

# # Iterate over each PDF file in the folder
# for pdf_file in os.listdir(pdf_folder):
#     if pdf_file.endswith(".pdf"):
#         # Create a folder with the PDF file's name
#         pdf_name = os.path.splitext(pdf_file)[0]
#         output_folder = os.path.join(output_parent_folder, pdf_name)
#         os.makedirs(output_folder, exist_ok=True)
        
#         # Convert only the first page of the PDF to an image
#         images = convert_from_path(
#             os.path.join(pdf_folder, pdf_file),
#             poppler_path=poppler_path,
#             first_page=1, last_page=1  # Extract only the first page
#         )
        
#         # Save the image in the output folder
#         images[0].save(os.path.join(output_folder, f"page_1.png"), "PNG", quality=100)

print("First pages saved successfully.")
