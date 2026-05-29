import FreeSimpleGUI as sg
import pyperclip
import tkinter as tk
import json
import os

def setvalues():
	iv={
		"pr":"","ne":"",
		"n":"10",
		"st":"32",
		"sa":"DDIM",
		"sc":"",
		"cf":"4",
		"se":"0",
		"ds":"0.4",
		"hu":"1.5",
		"hum":"NEAREST",
		"lora1":"","lora2":"","lora3":"","lora4":"","w1":"1.0","w2":"1.0","w3":"1.0","w4":"1.0",
		"input":"","out":"",
		"dtype":"bf16","dev":"xpu",
		"vae":"","p1":"","p2":"","p3":"","n1":"","n2":"","n3":"",
		"cl":"2","pag":"3.0","pic":""
	}
	if os.path.exists(os.getcwd()+"/tile_default.json"):
		f=open(os.getcwd()+"/tile_default.json","r")
		sd=json.load(f)
		f.close()
		for k in iv:
			if k in sd:
				iv[k]=sd[k]
	return iv

def loadvalues(win):
	f=open(os.getcwd()+"/tile_default.json","r")
	sd=json.load(f)
	f.close()
	iv={
		"pr":"","ne":"",
		"n":"10",
		"st":"32",
		"sa":"DDIM",
		"sc":"",
		"cf":"4",
		"se":"0",
		"ds":"0.4",
		"hu":"1.5",
		"hum":"NEAREST",
		"lora1":"","lora2":"","lora3":"","lora4":"","w1":"1.0","w2":"1.0","w3":"1.0","w4":"1.0",
		"input":"","out":"",
		"dtype":"bf16","dev":"xpu",
		"vae":"","p1":"","p2":"","p3":"","n1":"","n2":"","n3":"",
		"cl":"2","pag":"3.0","pic":""
	}
	for k in iv:
		if k in sd:
			win[k].update(sd[k])
		else:
			win[k].update(iv[k])

def savevalues(vs):
	iv={
		"pr":"","ne":"",
		"n":"10",
		"st":"32",
		"sa":"DDIM",
		"sc":"",
		"cf":"4",
		"se":"0",
		"ds":"0.4",
		"hu":"1.5",
		"hum":"NEAREST",
		"lora1":"","lora2":"","lora3":"","lora4":"","w1":"1.0","w2":"1.0","w3":"1.0","w4":"1.0",
		"input":"","out":"",
		"dtype":"bf16","dev":"xpu",
		"vae":"","p1":"","p2":"","p3":"","n1":"","n2":"","n3":"",
		"cl":"2","pag":"3.0","pic":""
	}
	for k in iv:
		iv[k]=vs[k]
	f=open(os.getcwd()+"/tile_default.json","w")
	json.dump(iv,f)
	f.close()

