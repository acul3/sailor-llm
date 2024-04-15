from mmengine.config import read_base

with read_base():
    from .datasets.tydiqa_id.tydiqa_id_346aa7 import tydiqa_datasets as tydiqa_id

    from .datasets.xcopa.xcopa_id_ppl_49je23 import xcopa_datasets as xcopa_id_ppl

    from .datasets.m3exam.m3exam_jv_ppl_4fs13f import m3exam_datasets as m3exam_id_ppl

    from .datasets.belebele.belebele_id_ppl_23f2d2 import belebele_datasets as belebele_id_ppl


    from .models.sailor.sailor_4b import models as sailor_4b

    from .models.sailor_baselines.bahasa_4b import models as bahasa_4b


datasets = [*tydiqa_id]
datasets += [*xcopa_id_ppl]
datasets += [*m3exam_id_ppl]
datasets += [*belebele_id_ppl]

models = sailor_4b + bahasa_4b
