try:
	from .workflow import (
		mokucola,
		mokuup,
		mokuani
	)
	from .dl import (
		dlc,
		dlk
	)

	path=__file__.replace("\\","/")
	f=open(path,"w")
	f.write("from .workflow import (\n")
	f.write("	mokucola,\n")
	f.write("	mokuup,\n")
	f.write("	mokuani\n")
	f.write(")\n")
	f.write("from .dl import (\n")
	f.write("	dlc,\n")
	f.write("	dlk\n")
	f.write(")\n")
	f.close()

except:
	path=__file__.replace("\\","/")
	path3=path.replace("mokucola/__init__.py","basicsr/data/degradations.py")
	f=open(path3,"r")
	data=[]
	for line in f:
		if "from torchvision.transforms.functional_tensor import rgb_to_grayscale" in line:
			line=line.replace(
				"from torchvision.transforms.functional_tensor import rgb_to_grayscale",
				"from torchvision.transforms.functional import rgb_to_grayscale"
				)
		data+=[line]
	f.close()
	f=open(path3,"w")
	for line in data:
		f.write(line)
	f.close()

	import requests

	path1=path.replace("mokucola/__init__.py","diffusers_anima")+"/loaders/lora_pipeline.py"
	url1="https://raw.githubusercontent.com/MokubaAttack/scripts_anima/refs/heads/main/lora_pipeline.py"
	response = requests.get(url1)
	with open(path1, 'wb') as f:
		f.write(response.content)

	path2=path.replace("mokucola/__init__.py","diffusers_anima")+"/pipelines/anima/loading.py"
	url2="https://raw.githubusercontent.com/MokubaAttack/scripts_anima/refs/heads/main/loading.py"
	response = requests.get(url2)
	with open(path2, 'wb') as f:
		f.write(response.content)

	from .workflow import (
		mokucola,
		mokuup,
		mokuani
	)
	from .dl import (
		dlc,
		dlk
	)

	path=__file__.replace("\\","/")
	f=open(path,"w")
	f.write("from .workflow import (\n")
	f.write("	mokucola,\n")
	f.write("	mokuup,\n")
	f.write("	mokuani\n")
	f.write(")\n")
	f.write("from .dl import (\n")
	f.write("	dlc,\n")
	f.write("	dlk\n")
	f.write(")\n")
	f.close()
