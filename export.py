import os
import sys

# TODO: add boolean to import functions from global utils.sk file used across all files into output file.

def compile_scripts(folder_path, output_filename):
    """
    Combines all local .sk files in the given folder into a single .sk file to be easily exported
    """
    output_path = os.path.join(folder_path, output_filename)

    sk_files = [f for f in sorted(os.listdir(folder_path)) if f.endswith('.sk') and f != output_filename]

    if "config.sk" in sk_files:
        sk_files.remove("config.sk")
        sk_files.insert(0, "config.sk")

    with open(output_path, 'w', encoding='utf-8') as outfile:
        first = True
        for filename in sk_files:
            file_path = os.path.join(folder_path, filename)
            
            with open(file_path, 'r', encoding='utf-8') as infile:
                if not first:
                    outfile.write("\n")
                else:
                    first = False

                outfile.write(f"## [SECTION: {filename}]\n")
                outfile.write(infile.read().strip() + "\n\n")

    print(f"Compiled scripts into {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python export.py <folder_path> <output_file>")
    else:
        compile_scripts(sys.argv[1], sys.argv[2])
