import logging
import threading
import os
import shutil
from datetime import datetime

_logger = None
_logger_lock = threading.Lock()

class TimestampedRotatingFileHandler(logging.FileHandler):
    def __init__(self, filename, maxBytes=0, backupDir="logs", encoding=None):
        super().__init__(filename, mode='a', encoding=encoding)
        self.baseFilename = os.path.abspath(filename)
        self.maxBytes = maxBytes
        self.backupDir = backupDir
        os.makedirs(self.backupDir, exist_ok=True)

    def shouldRollover(self, record):
        if self.stream is None:  # Delay was set, so open it now
            self.stream = self._open()
        self.stream.flush()
        if os.path.getsize(self.baseFilename) >= self.maxBytes:
            return True
        return False

    def doRollover(self):
        if self.stream:
            self.stream.close()
            self.stream = None

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = os.path.join(self.backupDir, f"log_file_{timestamp}.log")

        shutil.copy(self.baseFilename, backup_file)
        with open(self.baseFilename, "w"):  # Clear the current log file
            pass


def get_logger():
    global _logger
    if _logger:
        return _logger

    with _logger_lock:
        if _logger:
            return _logger

        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)

        log_file = os.path.join(log_dir, "log_file.log")

        logger = logging.getLogger("GlobalTestLogger")
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            fmt="%(asctime)s - [PID %(process)d] - [%(levelname)s] - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # Use custom rotating handler
        file_handler = TimestampedRotatingFileHandler(
            filename=log_file,
            maxBytes=5 * 1024 * 1024,  # 5 MB
            backupDir=log_dir,
            encoding="utf-8"
        )
        file_handler.setFormatter(formatter)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        logger.propagate = False

        _logger = logger
        return _logger
