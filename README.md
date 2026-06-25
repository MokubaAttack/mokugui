# mokugui
I make the module that run in local machine, because I buy intel arc b570.
## requirements
This module depends on only [realersgan](https://github.com/xinntao/Real-ESRGAN/tree/master) and [diffusers-anima](https://github.com/hdae/diffusers-anima).  
Please install the module shown below by yourself, before you install this module.  
- freesimplegui
- compel
- diffusers
- pyperclip
- torch
- torchvision
- piexif
- optimum-quanto

compel depends on transformers ~= 4.25. But it runs transformers == 5.5.4.  
[requirements_xpu.txt](https://github.com/MokubaAttack/mokugui/blob/main/requirements_xpu.txt) is the list of modules that I installed in 2026/05/27 in order to run this module. My Cpu is Ryzen 5 7600, and my Gpu is Intel arc B570.
## GUI Apprications
The codes in Scripts folder are the codes of GUI Apprication. Running the code, the window in order to input parameters is opened. Clicking RUN button after inputting parameters, diffusers is run.
- anima_gui.py  
  the code for anima model
- sdxl_gui.py  
  the code for sd or sdxl model
  If you check low memory, in gpu having 10GB vram you can run this program.
## Credits
- [hdae/diffusers-anima](https://github.com/hdae/diffusers-anima)  
- [xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN/tree/master)  
- [gokayfem/Tile-Upscaler](https://github.com/gokayfem/Tile-Upscaler)  
- [lllyasviel/control_v11f1e_sd15_tile](https://huggingface.co/lllyasviel/control_v11f1e_sd15_tile)  
- [KohakuBlueleaf/LyCORIS](https://github.com/KohakuBlueleaf/LyCORIS)
