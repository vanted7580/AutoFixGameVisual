# 大家就当这是个ICC共享仓库就行了，我写的程序就图一乐

已解压的文件在 [color](https://github.com/vanted7580/AutoFixGameVisual/tree/main/color) 文件夹。
更多的已压缩的色彩文件在 [compressed](https://github.com/vanted7580/AutoFixGameVisual/tree/main/compressed) 

如果我有什么违反社区规则或者是做得有问题的地方请大家告诉我，我不会使用GitHub（抱歉）。
感谢大家的支持。

## 贡献者 (不分先后)

[<img src="https://avatars.githubusercontent.com/u/81589160" width="30" >](https://github.com/Gannod-Kitkut)  [Gannod-Kitkut](https://github.com/Gannod-Kitkut)  -  [FX507VV](https://github.com/vanted7580/AutoFixGameVisual/discussions/2)

[<img src="https://avatars.githubusercontent.com/u/123755341" width="30" >](https://github.com/syh599)  [syh](https://github.com/syh599)  -  [GA503RM](https://github.com/vanted7580/AutoFixGameVisual/discussions/4)

[<img src="https://avatars.githubusercontent.com/u/120259194" width="30" >](https://github.com/Chen-Mengze)  [Chen-Mengze](https://github.com/Chen-Mengze)  -  [FA507RM](https://github.com/vanted7580/AutoFixGameVisual/discussions/5)   [G614JVR](https://github.com/vanted7580/AutoFixGameVisual/discussions/6)

[<img src="https://avatars.githubusercontent.com/u/46050179" width="30" >](https://github.com/summer-foam)  [Akafusu_Rain](https://github.com/summer-foam)  -  [G733Z/G533Z](https://github.com/vanted7580/AutoFixGameVisual/discussions/8)   [FA506QR](https://github.com/vanted7580/AutoFixGameVisual/discussions/7)


## 以防你不知道怎么确定屏幕的型号

<img src="https://raw.githubusercontent.com/vanted7580/assets/refs/heads/main/AutoFixGameVisual/9C4A9C401BD11ABB47A7B54B8B3BD4E0.png" width="600">

## Auto Fix ROG ArmouryCrate GameVisual
#### 自动修复奥创中心GameVisual

## 说明

此程序用于修复在华硕部分机型更换屏幕后GameVisual无法使用的问题。

- 需要机型自身支持GameVisual，此程序并不会为不支持的机型提供任何支持或者修复功能。
- 原生不支持色域切换的机器可能会增加切换的功能，取决于你的屏幕 (不保证缩限后的色准)

<img src="https://upload.cc/i1/2023/07/22/QZkXHo.png" width="400">

## 帮助改进

此程序的工作原理是通过检测显示器型号，匹配相应的icm文件，并将文件名称修改为主机的型号。

你可以在[这里](https://github.com/vanted7580/AutoFixGameVisual/discussions/new?category=general)提交你的电脑色彩配置文件(打包为Zip)，以帮助其他人。

文件的目录通常在

      C:\ProgramData\ASUS\GameVisual\
      C:\Windows\System32\spool\drivers\color\

文件名称格式是`Model_GPU_Monitor[_CMDEF].icm`，如`GU603ZW_10DE_E5090B74_CMDEF.icm`和`GU603ZW_8086_E5090B74.icm`。

## Potential Problems

#### 潜在面板识别错误


      screen = True if profile.find(monitor_code) != -1 else False

以上代码可能会导致配置文件识别错误

- 由于icm文件中显示器信息的格式是`制造商+显示器代号`，而代码仅仅在这段内容中寻找是否存在同样的显示器代号

- 这意味着如果制`制造商+显示器代号`中有显示器代号相同制造商不同，或者在字符串链接处产生了一个存在的显示器代号，程序将不能正确识别配置文件

(我不会修，因为我没有华硕的命名规则表（（）

## Configurtion
      [GPU_CODE]
      INTEL_IGPU = 8086 #英特尔核显代号
      NVIDIA_GPU = 10DE #英伟达独显代号
      AMD_GPU = #AMD独显代号 未知
      AMD_IGPU = 1002 #AMD核显代号
      
      [SYSTEM_PATH] #目标路径
      GameVisual = C:\ProgramData\ASUS\GameVisual\
      Color = C:\Windows\System32\spool\drivers\color\

## Tested Model

- GU603ZW with E5090B74

## License

[AutoFixGameVisual ]([https://github.com/wqy224491/recoil-control-for-apex/blob/main/VANTED.CC_Recoil_Control_for_Apex.lua](https://github.com/vanted7580/AutoFixGameVisual)) is available for [GPL-3.0 License](https://github.com/vanted7580/AutoFixGameVisual/blob/main/LICENSE) in files.

此项目适用于[GPL-3.0 协议](https://baike.baidu.com/item/GNU%E9%80%9A%E7%94%A8%E5%85%AC%E5%85%B1%E8%AE%B8%E5%8F%AF%E8%AF%81/393832)。

<img src="https://upload.cc/i1/2023/01/01/0nyLFI.png" width="280">
