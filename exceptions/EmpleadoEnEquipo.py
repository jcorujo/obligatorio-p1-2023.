class EmpleadoEnEquipo(Exception):
    def __init__(self, codigo, descripcion):
        self._codigo = codigo
        self._descripcion = descripcion