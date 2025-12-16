import sys
import os

CHUNK_SIZE = int(19.9 * 1024 * 1024)  # ~19.9 MB

def split_file(filename):
    if not os.path.isfile(filename):
        print(f"Error: {filename} not found.")
        sys.exit(1)

    filesize = os.path.getsize(filename)
    part_num = 1

    with open(filename, "rb") as f:
        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            part_filename = f"{filename}.part{part_num}"
            with open(part_filename, "wb") as part_file:
                part_file.write(chunk)
            print(f"Wrote {part_filename} ({len(chunk)} bytes)")
            part_num += 1

    print(f"Done! Split into {part_num-1} parts.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: splitfile <filename>")
        sys.exit(1)
    split_file(sys.argv[1])
