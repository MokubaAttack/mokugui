try:
	from .workflow import (
		mokucola,
		mokuup,
		mokuani,
		mokusp
	)

	path=__file__
	f=open(path,"w")
	f.write("from .workflow import (\n")
	f.write("	mokucola,\n")
	f.write("	mokuup,\n")
	f.write("	mokuani,\n")
	f.write("	mokusp\n")
	f.write(")\n")
	f.close()

except:
	import os
	path=os.path.dirname(__file__).removesuffix("mokugui")
	path3=path+"basicsr/data/degradations.py"
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

	path1=path+"diffusers_anima/loaders/lora_pipeline.py"
	url1="https://raw.githubusercontent.com/MokubaAttack/scripts_anima/refs/heads/main/lora_pipeline.py"
	response = requests.get(url1)
	with open(path1, 'wb') as f:
		f.write(response.content)

	path2=path+"diffusers_anima/pipelines/anima/loading.py"
	url2="https://raw.githubusercontent.com/MokubaAttack/scripts_anima/refs/heads/main/loading.py"
	response = requests.get(url2)
	with open(path2, 'wb') as f:
		f.write(response.content)

	from .workflow import (
		mokucola,
		mokuup,
		mokuani,
		mokusp
	)

	path=__file__
	f=open(path,"w")
	f.write("from .workflow import (\n")
	f.write("	mokucola,\n")
	f.write("	mokuup,\n")
	f.write("	mokuani,\n")
	f.write("	mokusp\n")
	f.write(")\n")
	f.close()