
**VSCode Deleted File Recovery Tool**

This tool helps you recover deleted files from your VSCode History.

**Features:**

* **File Search:** Scans vscode history for traces of deleted files.
* **Recovery:** Restores deleted files to a designated `_recovery` folder, organized to match original file structure.

**Usage**

1. **Install:**
```bash
pip install vscode_deleted_file_recovery
```

2. Create a Python file anywhere on your PC and run the following code to search for files:
```python
from vscode_deleted_file_recovery import Recover
Recover.print_files(search_term="/Chetan/Documents/tasks")  # Replace with your desired search path
```

3. Run the following code to restore deleted files. A folder named `_recovery` will be created in the same directory where you run it:
```python
from vscode_deleted_file_recovery import Recover
Recover.restore_files(search_term="/Chetan/Documents/tasks")  # Replace with your desired search path
```

You can find restored files in the `Recovery` folder where you ran the command.

## Love It? [Star It! ⭐](https://github.com/Chetan11-dev/vscode-deleted-file-recovery)

Become one of our amazing stargazers by giving us a star ⭐ on GitHub!

It's just one click, but it means the world to me.

<a href="https://github.com/Chetan11-dev/vscode-deleted-file-recovery/stargazers">
    <img src="https://bytecrank.com/nastyox/reporoster/php/stargazersSVG.php?user=Chetan11-dev&repo=vscode-deleted-file-recovery" alt="Stargazers for @Chetan11-dev/vscode-deleted-file-recovery">
</a>
