from pathlib import Path


def genfiles(file:Path):
    file.parent.mkdir(exist_ok=True, parents=True)
    file.write_text(f'{file.name} generate!')
    return True



def gen_model(modelfile: str|Path):
    file = Path(modelfile)
    return genfiles(file)


def gen_info(namefile: str|Path):
    file = Path(namefile)
    return genfiles(file)


