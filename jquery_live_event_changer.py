import os
import re
import argparse

# Define the regex pattern to match .live() events
pattern = r"\$\(['\"](.+?)['\"]\)\.live\(\s*['\"](.+?)['\"]\s*,\s*(.*)"
replacement = r'$(document).on("\2", "\1", \3'

def replace_live_events(directory):
    # Recursively scan the directory for .aspx and .js files
    for subdir, dirs, files in os.walk(directory):
        print("Currently working on " + subdir + "...")
        for file in files:
            filepath = os.path.join(subdir, file)
            if filepath.endswith('.aspx') or filepath.endswith('.js'):
                # Open the file and read its contents
                with open(filepath, 'r') as f:
                    content = f.read()
                    # Replace all instances of .live() with $(document).on() using the selector parameter
                    new_content = re.sub(pattern, replacement, content)
                    #new_content = re.sub(pattern, replacement2, content)
                # Write the new contents back to the file
                with open(filepath, 'w') as f:
                    f.write(new_content)
        print("Completed: " + subdir)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("arg", help="argument to be passed to the script")
    args = parser.parse_args()
    print("Replacing .live() events to $(document).on events...")
    replace_live_events(args.arg)
    print("Replaced successfully!")

if __name__ == '__main__':
    main();
