from diagrams import Cluster, Diagram, Edge

from diagrams.custom import Custom



with Diagram("Docker Network Diagram", show=False):
    
    host = Custom("Host (localhost:2357)", "./Images/computer-icon.png")
    web = Custom("Website 1 (localhost:3000)", "./Images/web.png")
    web2 = Custom("Website 2 (localhost:8080)", "./Images/web.png")


    with Cluster("Docker Container 1"):
        
        with Cluster("Subcontainer 1 (port: 3000)"):
            Subcontainer1 = [Custom("Node JS", "./Images/node.png")] 
        
        with Cluster("Subcontainer 2 (port: 5432)"):
            Subcontainer2 = [Custom("Postgres", "./Images/post.png")]

    with Cluster("Docker Container 2"):
        
        with Cluster("Alpine Linux"):
            with Cluster("Apache http (port: 5000)"):
                Apache = [Custom("Apache http", "./Images/apache.png")] 
        





    host >> Edge(color="darkgreen") >>Subcontainer1 >> Edge(color="firebrick", style="dashed") >> web
    
    
    Subcontainer1 << Edge(color="firebrick", style="dashed") << web


    host >> Edge(color="darkgreen") >> Apache >> Edge(color="firebrick", style="dashed") >> web2
    
    Apache << Edge(color="firebrick", style="dashed") << web2 










  

  
    



