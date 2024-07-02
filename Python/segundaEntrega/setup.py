from setuptools import setup, find_packages

setup(
    name="pedidos",
    version="1.0",
    description="Paquete segunda entrega",
    author="Lautaro Perez",
    author_email="perezlautaro@hotmail.com",
    packages=find_packages(), 
    scripts=["Pedidos/menu.py"] 
)
