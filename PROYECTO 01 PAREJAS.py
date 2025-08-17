class producto:
    def _init_(self, codigo, nombre, categoria, precio, stock):
        self.codigo=codigo
        self.nombre=nombre
        self.categoria=categoria
        self.precio=precio
        self.stock=stock
        self.valido=True



class Inventario:
    def _init_(self):
        self.productos={}
    def agregar_productos(self,producto):
        if producto.codigo == "" or producto.nombre == "" or producto.categoria == "":
            print("error, no puedes dejar espacios en blanco")
            return
        if producto.precio < 0 or producto.stock < 0:
            print("error, precio o stock debe ser positivo")
            return
        if producto.codigo in self.productos:
            print("error, el codigo ya existe")

        self.productos[producto.codigo]=producto
        print("producto agregado correctamente")

inventario = Inventario()

cantidad=int(input("cuantos productos desea ingresar"))

for i in range(cantidad):
    print(f"prodcuto {i+1} ")
    codigo = input("codigo: ")
    nombre = input("nombre: ")
    categoria=input("categoria: ")
    precio = input("precio: ")
    stock = int(input("stock"))

    prod=producto(codigo, nombre, categoria, precio,stock)
    inventario.agregar_productos(prod)

print("productos registrados")
for codigo, prod in inventario.productos.items():
    print("codigo: ",codigo)
    print("nombre: ", prod.nombre)
    print("categoria: ",prod.categoria)
    print("precio: ",prod.precio)
    print("stock: ",prod.stock)
'''***********************************************'''
    def quick_sort(lista):
        if len(lista) <= 1:
            return lista

        pivote = lista[0]
        menores = [x for x in lista[1:] if x < pivote]
        iguales = [x for x in lista[1:] if x == pivote]
        mayores = [x for x in lista[1:] if x > pivote]

        return quick_sort(menores) + iguales + quick_sort(mayores)
    numeros =
