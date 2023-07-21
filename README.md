# Auto Fix ROG ArmouryCrate GameVisual
#### 自动修复奥创中心GameVisual

## 说明

此程序的工作原理是通过检测显示器型号，匹配相应的icm文件，并将文件名称修改为主机的型号。

你可以在[这里](https://github.com/vanted7580/AutoFixGameVisual/discussions/new?category=general)提交你的电脑色彩配置文件(打包为Zip)，以帮助其他人。

文件的目录通常在

      C:\ProgramData\ASUS\GameVisual\
      C:\Windows\System32\spool\drivers\color\

文件名称格式是`Model_GPU_Monitor[_CMDEF].icm`，如`GU603ZW_10DE_E5090B74_CMDEF.icm`和`GU603ZW_8086_E5090B74.icm`。

## Configurtion
      [GPU_CODE]
      INTEL_IGPU = 8086 #英特尔核显代号
      NVIDIA_GPU = 10DE #英伟达独显代号
      AMD_GPU = #AMD独显代号 未知
      AMD_IGPU = 1002 #AMD核显代号
      
      [SYSTEM_PATH] #目标路径
      GameVisual = C:\ProgramData\ASUS\GameVisual\
      Color = C:\Windows\System32\spool\drivers\color\

## License

[AutoFixGameVisual ]([https://github.com/wqy224491/recoil-control-for-apex/blob/main/VANTED.CC_Recoil_Control_for_Apex.lua](https://github.com/vanted7580/AutoFixGameVisual)) is available for [GPL-3.0 License](https://github.com/vanted7580/AutoFixGameVisual/blob/main/LICENSE) in files.

此脚本适用于[GPL-3.0 协议](https://baike.baidu.com/item/GNU%E9%80%9A%E7%94%A8%E5%85%AC%E5%85%B1%E8%AE%B8%E5%8F%AF%E8%AF%81/393832)。

<img src="https://upload.cc/i1/2023/01/01/0nyLFI.png" width="280">
