---
name: csp-visual-detail
description: 精确检查截图或位图的小字号、1 px 边线、裁切、透明边或前后局部差异；用原图坐标裁切和整数倍像素放大保存证据。不用于图像生成、普通全图描述或桌面操控。
---

# 检查图像局部细节

先保留原图以及尺寸，确认目标元素和坐标空间。页面 CSS 坐标要按同一张截图的缩放、DPR、截取起点和滚动偏移换算成图像像素；比例不确定就用原图定位。记录截图来源、状态、宽高、裁切框和倍率。不要从缩略图猜字、颜色或线宽。

用 [裁切工具](scripts/crop_detail.py) 读取本地单帧图像；需要 Python 和现有 Pillow。坐标按图像像素，从左上角开始，右和下边界不含在内。新建 PNG，不覆盖原图或已有文件：

```powershell
python <本技能目录>/scripts/crop_detail.py <原图> <新输出.png> --box 10 20 60 42 --scale 4
```

看全图定位，再看裁切。比对两张截图时对齐状态、视口、字体、DPR 和对应元素；若元素有位移，分别确定框并记录。整数倍最近邻只负责展示源像素；保留缩放细节和原图，必要时给出数值或真实交互作交叉证据。读不清时报告具体不确定处，取更清晰的原始截图；不要把插值或 OCR 当原图证据。

来源：MIT 仓库 [image-detail-inspect](https://github.com/liushikuan63/Qoder-Optimization/tree/fe929cf1de22d4312b9526536568161d2a674439/skills/image-detail-inspect)。只提炼本地裁切和像素证据，工具按本机环境独立实现。
