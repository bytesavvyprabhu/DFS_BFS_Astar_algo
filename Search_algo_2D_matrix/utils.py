import os

def list_files(directory):
    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        if not files:
            print("No files found in the directory.")
            return
        print("Files in directory:")
        for idx, file in enumerate(files, start=1):
            print(f"{idx}. {file}")
        file_index = int(input(f"Select a file by entering its number between(1-{len(files)}): "))
        if file_index < 1 or file_index > len(files):
            print("Invalid selection.")
            return
        
        selected_file = files[file_index - 1]
        return selected_file
    
    except FileNotFoundError:
        print("The directory does not exist.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    directory = "maze_in_txt"
    list_files(directory)
