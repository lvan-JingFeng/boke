import pymysql
pymysql.version_info = (1, 4, 13, "final", 0)  # 修改数据库配置，匹配项目对应的数据库
pymysql.install_as_MySQLdb()