
init -200 python:

    from multipledispatch import dispatch

    class Paths:

        _base_path = "mod_assets/images"
        _file_format = "png"

        @dispatch(str, str, str)
        def monika(self, part: str, type: str, filename:str) -> str:
            return f"{self._base_path}/monika/{part}/{type}/{filename}.{self._file_format}"
        
        @dispatch(str, str)
        def monika(self, part: str, filename:str) -> str:
            return f"{self._base_path}/monika/{part}/{filename}.{self._file_format}"

        @dispatch(str, str, str)
        def natsuki(self, part: str, type: str, filename:str) -> str:
            return f"{self._base_path}/natsuki/{part}/{type}/{filename}.{self._file_format}"
        
        @dispatch(str, str)
        def natsuki(self, part: str, filename:str) -> str:
            return f"{self._base_path}/natsuki/{part}/{filename}.{self._file_format}"
        
        @dispatch(str, str, str)
        def yuri(self, part: str, type: str, filename:str) -> str:
            return f"{self._base_path}/yuri/{part}/{type}/{filename}.{self._file_format}"
        
        @dispatch(str, str)
        def yuri(self, part: str, filename:str) -> str:
            return f"{self._base_path}/yuri/{part}/{filename}.{self._file_format}"

        @dispatch(str, str, str)
        def sayori(self, part: str, type: str, filename:str) -> str:
            return f"{self._base_path}/sayori/{part}/{type}/{filename}.{self._file_format}"
        
        @dispatch(str, str)
        def sayori(self, part: str, filename:str) -> str:
            return f"{self._base_path}/sayori/{part}/{filename}.{self._file_format}"

    paths = Paths()