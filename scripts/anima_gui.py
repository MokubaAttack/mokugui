import FreeSimpleGUI as sg
import pyperclip
import tkinter as tk

if __name__=="__main__":
	keys=[
		"input","pr","ne","st","cf","se","n","x","y","lora1","lora2","lora3","lora4","w1","w2","w3","w4","hu","hs","hum","ds","sa","sc","out"
	]

	sa_list=["flowmatch_euler","euler","euler_a_rf","euler_ancestral_rf"]
	sc_list=["uniform","beta","simple","normal"]
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
		[sg.Multiline(size=(50, 5),key="pr",right_click_menu=grp_rclick_menu["pr"])]
	]
	col2=[
		[sg.Text("negative prompt")],
		[sg.Multiline(size=(50, 5),key="ne",right_click_menu=grp_rclick_menu["ne"])]
	]
	col3=[
		[sg.Text("Pic number"), sg.Input("10",key="n",right_click_menu=grp_rclick_menu["n"], size=(10, 1))],
		[sg.Text("Steps"), sg.Input("32",key="st",right_click_menu=grp_rclick_menu["st"], size=(10, 1))],
		[sg.Text("Sampler"), sg.Combo(default_value="flowmatch_euler",values=sa_list,key="sa")],
		[sg.Text("Schedule type"), sg.Combo(default_value="uniform",values=sc_list,key="sc")],
		[sg.Text("CFG scale"), sg.Input("4",key="cf",right_click_menu=grp_rclick_menu["cf"], size=(10, 1))],
		[sg.Text("Seed"), sg.Input("0",key="se",right_click_menu=grp_rclick_menu["se"], size=(20, 1))],
	]
	col4=[
		[sg.Text("width"), sg.Input("896",key="x",right_click_menu=grp_rclick_menu["x"], size=(10, 1))],
		[sg.Text("height"), sg.Input("1152",key="y",right_click_menu=grp_rclick_menu["y"], size=(10, 1))],
		[sg.Text("Denoising strength"), sg.Input("0.4",key="ds",right_click_menu=grp_rclick_menu["ds"], size=(10, 1))],
		[sg.Text("Hires upscale"), sg.Input("1.5",key="hu",right_click_menu=grp_rclick_menu["hu"], size=(10, 1))],
		[sg.Text("Hires steps"), sg.Input("16",key="hs",right_click_menu=grp_rclick_menu["hs"], size=(10, 1))],
		[sg.Text("Hires upscaler"), sg.Combo(default_value="NEAREST",key="hum",values=hum_list,enable_events=True)],
	]

	layout=[
		[
			sg.Text("ckpt"),
			sg.Input(key="input",right_click_menu=grp_rclick_menu["input"]),sg.FilesBrowse(file_types=(('ckpt file', '.safetensors'),))
		],
		[
			sg.Text("lora1"),
			sg.Input(key="lora1",right_click_menu=grp_rclick_menu["lora1"]),sg.FilesBrowse(file_types=(('lora file', '.safetensors'),)),
			sg.Text("weight"),
			sg.Input("1.0",key="w1",right_click_menu=grp_rclick_menu["w1"], size=(10, 1))
		],
		[
			sg.Text("lora2"),
			sg.Input(key="lora2",right_click_menu=grp_rclick_menu["lora2"]),sg.FilesBrowse(file_types=(('lora file', '.safetensors'),)),
			sg.Text("weight"),
			sg.Input("1.0",key="w2",right_click_menu=grp_rclick_menu["w2"], size=(10, 1))
		],
		[
			sg.Text("lora3"),
			sg.Input(key="lora3",right_click_menu=grp_rclick_menu["lora3"]),sg.FilesBrowse(file_types=(('lora file', '.safetensors'),)),
			sg.Text("weight"),
			sg.Input("1.0",key="w3",right_click_menu=grp_rclick_menu["w3"], size=(10, 1))
		],
		[
			sg.Text("lora4"),
			sg.Input(key="lora4",right_click_menu=grp_rclick_menu["lora4"]),sg.FilesBrowse(file_types=(('lora file', '.safetensors'),)),
			sg.Text("weight"),
			sg.Input("1.0",key="w4",right_click_menu=grp_rclick_menu["w4"], size=(10, 1))
		],
		[sg.Column(col1),sg.Column(col2)],
		[sg.Column(col3),sg.Column(col4)],
		[
			sg.Text("dtype"), sg.Combo(default_value="bf16",values=["f32","f16","bf16"],key="dtype"),
			sg.Text("device"), sg.Combo(default_value="xpu",values=["cpu","cuda","mps","xpu"],key="dev")
		],
		[
			sg.Text("output folder"),
			sg.Input(key="out",right_click_menu=grp_rclick_menu["out"]),sg.FolderBrowse()
		],
		[sg.Button('RUN', key='RUN'),sg.Button('EXIT', key='EXIT')]
	]

	window = sg.Window('anima gui', layout)

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
		
		try:
			n=int(sd["n"])
		except:
			n=10

		try:
			gs=float(sd["cf"])
		except:
			gs=4

		try:
			step=int(sd["st"])
		except:
			step=32

		try:
			x=int(sd["x"])
		except:
			x=1024
		try:
			y=int(sd["y"])
		except:
			y=1024

		if sd["ds"]=="" or sd["hu"]=="" or sd["hum"]=="" or sd["hs"]=="":
			mode=0
			ss=0.4
			Interpolation=3
			step2=16
			up=1.5
		else:
			mode=1
			try:
				ss=float(sd["ds"])
			except:
				ss=0.4
			try:
				up=float(sd["hu"])
			except:
				up=1.5
			try:
				step2=int(sd["hs"])
			except:
				step2=16
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
		
		result=mokugui.mokuani(
			loras=loras,
			lora_weights=lora_weights,
			prompt = sd["pr"],
			n_prompt = sd["ne"],
			pic_number=n,
			gs=gs,
			step=step,
			sample=sd["sa"],
			sgm=sd["sc"],
			seed=sd["se"],
			out_folder=sd["out"],
			base_safe=sd["input"],
			j_or_p="j",
			url="",
			dtype=sd["dtype"],
			dev=sd["dev"],
			x=x,
			y=y,
			mode=mode,
			up=up,
			Interpolation=Interpolation,
			step2=step2,
			ss=ss
			)
		sg.popup(result,title='anima gui')
