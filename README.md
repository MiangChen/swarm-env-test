# swarm-env-test
based on genesis；focus on multi agent robotics task

## Initialization
create conda environment
```
conda create -n swarm_env_312 python=3.12
conda activate swarm_env_312
```


Manually install PyTorch first following the official instructions.
```
https://pytorch.org/get-started/locally/
```

Install other packages
```
pip install -r requirements.txt --timeout=120
```
> 这里有一个问题，genesis使用pip安装还是要哪个git clone的方式安装;发现使用pip安装缺少examples，并且运行起来有一些bug，比如视频无法保存？
> 使用git clone再pip安装的话，记得右键Genesis，然后Make Directory as Source ，（pycharm），可以避免import 报错

## Running


## Customization

