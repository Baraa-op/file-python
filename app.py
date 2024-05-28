import os

path = '/storage/emulated/0/'

def delete_files_by_extension(path):
    try:
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if filename.lower().endswith((
                '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.raw',
                '.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv',
                '.mp3', '.aac', '.wma', '.wav', '.flac', '.ogg', '.m4a',
                '.pdf', '.txt', '.py', '.html', '.htm', '.doc', '.docx', 
                '.xls', '.xlsx', '.ppt', '.pptx', '.rtf', '.odt', '.mobi', 
                '.tcr', '.xml', '.json', '.epub', '.azw',
                '.zip', '.7z', '.rar', '.tar', '.gz', '.bz2', '.xz',
                '.java', '.c', '.h', '.cpp', '.php', '.rb', '.go',
                '.css', '.js', '.asp', '.aspx',
                '.sql', '.db', '.sqlite',
                '.bat', '.sh', '.bin', '.exe', '.dll', '.sys', '.tmp',
                '.iso', '.dmg', '.img', '.cue', '.bin', '.vmdk',
                '.log', '.cfg', '.ini', '.dat', '.bak',
                '.md', '.markdown', '.rst', '.tex',
                '.avi', '.mov', '.mpg', '.mpeg', '.m4v', '.3gp',
                '.ai', '.eps', '.psd', '.xcf', '.indd', '.sketch',
                '.key', '.numbers', '.pages'
            )):
                os.remove(file_path)
                print(f"✅ {filename} has been deleted")
    except Exception as e:
        print(f"Error: {str(e)}")

delete_files_by_extension(path)
