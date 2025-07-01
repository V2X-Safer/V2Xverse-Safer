#!/bin/fish

set -gx CARLA_HOME /home/test/V2X/OpenCDA/V2Xverse/carla
set -gx CARLA_ROOT /home/test/V2X/OpenCDA/V2Xverse/carla
set -gx CARLA_VERSION 0.9.10
set -gx SUMO_HOME /usr/share/sumo
set -gx PATH $PATH /opt/nvim-linux-x86_64/bin
set -gx PATH $PATH /home/test/go/bin
set -gx MESA_GL_VERSION_OVERRIDE 3.3
set -gx SCENARIO_RUNNER_ROOT /home/test/V2X/OpenCDA/V2Xverse/simulation/scenario_runner/
set -gx PYTHONPATH $SCENARIO_RUNNER_ROOT
set -gx PYTHONPATH $PYTHONPATH:$CARLA_ROOT/PythonAPI/carla/dist/carla-0.9.10-py3.7-linux-x86_64.egg
set -gx PYTHONPATH $PYTHONPATH:$CARLA_ROOT/PythonAPI/carla
