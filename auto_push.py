from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time
from datetime import datetime


class AutoCommitHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            try:
                subprocess.run(["git", "add", "."], check=True)
                message = f"Auto-commit: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                subprocess.run(["git", "commit", "-m", message], check=True)
                subprocess.run(["git", "push", "origin", "main"], check=True)
                print(f"[Pushed] {message}")
            except subprocess.CalledProcessError:
                pass


if __name__ == "__main__":
    path = "."
    event_handler = AutoCommitHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=True)
    observer.start()
    print("🚀 Watching for file changes... (Ctrl+C to stop)")
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
