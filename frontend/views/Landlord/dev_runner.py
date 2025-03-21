import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# 🔧 Tên file Python bạn muốn theo dõi
file_to_watch = "MainWindowLandlord.py"


class ReloadHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(file_to_watch):
            print("🔁 Phát hiện thay đổi! Đang reload UI...")
            os.system(f"python {file_to_watch}")
            print("✅ UI đã chạy lại. Chờ lần sửa tiếp theo...\n")


if __name__ == "__main__":
    path = "."  # thư mục hiện tại
    event_handler = ReloadHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=False)
    observer.start()

    print(f"👀 Đang theo dõi file: {file_to_watch}")
    print("🛠️  Mỗi khi bạn lưu lại, UI sẽ tự chạy lại...\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
