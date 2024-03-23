import os
import json
import urllib.parse

def clean_file(resource_path):
      # Decoding the URL-encoded path and removing the 'file:///' prefix
    decoded_path = urllib.parse.unquote(resource_path.lstrip("file:///"))

    # Extracting the relative path part
    dcd = decoded_path.split('/')[1:]
    dcd = [item for item in dcd if item]
     
    
    return '/'.join(dcd)
 
def recover_file(resource_path:str, contents):
    relative_path = clean_file(resource_path)
    # Constructing the new path within the '_recovery' folder
    new_path = os.path.join('Recovery', relative_path)

    # Creating the directory structure if it doesn't exist
    os.makedirs(os.path.dirname(new_path), exist_ok=True)

    # Creating an empty 'serializers.py' file
    with open(new_path, 'w', encoding='utf-8') as f:
        f.write(contents)

    print(f"File created at: {new_path}")

def get_vscode_path():
  """
  Gets the path to the VS Code directory across different operating systems.

  Returns:
      str: The path to the VS Code directory, including the "User/History" folder.
  """

  if os.name == 'nt':  # Windows
    code_dir = os.path.join(os.environ['APPDATA'], 'Code')
  elif os.name == 'posix':  # macOS or Linux
    if 'HOME' in os.environ:
      home_dir = os.environ['HOME']
      if os.path.exists(os.path.join(home_dir, 'Library', 'Application Support', 'Code')):
        code_dir = os.path.join(home_dir, 'Library', 'Application Support', 'Code')
      else:
        code_dir = os.path.join(home_dir, '.config', 'Code')
    else:
      raise EnvironmentError('Could not determine home directory')
  else:
    raise EnvironmentError('Unsupported operating system')

  return os.path.join(code_dir, 'User', 'History')


class Recover:
    @staticmethod
    def print_files(search_term):
        xs = []
        base_folder = get_vscode_path()
        for folder in os.listdir(base_folder):
            if not folder.startswith("_recovery"):
                entries_path = os.path.join(base_folder, folder, 'entries.json')
                if os.path.exists(entries_path):
                    with open(entries_path, 'r') as f:
                        data = json.load(f)
                        if search_term in data['resource']:
                            xs.append("found "+  clean_file(data['resource']))
        xs.sort()
        for x in xs:
            print(x)

    @staticmethod
    def restore_files(search_term):
        vs_folder = get_vscode_path()
        base_folder = os.getcwd()

        for folder in os.listdir(vs_folder):
            if not folder.startswith("_recovery"):
                entries_path = os.path.join(vs_folder, folder, 'entries.json')
                if os.path.exists(entries_path):
                    with open(entries_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        if search_term in data['resource']:
                            max_f = None
                            for x in data['entries']:
                                if not max_f:
                                  max_f = x
                                elif max_f['timestamp'] < x['timestamp']: 
                                  max_f = x
                            if max_f: 
                                with open(os.path.join(vs_folder, folder, max_f['id']), 'r', encoding='utf-8') as f:
                                    recover_file( data['resource'] , f.read())


if __name__ == "__main__":    
#    print(get_vscode_path())
    # Recover.print_files("/Chetan/Documents/tasks") 
    Recover.restore_files("/Chetan/Documents/tasks")