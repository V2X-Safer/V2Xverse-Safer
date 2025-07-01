# V2Xverse 多车V2X通信仿真环境搭建与运行教程

## 📋 目录
1. [环境依赖概述](#环境依赖概述)
2. [环境搭建步骤](#环境搭建步骤)
3. [多车V2X仿真配置](#多车v2x仿真配置)
4. [运行与调试](#运行与调试)
5. [常见问题解决](#常见问题解决)

## 🔧 环境依赖概述

V2Xverse是一个复杂的多车协作自动驾驶仿真平台，主要依赖包括：

### 核心组件
- **Python 3.7+**: 主要编程语言
- **PyTorch 1.10.2**: 深度学习框架  
- **CARLA 0.9.13**: 自动驾驶仿真器
- **OpenCOOD**: 协作感知框架
- **CoDriving**: 协作驾驶模块

### 关键功能模块
- **V2X通信**: 车辆间通信协议实现
- **多车协作**: 多智能体协作决策
- **感知融合**: 多车感知信息融合
- **路径规划**: 协作式路径规划

## 🚀 环境搭建步骤

### Step 1: 创建Conda环境

```bash
# 使用提供的environment.yml文件创建环境
conda env create -f v2xfuzz_v2xverse_environment.yml

# 或手动创建环境
conda create -n v2xfuzz_v2xverse python=3.7
conda activate v2xfuzz_v2xverse
```

### Step 2: 安装PyTorch (CUDA支持)

```bash
conda activate v2xfuzz_v2xverse
conda install pytorch==1.10.2 torchvision==0.11.3 torchaudio==0.10.2 cudatoolkit=11.3 -c pytorch
```

### Step 3: 安装基础依赖

```bash
# 安装requirements文件中的依赖
pip install -r v2xfuzz_v2xverse_requirements.txt
```

### Step 4: 安装特殊依赖（手动安装）

```bash
# 1. 安装SpConv (稀疏卷积，用于点云处理)
pip install spconv-cu113==2.1.25

# 2. 安装PyTorch Geometric相关包
pip install torch-scatter torch-sparse torch-cluster torch-spline-conv torch-geometric -f https://data.pyg.org/whl/torch-1.10.0+cu113.html

# 3. 验证CARLA安装
python -c "import carla; print('CARLA imported successfully')"
```

### Step 5: 设置自定义模块

```bash
# 进入V2Xverse根目录
cd /home/test/V2X/OpenCDA/V2Xverse

# 安装OpenCOOD模块
cd opencood
python setup.py develop
cd ..

# 安装CoDriving模块  
cd codriving
pip install -e .
cd ..

# 验证安装
python -c "import opencood; import codriving; print('Custom modules imported successfully')"
```

### Step 6: 配置CARLA路径

```bash
# 设置CARLA路径环境变量
echo 'export CARLA_ROOT="/home/test/V2X/OpenCDA/V2Xverse/carla"' >> ~/.bashrc
echo 'export PYTHONPATH="${CARLA_ROOT}/PythonAPI/carla/dist/carla-0.9.13-py3.7-linux-x86_64.egg:${PYTHONPATH}"' >> ~/.bashrc
source ~/.bashrc

# 或在external_paths目录设置
echo "/home/test/V2X/OpenCDA/V2Xverse/carla" > external_paths/carla_root
```

## 🚗 多车V2X仿真配置

### 配置文件结构
```
simulation/leaderboard/
├── leaderboard/scenarios/
│   └── scenario_parameter_1.yaml    # 场景参数配置
├── team_code/
│   └── pnp_infer_action_e2e.py      # 智能体行为逻辑
└── .vscode/launch.json              # 调试配置
```

### 多车场景配置 (scenario_parameter_1.yaml)

```yaml
# 关键配置参数
scenarios:
  - scene: "Scenario1"
    ego_num: 2                    # 设置ego车辆数量为2
    max_cav_num: 5               # 最大协作车辆数
    communication_range: 70.0     # V2X通信范围(米)
    proportion: 1.0              # 该场景的使用比例 (1.0=100%使用)
    
  - scene: "Scenario2" 
    ego_num: 2
    max_cav_num: 3
    communication_range: 50.0
    proportion: 0.0              # 0.0=不使用该场景
```

### 智能体配置要点

1. **通信配置**: 确保 `communication_range` 覆盖车辆间距
2. **车辆数量**: `ego_num=2` 启用双车协作
3. **场景选择**: 通过 `proportion` 控制场景使用
4. **协作模式**: 在 `team_code/pnp_infer_action_e2e.py` 中配置协作逻辑

## 🎮 运行与调试

### 方法1: VS Code调试模式

在VS Code中使用已配置的调试选项：

1. 打开 `.vscode/launch.json`
2. 选择 **"Eval Debug with 2 Ego Vehicles"** 配置
3. 按F5启动调试

调试配置详情：
```json
{
    "name": "Eval Debug with 2 Ego Vehicles",
    "type": "python",
    "request": "launch",
    "program": "${workspaceFolder}/simulation/leaderboard/leaderboard/leaderboard_evaluator_local.py",
    "args": [
        "--routes=${workspaceFolder}/simulation/leaderboard/data/longest6/longest6.xml",
        "--scenarios=${workspaceFolder}/simulation/leaderboard/leaderboard/scenarios/scenario_parameter_1.yaml",
        "--agent=${workspaceFolder}/simulation/leaderboard/team_code/pnp_infer_action_e2e.py",
        "--agent-config=${workspaceFolder}/simulation/leaderboard/team_code/interfuser_config.py",
        "--track=SENSORS",
        "--checkpoint=${workspaceFolder}/results/results_driving_debug",
        "--ego_num=2",
        "--debug=1"
    ]
}
```

### 方法2: 命令行运行

```bash
# 进入仿真目录
cd /home/test/V2X/OpenCDA/V2Xverse/simulation/leaderboard

# 启动多车V2X仿真
python leaderboard/leaderboard_evaluator_local.py \
    --routes=data/longest6/longest6.xml \
    --scenarios=leaderboard/scenarios/scenario_parameter_1.yaml \
    --agent=team_code/pnp_infer_action_e2e.py \
    --agent-config=team_code/interfuser_config.py \
    --track=SENSORS \
    --checkpoint=../../results/results_driving_debug \
    --ego_num=2 \
    --debug=1
```

### 方法3: 后台运行脚本

```bash
# 创建运行脚本
cat > run_multi_ego_v2x.sh << EOF
#!/bin/bash
cd /home/test/V2X/OpenCDA/V2Xverse/simulation/leaderboard

python leaderboard/leaderboard_evaluator_local.py \\
    --routes=data/longest6/longest6.xml \\
    --scenarios=leaderboard/scenarios/scenario_parameter_1.yaml \\
    --agent=team_code/pnp_infer_action_e2e.py \\
    --agent-config=team_code/interfuser_config.py \\
    --track=SENSORS \\
    --checkpoint=../../results/results_driving_codriving \\
    --ego_num=2 \\
    --debug=0
EOF

chmod +x run_multi_ego_v2x.sh
./run_multi_ego_v2x.sh
```

## 📊 结果分析

### 结果文件位置
```
results/results_driving_codriving/v2x_final/
├── town05_short_collab/
│   ├── r0_repeat0/
│   │   ├── ego_vehicle_0/
│   │   │   └── results.json    # 第一辆ego车结果
│   │   └── ego_vehicle_1/
│   │       └── results.json    # 第二辆ego车结果
│   └── summary_results.json    # 整体结果汇总
```

### 关键评价指标

```json
{
    "score_composed": 85.23,      // 综合得分 (0-100)
    "score_penalty": 5.15,       // 惩罚得分 (碰撞、违规等)
    "score_route": 90.38,        // 路径完成度得分
    "collisions_layout": 0,      // 静态障碍物碰撞
    "collisions_pedestrian": 0,  // 行人碰撞  
    "collisions_vehicle": 1,     // 车辆碰撞
    "route_completed": 95.5      // 路径完成百分比
}
```

## 🔍 常见问题解决

### 1. CARLA连接问题
```bash
# 确保CARLA服务器启动
cd /home/test/V2X/OpenCDA/V2Xverse/carla
./CarlaUE4.sh -world-port=2000 -resx=800 -resy=600

# 检查端口占用
netstat -tulpn | grep :2000
```

### 2. SpConv安装失败
```bash
# 重新安装SpConv
pip uninstall spconv-cu113
pip install spconv-cu113==2.1.25 --no-cache-dir

# 或使用conda-forge
conda install -c conda-forge spconv
```

### 3. 内存不足
```bash
# 监控内存使用
free -h
htop

# 减少并行车辆数或降低仿真分辨率
# 在配置文件中设置: max_cav_num: 3
```

### 4. GPU显存不足
```bash
# 检查GPU使用情况
nvidia-smi

# 在PyTorch中限制GPU内存
export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:512
```

### 5. 占用栅格图索引错误
```python
# 在代码中添加边界检查
if i >= 0 and i < occ_map.shape[0] and j >= 0 and j < occ_map.shape[1]:
    value = occ_map[i, j]
else:
    print(f"Index out of bounds: i={i}, j={j}, shape={occ_map.shape}")
```

## 📝 日志与监控

### 启用详细日志
```bash
export PYTHONPATH="${PYTHONPATH}:/home/test/V2X/OpenCDA/V2Xverse"
export CUDA_VISIBLE_DEVICES=0
python -u simulation/leaderboard/leaderboard/leaderboard_evaluator_local.py \
    --debug=1 \
    --ego_num=2 2>&1 | tee simulation_log.txt
```

### 性能监控
```bash
# 安装监控工具
pip install psutil gpustat

# 实时监控脚本
watch -n 1 'gpustat && echo "---" && free -h'
```

---

## 📞 技术支持

如遇到问题，可以：
1. 查看 `simulation_log.txt` 日志文件
2. 检查 `results/` 目录下的结果文件
3. 验证环境变量和依赖安装
4. 参考 `doc/` 目录下的详细文档

**环境验证命令：**
```bash
python -c "
import torch; print(f'PyTorch: {torch.__version__}')
import carla; print(f'CARLA: {carla.__version__}')  
import opencood; print('OpenCOOD: OK')
import codriving; print('CoDriving: OK')
print('✅ 环境验证通过！')
"
```
