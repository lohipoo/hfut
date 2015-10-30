# hfut-stu-lib
[![PyPI version](https://badge.fury.io/py/hfut_stu_lib.svg)](http://badge.fury.io/py/hfut_stu_lib)
[![Build Status](https://travis-ci.org/evilerliang/hfut-stu-lib.svg?branch=dev)](https://travis-ci.org/evilerliang/hfut-stu-lib)
[![Coverage Status](https://coveralls.io/repos/evilerliang/hfut-stu-lib/badge.svg?branch=dev&service=github)](https://coveralls.io/github/evilerliang/hfut-stu-lib?branch=dev)

----

Provided full-featured interfaces for the educational administration system of HeFei University of Technology.

提供了合肥工业大学教务系统学生端接口并提供了方便开发者开发围绕学生数据的一些工具

# 快速开始

- 安装
    
    ```
    $ pip install hfut_stu_lib
    ```

- 使用

    ```
    >>> from hfut_stu_lib import AuthSession, STUDENT
    >>> stu = AuthSession('your-account', 'your-password', STUDENT)
    >>> stu.get_stu_info()
    ```


**更新日志请查看** *[CHANGES.md](https://github.com/evilerliang/hfut-stu-lib/blob/master/CHANGES.md)*