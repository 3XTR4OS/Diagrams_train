from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53
from diagrams.onprem.database import PostgreSQL  # Would typically use RDS from aws.database
from diagrams.onprem.inmemory import Redis  # Would typically use ElastiCache from aws.database

with Diagram('Простая диаграмма') as diag:
    '''Diagram автоматически создаёт, открывает и сохраняет диаграмму.
    (даже если код пуст и нигде не вызывается)'''
    # Каждый созданный объект добавляется "сверху".
    dns = Route53('Основной json ')  # Значок с надписью 53
    load_balancer = ELB('Балансировщик загрузки')
    data_base = PostgreSQL('User Database')
    redis = Redis('Редиска')

    with Cluster('Кластер с веб-серверами'):
        '''Класс cluster объединяет объекты, созданные в нём, в кластер на диаграмме'''
        svc_group = [EC2("Webserver 1"),
                     EC2("Webserver 2"),
                     EC2("Webserver 3")]
    # --------------------------------------------
    dns >> redis
    redis << redis
    redis << dns
    # двойные стрелки ">>" связывают два созданных объекта на диаграмме стрелочкой
