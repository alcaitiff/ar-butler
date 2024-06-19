import os

class Forget:
  cfg = {}
  mic = {}
  transcriptor = {}

  def __init__(self, config):
    self.cfg = config

  def get_answer(self):
    self.mic.detect_and_record()
    return self.transcriptor.transcribe(self.cfg.mic.audio_file).strip().translate(str.maketrans(dict.fromkeys(',!.;:', '')))

  def delete_line_from_file(self,file_path, line_number):
    try:
        # Check if the line number is valid
        if line_number < 0:
          print("Error: number should be greater than 0.")
          return
        # Read through the file to find the specified line
        with open(file_path, 'r') as file:
          lines = list(enumerate(file, start=1))
        if line_number > len(lines):
          print(f"Error: The memory has only {len(lines)} lines.")
          return
        # Get the line to delete
        line_to_delete = lines[line_number][1].strip()
        # Print the specified line
        print(f"{line_number}: {line_to_delete}")
        # Ask user if they want to delete this line
        print('\033[93m Forget it?\033[0m[Yes/No]')
        user_input = self.get_answer().upper()
        if user_input in self.cfg.actions.yes.keywords:
          # Create a temporary file to write the updated content
          temp_file_path = file_path + '.tmp'
          with open(file_path, 'r') as file, open(temp_file_path, 'w') as temp_file:
            for i, line in enumerate(file):
              if i != line_number:
                temp_file.write(line)
          # Replace the original file with the temporary file
          os.replace(temp_file_path, file_path)
          print(f"Memory {line_number} has been erased.")
        else:
          print("No changes were made.")
    except FileNotFoundError:
      print("Error: No memory found.")

  def do_action(self,msg,mic,transcriptor):
    self.mic=mic
    self.transcriptor=transcriptor
    arg=msg.strip().split(' ',1)[1].translate(str.maketrans(dict.fromkeys(',!.;:', '')))
    print("Forgeting: "+arg)
    self.delete_line_from_file(self.cfg.memory.text_file_path,int(arg))
