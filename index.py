def read_modify_write_file():
    # Ask the user for the input filename
    filename = input("📂 Enter the name of the file to read: ")

    try:
        # Open the original file and read the content
        with open(filename, "r") as file:
            content = file.read()
            print("\n📝 Original Content:")
            print(content)

        # Modify the content (for example, convert to uppercase)
        modified_content = content.upper()

        # Prepare new filename and write the modified content
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"\n✅ Modified content saved to '{new_filename}'")

    except FileNotFoundError:
        print("❌ Error: The file was not found.")
    except PermissionError:
        print("❌ Error: Permission denied to read the file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the combined function
read_modify_write_file()

