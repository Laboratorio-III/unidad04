from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from tinydb import TinyDB, Query
from typing import List
import datetime
import json
import os

FORMATO_FECHA = '%Y-%m-%d'


class Tarea:
    def __init__(self, tarea_id: int, titulo: str, descripcion: str, estado: str, creada: str, actualizada: str):
        self.tarea_id = tarea_id
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado
        self.creada = creada
        self.actualizada = actualizada

    def to_dict(self) -> dict:
        return {
            "id": self.tarea_id,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "estado": self.estado,
            "creada": self.creada,
            "actualizada": self.actualizada
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    def actualizar_fecha_actualizacion(self) -> None:
        self.actualizada = datetime.datetime.now().strftime(FORMATO_FECHA)


class AdminTarea:
    def __init__(self):
        self.db = TinyDB('tareas_db.json')
        self.tareas_table = self.db.table('tareas')

    def agregar_tarea(self, tarea: Tarea) -> int:
        tarea_dict = tarea.to_dict()
        tarea_id = self.tareas_table.insert(tarea_dict)
        return tarea_id

    def agregar_tareas(self, tareas: List[Tarea]) -> List[int]:
        tarea_ids = []
        for tarea in tareas:
            tarea_dict = tarea.to_dict()
            tarea_id = self.tareas_table.insert(tarea_dict)
            tarea_ids.append(tarea_id)
        return tarea_ids

    def traer_tarea(self, tarea_id: int) -> Tarea:
        tarea_dict = self.tareas_table.get(doc_id=tarea_id)
        if tarea_dict:
            tarea = Tarea(**tarea_dict)
            return tarea
        return None

    def actualizar_estado_tarea(self, tarea_id: int, estado: str) -> None:
        self.tareas_table.update({'estado': estado, 'actualizada': datetime.datetime.now().strftime(FORMATO_FECHA)},
                                 doc_ids=[tarea_id])

    def eliminar_tarea(self, tarea_id: int) -> None:
        self.tareas_table.remove(doc_ids=[tarea_id])

    def traer_todas_tareas(self) -> List[Tarea]:
        tareas_dicts = self.tareas_table.all()
        tareas = [Tarea(**tarea_dict) for tarea_dict in tareas_dicts if isinstance(tarea_dict, dict)]
        return tareas

    def cerrar_conexion(self) -> None:
        self.db.close()


class InterfazUsuario:
    def __init__(self, admin_tareas: AdminTarea):
        self.admin_tareas = admin_tareas

    def mostrar_menu(self) -> None:
        print("Selecciona una opción:")
        print("1. Agregar tarea")
        print("2. Agregar varias tareas")
        print("3. Traer tarea")
        print("4. Actualizar estado de tarea")
        print("5. Eliminar tarea")
        print("6. Traer todas las tareas")
        print("7. Salir")

    def agregar_tarea(self) -> None:
        tarea_id = int(input("Ingrese el ID de la tarea: "))
        titulo = input("Ingrese el título de la tarea: ")
        descripcion = input("Ingrese la descripción de la tarea: ")
        estado = input("Ingrese el estado de la tarea: ")
        creada = datetime.datetime.now().strftime(FORMATO_FECHA)
        actualizada = datetime.datetime.now().strftime(FORMATO_FECHA)

        tarea = Tarea(tarea_id, titulo, descripcion, estado, creada, actualizada)
        tarea_id = self.admin_tareas.agregar_tarea(tarea)
        print("Tarea agregada con ID:", tarea_id)

    def agregar_varias_tareas(self) -> None:
        num_tareas = int(input("Ingrese el número de tareas a agregar: "))
        tareas = []
        for _ in range(num_tareas):
            tarea_id = int(input("Ingrese el ID de la tarea: "))
            titulo = input("Ingrese el título de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea: ")
            estado = input("Ingrese el estado de la tarea: ")
            creada = datetime.datetime.now().strftime(FORMATO_FECHA)
            actualizada = datetime.datetime.now().strftime(FORMATO_FECHA)

            tarea = Tarea(tarea_id, titulo, descripcion, estado, creada, actualizada)
            tareas.append(tarea)

        tarea_ids = self.admin_tareas.agregar_tareas(tareas)
        print("Tareas agregadas con IDs:", tarea_ids)

    def traer_tarea(self) -> None:
        tarea_id = int(input("Ingrese el ID de la tarea a traer: "))
        tarea = self.admin_tareas.traer_tarea(tarea_id)
        if tarea:
            print("Tarea encontrada:")
            print("ID:", tarea.tarea_id)
            print("Título:", tarea.titulo)
            print("Descripción:", tarea.descripcion)
            print("Estado:", tarea.estado)
            print("Creada:", tarea.creada)
            print("Actualizada:", tarea.actualizada)
        else:
            print("No se encontró la tarea.")

    def actualizar_estado_tarea(self) -> None:
        tarea_id = int(input("Ingrese el ID de la tarea a actualizar: "))
        estado = input("Ingrese el nuevo estado de la tarea: ")
        self.admin_tareas.actualizar_estado_tarea(tarea_id, estado)
        print("Estado de la tarea actualizado.")

    def eliminar_tarea(self) -> None:
        tarea_id = int(input("Ingrese el ID de la tarea a eliminar: "))
        self.admin_tareas.eliminar_tarea(tarea_id)
        print("Tarea eliminada.")

    def traer_todas_tareas(self) -> None:
        tareas = self.admin_tareas.traer_todas_tareas()
        print("Todas las tareas:")
        for tarea in tareas:
            print("ID:", tarea.tarea_id)
            print("Título:", tarea.titulo)
            print("Descripción:", tarea.descripcion)
            print("Estado:", tarea.estado)
            print("Creada:", tarea.creada)
            print("Actualizada:", tarea.actualizada)
            print("---")

    def ejecutar(self) -> None:
        corriendo = True
        while corriendo:
            self.mostrar_menu()
            opcion = input("Ingrese una opción: ")

            if opcion == "1":
                self.agregar_tarea()
            elif opcion == "2":
                self.agregar_varias_tareas()
            elif opcion == "3":
                self.traer_tarea()
            elif opcion == "4":
                self.actualizar_estado_tarea()
            elif opcion == "5":
                self.eliminar_tarea()
            elif opcion == "6":
                self.traer_todas_tareas()
            elif opcion == "7":
                corriendo = False
                self.admin_tareas.cerrar_conexion()
                print("¡Hasta luego!")
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.")


def obtener_ruta_db() -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_file = os.path.join(script_dir, 'tareas_db.json')
    return db_file


if __name__ == "__main__":
    db_file = obtener_ruta_db()
    admin_tareas = AdminTarea()
    interfaz_usuario = InterfazUsuario(admin_tareas)
    interfaz_usuario.ejecutar()
