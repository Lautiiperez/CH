######################## 1-Generaciones Digitales
anio = int(input("En que año naciste?"))

if 2001 <= anio <= 2010:
    print("Generación Z")

elif 1980 <= anio <= 2000:
    print("Generación Y")

elif 1965 <= anio <= 1979:
    print("Generacion X")

elif 1946 <= anio <= 1964:
    print("Baby Boomer")
    
elif 1920 <= anio <= 1940:
    print("Generación Silenciosa")
else:
    print("No clasificado")