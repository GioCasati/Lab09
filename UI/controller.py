import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_analizza(self, e):
        x = self._view.txt_distanza.value
        if not x:
            self._view.create_alert("Inserire la distanza minima")
            return
        try:
            dist = int(x)
        except ValueError:
            self._view.create_alert("Inserire un numero intero come distanza minima")
            return
        self._view.btn_analizza.disabled = True
        self._view.update_page()
        n, e =self._model._build_graph(dist)
        self._view.lst_result.controls.clear()
        self._view.lst_result.controls.append(ft.Text("Grafo correttamente creato!"))
        self._view.lst_result.controls.append(ft.Text(f"Il grafo contiene {n} nodi."))
        self._view.lst_result.controls.append(ft.Text(f"Il grafo contiene {e} archi."))
        for source, target, data in self._model._get_graph_edges():
            self._view.lst_result.controls.append(
                ft.Text(f"{source} --> {target}, distanza: {data['weight']}"))
        self._view.btn_analizza.disabled = False
        self._view.update_page()
