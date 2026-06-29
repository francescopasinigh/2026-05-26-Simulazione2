from database.DB_connect import DBConnect
from model.connessione import Connessione
from model.names import Names
from model.rating import Rating


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllRating():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=False)
        query = """select distinct median_rating 
                    from ratings r 
                    order by r.median_rating  """

        cursor.execute(query)

        for row in cursor:
            result.append(Rating(row[0]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllActor():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct * 
                        from names  
                          """

        cursor.execute(query)

        for row in cursor:
            result.append(Names(**row))

        cursor.close()
        conn.close()
        return result
    @staticmethod
    def getAllNodes(n,x, idMapA):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct n.*
                    from names n ,role_mapping rm , movie m ,ratings r 
                    where n.id =rm.name_id 
                    and rm.movie_id =m.id 
                    and r.movie_id =m.id 
                    and r.avg_rating >%s
                    and r.avg_rating <=%s
                    group by n.id"""

        cursor.execute(query, (n,x))

        for row in cursor:
            result.append(Names(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdgesv1(idMapA):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select n.id,n2.id , m.worlwide_gross_income  as peso
                    from names n ,names n2 , role_mapping rm ,role_mapping rm2 ,movie m 
                    where n.id=rm.name_id
                    and n2.id=rm2.name_id
                    and rm.movie_id=rm2.movie_id 
                    and rm2.movie_id =m.id  
                    and n.id<n2.id """

        cursor.execute(query)

        for row in cursor:
            result.append((Connessione(
                idMapA[row["id"]],
                idMapA[row["id"]],
                row["peso"])))

        cursor.close()
        conn.close()
        return result