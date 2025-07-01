# V2Xverse 环境搭建与使用说明

## 测试环境

| CPU      | 13th Gen Intel(R) Core(TM) i9-13900K                         |
| -------- | :----------------------------------------------------------- |
| GPU      | NVIDIA GeForce RTX 4090 (×1)                                 |
| RAM      | 64GB / DDR5 4800MHz (Corsair ×2)                             |
| 硬盘空间 | 1TB NVMe SSD (Samsung 980 PRO) + 500GB NVMe SSD (ZHITAI Ti600) + 3.6TB SATA HDD (ST4000NM0035) |

## 安装步骤

### 1. Conda 环境准备

```shell
cd V2Xverse
conda env create -f v2xfuzz_v2xverse_environment.yml
conda activate v2xfuzz_v2xverse
```

### 2. 安装依赖

```shell
pip install -r v2xfuzz_v2xverse_requirements.txt
```

### 3. 安装 spconv 2.0、FPV-RCNN、点云处理与协同感知模块
- 按照 [V2Xverse Installation](https://github.com/CollaborativePerception/V2Xverse) 官方文档安装
- 确保 spconv 2.0 版本，FPV-RCNN 必须安装
- 安装点云处理、规划与闭环驾驶相关依赖

### 4. 数据集准备
- 数据集较大，需从 [Huggingface](https://huggingface.co/gjliu/v2xverse) 下载
- 按官方说明准备感知和规划模型

### 5. 环境变量加载

```shell
source v2xfuzz_v2xverse_env.sh
```

---

## 参考文档
- [V2Xverse 官方文档](https://github.com/CollaborativePerception/V2Xverse)
- [OpenCOOD 官方文档](https://opencood.readthedocs.io/en/latest/md_files/installation.html)

如需自定义感知、规划等模块，请参考源码及官方文档说明。

