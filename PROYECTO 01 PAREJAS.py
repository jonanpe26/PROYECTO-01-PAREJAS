class producto:
    def __init__(self, codigo, nombre, categoria, precio, stock):
        self.codigo=codigo
        self.nombre=nombre
        self.categoria=categoria
        self.precio=float(precio)
        self.stock=int(stock)
        self.valido=True
    def __str__(self):
        return f"[{self.codigo} {self.nombre}{self.categoria} Q{self.precio:.2f} Stock: {self.stock}]"


class Inventario:
    def __init__(self):
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

    def ListaProductos(self,criterio="nombre"):
        lista = list(self.productos.values())
        ListaOrdenada = OrdenarProducto.quick_sort(lista,criterio)
        for x in ListaOrdenada:
            print(x)

    def ActualizarProductos(self,codigo,nuevoprecio=None,nuevostock=None):
         if codigo not in self.productos:
             print("Productos no encontrados.")
             return
         if nuevoprecio is not None:
            self.productos[codigo].precio = float(nuevoprecio)
         if nuevostock is not None:
             self.productos[codigo].stock = int(nuevostock)
         print("Producto actualizado correctamente.")
    def EliminarProducto(self,codigo):
        if codigo in self.productos:
            del self.productos[codigo]
            print("Producto eliminado!")
        else:
            print("Codigo del producto no encontrado")

inventario = Inventario()


class OrdenarProducto:
    def quick_sort(lista,criterio):
        if len(lista) <= 1:
            return lista

        pivote = lista[0]
        menores = [x for x in lista[1:] if getattr(x, criterio) < getattr(pivote,criterio)]
        iguales = [x for x in lista[1:] if getattr(x,criterio) == getattr(pivote,criterio)]
        mayores = [x for x in lista[1:] if getattr(x,criterio) > getattr(pivote,criterio)]

        return OrdenarProducto.quick_sort(menores,criterio) + [pivote] + iguales + OrdenarProducto.quick_sort(mayores,criterio)

class Buscador:
    def buscar(lista,campo,valor):
        resultados = []
        valor = valor.lower()
        for x in lista:
            if campo == "codigo" and x.codigo == valor:
                resultados.append(x)
            elif campo == "nombre" and valor in x.nombre.lower():
                resultados.append(x)
            elif campo == "categoria" and valor in x.categoria.lower():
                resultados.append(x)
        return resultados




print("productos registrados")
for codigo, prod in inventario.productos.items():
    print("codigo: ",codigo)
    print("nombre: ", prod.nombre)
    print("categoria: ",prod.categoria)
    print("precio: ",prod.precio)
    print("stock: ",prod.stock)

def menu():
    inventario = Inventario()
    while True:
        print("\n*******MENU PRINCIPAL*******")
        print("1. Registrar productos")
        print("2. Lista de productos")
        print("3. Buscar productos")
        print("4. Actualizar productos")
        print("5. Eliminar productos")
        print("6. Salir")

        opcion = input("Elija una opcion: ")
        if opcion == "1":
            print("****AGREGAR PRODUCTOS****")
            cantidad = int(input("cuantos productos desea ingresar: "))
            for i in range(cantidad):
                print(f"producto #{i + 1} ")
                codigo = int(input("Codigo: "))
                nombre = input("Nombre: ")
                categoria = input("Categoria: ")
                precio = float(input("Precio: "))
                stock = int(input("Stock: "))
                inventario.agregar_productos(producto(codigo,nombre,categoria,precio,stock))
        elif opcion == "2":
            print("***LISTA DE PRODUCTOS***")
            ListaProducto = input("Como le gustaria ver la lista? por: nombre,precio,stock ")
            inventario.ListaProductos(ListaProducto)
        elif opcion == "3":
            print("***BUSCAR PRODUCTO***")
            campo = input("Buscar por (Codigo,nombre,categoria: )")
            valor = input("Ingrese el valor que desea buscar: ")
            resultado = Buscador.buscar(list(inventario.productos.values()),campo,valor)
            if resultado:
                for x in resultado:
                    print(x)
            else:
                print("Datos invalidos")
        elif opcion == "4":
            print("***ACTUALIZAR PRODUCTOS***")
            continue
        elif opcion == "5":
            print("***ELIMINAR PRODUCTOS***")
            codigo = input("Ingrese el codigo del producto que desea eliminar: ")
            inventario.EliminarProducto(codigo)
        elif opcion == "6":
            print("Hasta pronto!")
            break
        else:
            print("Opcion invalida.")
menu()