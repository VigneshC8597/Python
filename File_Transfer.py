import shutil

def send_file(source_path, destination_path):
    try:
        shutil.move(source_path, destination_path)
        print("File sent successfully!")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    source_path = "D:\\Godrej_application_count\\Batch Count\\Matching Count\\AMCPCP_828.xlsx"
    destination_path = "D:\\Godrej_application_count\\Batch Count\\MisMatching Count"
    send_file(source_path, destination_path)
