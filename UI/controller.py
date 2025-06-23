import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):
        self._model.buildGraph()
        numNodi, numArchi = self._model.getNumeriGrafo()
        self._view.txt_result.clean()
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato correttamente:"))
        self._view.txt_result.controls.append(ft.Text(f"Numero nodi: {numNodi}. Numero archi: {numArchi}"))
        self._view._btnCompConnessa.disabled = False
        self._view.update_page()

    def handleCompConnessa(self,e):
        obj = self._view._txtIdOggetto.value
        try:
            int(obj)
        except ValueError:
            self._view.txt_result.clean()
            self._view.txt_result.controls.append(ft.Text(f"Inserire l'id numerico di un oggetto"))
            self._view.update_page()
            return
        compConn = self._model.getCompConn(obj)
        self._view.txt_result.clean()
        self._view.txt_result.controls.append(ft.Text(f"la componente connessa è lunga: {len(compConn)}"))
        for el in compConn:
            self._view.txt_result.controls.append(ft.Text(f"{el.object_id}"))
        self._view.update_page()


    def handleCerca(self, e):
        pass
