from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53
from diagrams.onprem.database import PostgreSQL  # Would typically use RDS from aws.database
from diagrams.onprem.inmemory import Redis  # Would typically use ElastiCache from aws.database

with Diagram("New_diagram") as diag:
   """Diagram automatically creates, opens and saves a diagram.
    (even if the code is empty and is not called anywhere)"""
    # Each created object is added "from above".
    dns = Route53("dns")  # Значок с надписью 53
    load_balancer = ELB("load_balancer")
    data_base = PostgreSQL("PostGreSql")
    redis = Redis("Redis")

    with Cluster("databases"):
        """Класс cluster объединяет объекты, созданные в нём, в кластер на диаграмме"""
        svc_group = [
            EC2("Data base1"),
            EC2("Data base2"),
            EC2("Data base3"),

                     ]
    # --------------------------------------------
    dns >> load_balancer >> svc_group >> redis >> data_base
    # double arrows ">>" link two created objects in the diagram with an arrow
    