if __name__=="__main__":
	iv=setvalues()
	if os.path.exists(os.getcwd()+"/tile_default.json"):
		d=False
	else:
		d=True
	
	keys=[
		"input","pr","ne","st","cf","se","n","lora1","lora2","lora3","lora4","w1","w2","w3","w4","hu","hum","ds","sa","sc","out",
		"vae","p1","p2","p3","n1","n2","n3","cl","pag","pic"
	]

	sa_list=[
		"Euler a",
        "Euler",
        "LMS",
        "Heun",
        "DPM2",
        "DPM2 a",
        "DPM++"
        "DPM++ 2M",
        "DPM++ SDE",
        "DPM++ 2M SDE",
        "DPM++ 3M SDE",
        "DDIM",
        "PLMS",
        "UniPC",
        "LCM"
	]
	sc_list=["","Karras","beta","exponential","sgm_uniform","simple"]
	hum_list=["NEAREST","BOX","BILINEAR","HAMMING","BICUBIC","LANCZOS","select file"]

	grp_rclick_menu={}
	for key in keys:
		grp_rclick_menu[key]=[
			"",
			[
				"-copy-::"+key,"-cut-::"+key,"-paste-::"+key
			]
		] 

	col1=[
		[sg.Text("prompt")],
		[sg.Multiline(iv["pr"],size=(50, 5),key="pr",right_click_menu=grp_rclick_menu["pr"])]
	]
	col2=[
		[sg.Text("negative prompt")],
		[sg.Multiline(iv["ne"],size=(50, 5),key="ne",right_click_menu=grp_rclick_menu["ne"])]
	]
	col3=[
		[sg.Text("Steps"), sg.Input(iv["st"],key="st",right_click_menu=grp_rclick_menu["st"], size=(10, 1))],
		[sg.Text("Sampler"), sg.Combo(default_value=iv["sa"],values=sa_list,key="sa")],
		[sg.Text("Schedule type"), sg.Combo(default_value=iv["sc"],values=sc_list,key="sc")],
		[sg.Text("CFG scale"), sg.Input(iv["cf"],key="cf",right_click_menu=grp_rclick_menu["cf"], size=(10, 1))],
		[sg.Text("Clip skip"), sg.Input(iv["cl"],key="cl",right_click_menu=grp_rclick_menu["cl"], size=(10, 1))],
        [sg.Text("PAG scale"), sg.Input(iv["pag"],key="pag",right_click_menu=grp_rclick_menu["pag"], size=(10, 1))],
	]
	col4=[
		[sg.Text("Pic number"), sg.Input(iv["n"],key="n",right_click_menu=grp_rclick_menu["n"], size=(10, 1))],
		[sg.Text("Seed"), sg.Input(iv["se"],key="se",right_click_menu=grp_rclick_menu["se"], size=(20, 1))],
		[sg.Text("Denoising strength"), sg.Input(iv["ds"],key="ds",right_click_menu=grp_rclick_menu["ds"], size=(10, 1))],
		[sg.Text("Tile upscale"), sg.Input(iv["hu"],key="hu",right_click_menu=grp_rclick_menu["hu"], size=(10, 1))],
		[sg.Text("Tile upscaler"), sg.Combo(default_value=iv["hum"],key="hum",values=hum_list,enable_events=True)],
	]
	col5=[
		[sg.Text("positive embedding")],
		[sg.Input(iv["p1"],key="p1",right_click_menu=grp_rclick_menu["p1"]),sg.FilesBrowse(file_types=(('embedding file', '.safetensors'),))],
		[sg.Input(iv["p2"],key="p2",right_click_menu=grp_rclick_menu["p2"]),sg.FilesBrowse(file_types=(('embedding file', '.safetensors'),))],
		[sg.Input(iv["p3"],key="p3",right_click_menu=grp_rclick_menu["p3"]),sg.FilesBrowse(file_types=(('embedding file', '.safetensors'),))],
	]
	col6=[
		[sg.Text("negative embedding")],
		[sg.Input(iv["n1"],key="n1",right_click_menu=grp_rclick_menu["n1"]),sg.FilesBrowse(file_types=(('embedding file', '.safetensors'),))],
		[sg.Input(iv["n2"],key="n2",right_click_menu=grp_rclick_menu["n2"]),sg.FilesBrowse(file_types=(('embedding file', '.safetensors'),))],
		[sg.Input(iv["n3"],key="n3",right_click_menu=grp_rclick_menu["n3"]),sg.FilesBrowse(file_types=(('embedding file', '.safetensors'),))],
	]
	col7=[
		[sg.Button("Save Params",key="save")],
		[sg.Button("Load Params",key="load",disabled=d)],
		[sg.Button('RUN', key='RUN')],
		[sg.Button('EXIT', key='EXIT')]
	]

	layout=[
		[
			sg.Text("image"),
			sg.Input(iv["pic"],key="pic",right_click_menu=grp_rclick_menu["pic"]),sg.FilesBrowse(file_types=(('jpg file', '.jpg'),('jpg file', '.JPG'),('png file', '.png'),('png file', '.PNG'),)),
		],
		[
			sg.Text("ckpt"),
			sg.Input(iv["input"],key="input",right_click_menu=grp_rclick_menu["input"]),sg.FilesBrowse(file_types=(('ckpt file', '.safetensors'),)),
			sg.Text("vae"),
			sg.Input(iv["vae"],key="vae",right_click_menu=grp_rclick_menu["vae"]),sg.FilesBrowse(file_types=(('vae file', '.safetensors'),))
		],
		[
			sg.Text("lora1"),
			sg.Input(iv["lora1"],key="lora1",right_click_menu=grp_rclick_menu["lora1"]),sg.FilesBrowse(file_types=(('lora file', '.safetensors'),)),
			sg.Text("weight"),
			sg.Input(iv["w1"],key="w1",right_click_menu=grp_rclick_menu["w1"], size=(10, 1))
		],
		[
			sg.Text("lora2"),
			sg.Input(iv["lora2"],key="lora2",right_click_menu=grp_rclick_menu["lora2"]),sg.FilesBrowse(file_types=(('lora file', '.safetensors'),)),
			sg.Text("weight"),
			sg.Input(iv["w2"],key="w2",right_click_menu=grp_rclick_menu["w2"], size=(10, 1))
		],
		[
			sg.Text("lora3"),
			sg.Input(iv["lora3"],key="lora3",right_click_menu=grp_rclick_menu["lora3"]),sg.FilesBrowse(file_types=(('lora file', '.safetensors'),)),
			sg.Text("weight"),
			sg.Input(iv["w3"],key="w3",right_click_menu=grp_rclick_menu["w3"], size=(10, 1))
		],
		[
			sg.Text("lora4"),
			sg.Input(iv["lora4"],key="lora4",right_click_menu=grp_rclick_menu["lora4"]),sg.FilesBrowse(file_types=(('lora file', '.safetensors'),)),
			sg.Text("weight"),
			sg.Input(iv["w4"],key="w4",right_click_menu=grp_rclick_menu["w4"], size=(10, 1))
		],
		[sg.Column(col5),sg.Column(col6)],
		[sg.Column(col1),sg.Column(col2)],
		[sg.Column(col3),sg.Column(col4),sg.Column(col7)],
		[
			sg.Text("dtype"), sg.Combo(default_value=iv["dtype"],values=["f32","f16","bf16"],key="dtype"),
			sg.Text("device"), sg.Combo(default_value=iv["dev"],values=["cpu","cuda","mps","xpu"],key="dev")
		],
		[
			sg.Text("output folder"),
			sg.Input(iv["out"],key="out",right_click_menu=grp_rclick_menu["out"]),sg.FolderBrowse()
		]
	]

	window = sg.Window('tile gui', layout)

	while True:
		event, values = window.read()
		if event == sg.WINDOW_CLOSED:
			sd={}
			break
		elif event=="EXIT":
			sd={}
			break
		elif event=="RUN":
			if values["input"]!="" and values["out"]!="":
				sd=values
				break
		elif "-copy-" in event:
			try:
				key=event.replace("-copy-::","")
				selected = window[key].widget.selection_get()
				pyperclip.copy(selected)
			except:
				pass
		elif "-cut-" in event:
			try:
				key=event.replace("-cut-::","")
				selected = window[key].widget.selection_get()
				pyperclip.copy(selected)
				window[key].widget.delete(tk.SEL_FIRST, tk.SEL_LAST)
			except:
				pass
		elif "-paste-" in event:
			try:
				key=event.replace("-paste-::","")
				selected = pyperclip.paste()
				insert_pos = window[key].widget.index("insert")
				window[key].Widget.insert(insert_pos, selected)
				window[key].widget.delete(tk.SEL_FIRST, tk.SEL_LAST)
			except:
				pass
		elif "hum" in event:
			if values["hum"]=="select file":
				value = sg.popup_get_file('upscaler file',file_types=(('upscaler File', '.pth'),))
				if value!=None:
					window["hum"].update(value)
		elif event=="save":
			try:
				savevalues(values)
				window["load"].update(disabled=False)
			except:
				pass
		elif event=="load":
			try:
				loadvalues(window)
			except:
				pass

	window.close()

	if sd!={}:
		import mokugui

		loras=[]
		lora_weights=[]
		for i in range(4):
			if sd["lora"+str(i+1)]!="":
				loras.append(sd["lora"+str(i+1)])
				try:
					lora_weights.append(float(sd["w"+str(i+1)]))
				except:
					lora_weights.append(1.0)

		pos_emb=[]
		neg_emb=[]
		for i in range(3):
			if sd["p"+str(i+1)]!="":
				pos_emb.append(sd["p"+str(i+1)])
			if sd["n"+str(i+1)]!="":
				neg_emb.append(sd["n"+str(i+1)])
		
		try:
			n=int(sd["n"])
		except:
			n=3

		try:
			gs=float(sd["cf"])
		except:
			gs=7

		try:
			step=int(sd["st"])
		except:
			step=30

		try:
			ccs=float(sd["ccs"])
		except:
			ccs=1.0

		try:
			pag=float(sd["pag"])
		except:
			pag=3.0

		try:
			cs=int(sd["cl"])
		except:
			cs=2

		try:
			ss=float(sd["ds"])
		except:
			ss=0.4
		try:
			up=float(sd["hu"])
		except:
			up=1.5
		if sd["hum"]=="NEAREST":
			Interpolation=1
		elif sd["hum"]=="BOX":
			Interpolation=2
		elif sd["hum"]=="BILINEAR":
			Interpolation=3
		elif sd["hum"]=="HAMMING":
			Interpolation=4
		elif sd["hum"]=="BICUBIC":
			Interpolation=5
		elif sd["hum"]=="LANCZOS":
			Interpolation=6
		else:
			Interpolation=sd["hum"]
		
		result=mokugui.mokuup(
			img_path=sd["pic"],
			loras=loras,
			lora_weights=lora_weights,
			prompt = sd["pr"],
			n_prompt = sd["ne"],
			pic_number=n,
			gs=gs,
			sample=sd["sa"],
			sgm=sd["sc"],
			seed=sd["se"],
			out_folder=sd["out"],
			base_safe=sd["input"],
			j_or_p="j",
			url="",
			dtype=sd["dtype"],
			dev=sd["dev"],
			Interpolation=Interpolation,
			step=step,
			ss=ss,
			cs=cs,
			up=up,
			vae_safe=sd["vae"],
			pag=pag,
			pos_emb=pos_emb,
			neg_emb=neg_emb,
			ccs=ccs
			)
		sg.popup(result,title='tile gui')
