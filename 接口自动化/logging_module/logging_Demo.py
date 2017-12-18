import logging.handlers
import logging

class FinalLogger:
    logger = None

    levels = {"n":logging.NOTSET,
              "d":logging.DEBUG,
              "i":logging.INFO,
              "w":logging.WARNING,
              "e":logging.ERROR,
              "c":logging.CRITICAL
              }
    log_level = "d"
    log_file = ".\\test.log"
    log_max_byte = 10 * 1024 * 1024
    log_backup_count = 5

    #类的静态方法，只初始化一次，后面若需要用到这个类，直接调用即可
    @staticmethod
    def getLogger():
        if FinalLogger.logger is not None:
            return FinalLogger

        FinalLogger.logger = logging.getLogger("oggingmodule.FinalLogger")
        log_handler = logging.handlers.RotatingFileHandler(filename=FinalLogger.log_file,
                                                   maxBytes=FinalLogger.log_max_byte,
                                                   backupCount=FinalLogger.log_backup_count)
        log_fmt = logging.Formatter("%(levelname)s %(funcName)s %(lineno)d %(asctime)s %(message)s")

        log_handler.setFormatter(log_fmt)
        FinalLogger.logger.addHandler(log_handler)

        FinalLogger.logger.setLevel(FinalLogger.levels.get(FinalLogger.log_level))
        return FinalLogger.logger

if __name__ == "__main__":
    logger = FinalLogger().getLogger()

    #新建一个handler，用于将日志打印到屏幕上
    console = logging.StreamHandler()
    console.setLevel(logging.WARNING)
    formatter = logging.Formatter("%(levelname)s-%(funcName)s-%(lineno)d-%(asctime)s-%(message)s")
    console.setFormatter(formatter)

    logger.addHandler(console)

    logger.debug("this is a debug msg")
    logger.info("this is a info msg")
    logger.warning("this is a warning msg")
    logger.error("this is a error msg")
    logger.critical("this is a critical msg")