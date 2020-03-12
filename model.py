import kfserving
from typing import List, Dict


class KFServingSampleModel(kfserving.KFModel):
    def __init__(self, name: str):
        super().__init__(name)
        self.name = name
        self.ready = False

    def load(self):
        print("load...")
        self.ready = True

    def predict(self, request: Dict) -> Dict:

        print("sdfs:" + str(request))
        return {"predictions": "result"}


if __name__ == "__main__":
    model = KFServingSampleModel("kfserving-demo")
    model.load()
    kfserving.KFServer(workers=2).start([model])