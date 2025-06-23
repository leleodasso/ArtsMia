from database.DB_connect import DBConnect
from model.artObject import ArtObject


class DAO():

    @staticmethod
    def getAllObjects():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select * from objects o  """

        cursor.execute(query)

        for row in cursor:
            result.append(ArtObject(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges(idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ 
                    select eo1.object_id as id1, eo2.object_id as id2, count(*) as peso
                    from exhibition_objects eo1, exhibition_objects eo2
                    where eo1.exhibition_id = eo2.exhibition_id
                    and eo1.object_id > eo2.object_id
                    group by eo1.object_id, eo2.object_id 
                """

        cursor.execute(query)

        for row in cursor:
            result.append((idMap[row["id1"]], idMap[row["id2"]],row["peso"]))
        cursor.close()
        conn.close()
        return result


