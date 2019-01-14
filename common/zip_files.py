# -*- coding:utf-8 -*-
# @Time   : 2019-01-14 19:04
# @Author : YangWeiMin
import zipfile
import os
from common.logger import Log

class ZipMethod(object):
    """压缩文件的公共方法"""


    def __init__(self, file_path):
        self.file_path = file_path
        self.log = Log()


    def zip_files(self, zip_name):
        """将路径下的所有文件压缩成zip包"""
        data = os.listdir(self.file_path)
        zip_file = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
        for file in data:
            self.log.info('%s正在压缩中......' % file)
            zip_file.write(file)
        zip_file.close()
        self.log.info('压缩完成')


    def zip_path(self, zip_name):
        """按照全路径压缩文件"""
        data = os.listdir(self.file_path)
        if len(data) == None or len(data) < 1:
            self.log.info('待压缩的文件目录：%s' % self.file_path + '里面不存在文件，不需要压缩')
        else:
            zip_file = zipfile.ZipFile(self.file_path, 'w', zipfile.ZIP_DEFLATED)
            for file in data:
                self.log.info('%s正在压缩中......' % file)
                filefullpath = os.path.join(self.file_path, file)
                zip_file.write(filefullpath, file)
            zip_file.close()






