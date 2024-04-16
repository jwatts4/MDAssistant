import os
import subprocess
import sys


def aggregate_folder():
    """
    Concatenate all the MD files in specified folder, using 
    filenames and figlet (or some other utility) to create nice titles.

    """
    pass


def reformat_markdown(directory, columns):
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            filepath = os.path.join(directory, filename)
            temp_filepath = os.path.join(directory, "temp.md")
            # Call Pandoc to reformat the markdown file
            subprocess.run(
                [
                    "pandoc",
                    "-f",
                    "markdown",
                    "-t",
                    "markdown",
                    "--columns",
                    str(columns),
                    "-o",
                    temp_filepath,
                    filepath,
                ]
            )
            # Overwrite the original file with the new formatted file
            os.rename(temp_filepath, filepath)
            print(f"Reformatted: {filepath}")


def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py [directory] [columns]")
        sys.exit(1)

    directory = sys.argv[1]
    columns = int(sys.argv[2])
    reformat_markdown(directory, columns)


if __name__ == "__main__":
    main()
