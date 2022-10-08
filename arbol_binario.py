class Nodo:
    def __int__(self, valor):
        self.valor = valor
        self.lef = None
        self.right = None

class ArbolBinario:
        def __init__(self):
            self.root = None

        def crear_desde_archivo(self, nombre): # Esto es un wrapper se llama otra funcion dentro de esta

            try:
                handle = open(nombre, 'r')
            except IOError: #INPUT OUTPUT ERROR
                return None

            self.root = self._crear_desde_archivo(handle)

            handle.close()

            if self.root is None:
                return None
            return 1

        def _crear_desde_archivo(self, handle): # Esta funcion con el primer underscore se va a ver cm privada
            c = handle.read(1) # Lee solo un caracter, o sea un bit. Eso se paso

            if c == '$':
                return None

            tmp = Nodo(c)

            tmp.lef = self._crear_desde_archivo(handle)
            tmp.right = self.crear_desde_archivo(handle)

            return tmp

        def pre_orden(self):
            self._pre_orden(self.root)

        def in_orden(self):
            self._pre_orden(self.root)

        def post_orden(self):
            self._pre_orden(self.root)

        def _pre_orden(self, actual): # Actual es la raiz de cada subarbol
            if actual is None:
                return None

            print(actual.valor, end=' ')

            self._pre_orden(self, actual.lef)
            self._pre_orden(self, actual.right)

        def _in_orden(self, actual): # Actual es la raiz de cada subarbol
            if actual is None:
                return None

            self._pre_orden(self, actual.lef)
            print(actual.valor, end=' ')
            self._pre_orden(self, actual.right)

        def _post_orden(self, actual): # Actual es la raiz de cada subarbol
            if actual is None:
                return None

            self._pre_orden(self, actual.lef)
            self._pre_orden(self, actual.right)
            print(actual.valor, end=' ')
