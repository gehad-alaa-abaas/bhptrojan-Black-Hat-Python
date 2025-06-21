import os
import zipfile

zip_path = r""
extract_to = r""

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    for member in zip_ref.infolist():
        # Replace colons in the filename
        fixed_name = member.filename.replace(':', '_')
        # Build the full output path
        out_path = os.path.join(extract_to, *fixed_name.split('/'))
        # Create directories as needed
        if member.is_dir():
            os.makedirs(out_path, exist_ok=True)
        else:
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            with open(out_path, 'wb') as f:
                f.write(zip_ref.read(member.filename))

print("Done! All files extracted and renamed to:", extract_to)