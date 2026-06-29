import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._min_rating = None
        self._max_rating = None

    def fillDDsRating(self, dd: ft.Dropdown()):
        ratings = self._model.getAllRating()

        if dd == self._view._ddrating1:
            for r in ratings:
                dd.options.append(ft.dropdown.Option(text=r.rating,
                                                     data=r,
                                                     on_click=self.read_Rating_partenza))
        elif dd == self._view._ddrating2:
            for r in ratings:
                dd.options.append(ft.dropdown.Option(text=r.rating,
                                                     data=r,
                                                     on_click=self.read_Rating_Arrivo))
    def read_Rating_partenza(self, e):
        if e.control.data is None:
            self._min_rating = None
        else:
            self._min_rating = e.control.data.rating

    def read_Rating_Arrivo(self, e):
        print("Voto called ")
        if e.control.data is None:
            self._max_rating = None
        else:
            self._max_rating = e.control.data.rating


    def handleCreaGrafo(self, e):
        self._view.txt_result.controls.clear()

        if self._min_rating is None or self._max_rating is None:
            self._view.txt_result.controls.append(ft.Text("Seleziona entrambi i valori"))
            self._view.update_page()
            return

        minimo = min(self._min_rating,self._max_rating)
        massimo = max(self._min_rating,self._max_rating)
        self._model.buildGraphPesato(minimo,massimo)

        self._view.txt_result.controls.append(ft.Text(f"creato grafico ha {self._model.getNumNodi()} nodi"))
        self._view.txt_result.controls.append(ft.Text(f"creato grafico ha {self._model.getNumArchi()} archi"))
        self._view.update_page()




    def handleCammino(self, e):
            pass