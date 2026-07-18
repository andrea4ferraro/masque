from repository import Repository

from notebook import Notebook

from printer import show

from search import Search

repository = Repository()

notebook = Notebook(

    repository.load()

)

results = Search().keyword(

    notebook.all(),

    ""

)

show(

    results

)
