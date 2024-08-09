import os

def search_text_in_file(file_path, text):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                if text.lower() in line.lower():  # Make search case-insensitive
                    return True
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
    return False

def search_files(directory, text):
    matched_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Scanning file: {file_path}")
            if search_text_in_file(file_path, text):
                print(f"Text found in: {file_path}")
                matched_files.append(file_path)
        
        for sub_dir in dirs:
            sub_dir_path = os.path.join(root, sub_dir)
            print(f"Scanning sub-folder: {sub_dir_path}")
    print("Matched Files Path:- ", matched_files)
    return matched_files

def save_to_file(file_list, output_file):
    with open(output_file, 'w') as f:
        for file_name in file_list:
            f.write(f"{file_name}\n")

def list_directories(base_directory):
    directories = []
    for root, dirs, _ in os.walk(base_directory):
        for directory in dirs:
            directories.append(os.path.join(root, directory))
    directories.insert(0, base_directory)  # Include the base directory itself
    return directories

def main(base_directory, text, output_file="file.txt"):
    directories = list_directories(base_directory)
    
    print("Select the directory you want to scan:")
    for i, directory in enumerate(directories):
        print(f"{i}: {directory}")
    
    user_input = input("Enter the number corresponding to the directory or the full directory path: ")
    
    if user_input.isdigit():  # If the input is a number
        selected_index = int(user_input)
        if 0 <= selected_index < len(directories):
            selected_directory = directories[selected_index]
        else:
            print("Invalid selection. Exiting.")
            return
    elif os.path.isdir(user_input):  # If the input is a valid directory path
        selected_directory = user_input
    else:
        print("Invalid input. Exiting.")
        return
    
    print(f"\nStarting scan in directory: {selected_directory}\n")
    
    matched_files = search_files(selected_directory, text)
    save_to_file(matched_files, output_file)
    
    if matched_files:
        print(f"\nSearch complete. {len(matched_files)} files found containing the text '{text}'. Results saved to {output_file}.")
    else:
        print(f"\nNo files found containing the text '{text}'. Check the text or the directory and try again.")

# Example usage
if __name__ == "__main__":
    base_directory = os.getcwd()  # Current directory
    text_to_find = input("Enter the text you want to search for: ")
    output_file_name = "file.txt"
    
    main(base_directory, text_to_find, output_file_name)
