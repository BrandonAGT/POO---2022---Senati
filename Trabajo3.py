def singleton(cls):
  instance = dict()
  def wrap(*args, **kwargs):
    if cls not in instance:
      instance[cls] = cls(*args, **kwargs)
    return instance[cls]
  return wrap

class Producto:

    def __init__(self, id, descripcion, costo):
        self.id = id
        self.descripcion = descripcion
        self.costo = costo

    def crear_etiqueta(self):
        return '%s %s %0.2f'%(self.id, self.descripcion, self.costo)

@singleton   
class Electronico(Producto):

    def __init__(self, id, descripcion, costo, marca):
        super().__init__(id,descripcion,costo)
        self.marca = marca
if __name__ == '__main__':
        vendedor1 = Electronico('Electrodomestico','Lavadora',1800,'LG')
        vendedor2 = Electronico('Electrodomestico','Aspiradora',750,'Philips')
        print(vendedor1 is vendedor2)
        print('Esta en uso')

class Comestible(Producto):

    def __init__(self, id, descripcion, costo, caducidad):
        super().__init__(id,descripcion,costo)
        self.caducidad = caducidad

    def crear_etiqueta(self):
        return super().crear_etiqueta()+'\n %s'%self.caducidad
if __name__ == '__main__':
        vendedor1 = Comestible('Alimentos','Gomitas',1.3,'FV: 05/7/2024')
        vendedor1 = Comestible('Alimentos','Leche',1.7,'FV: 12/5/2023')
        variable = print(vendedor1 is vendedor2)
        if variable == True:
            print('Esta en uso')