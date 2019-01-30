# from src import connectionStr
# import cx_Oracle
#
#
# class DB_INIT(object):
#     def __connect__(self):
#         try:
#             con = cx_Oracle.Connection(connectionStr)
#             db = con.cursor()
#             return db
#         except Exception as e:
#             print(str(e))
#
#     def executeQuery(self, query):
#         db = self.__connect__()
#         result = []
#         try:
#             print(db)
#             for row in db.execute(query).fetchall():
#                 print(row)
#                 result.append(row)
#         except Exception as e:
#             print(e)
#         return result
#
#