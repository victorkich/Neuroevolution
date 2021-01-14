
<h1 align="center">Using the Neuroevolution to solve the problem of inverse kinematics and manipulation on tri-dimentional environment ManyTor.</h1>

<p align="center"> 
  <img src="https://img.shields.io/badge/Vispy-v0.6.4-blue"/>
  <img src="https://img.shields.io/badge/Numpy-v1.18.2-blue"/>
  <img src="https://img.shields.io/badge/Tqdm-v4.42.1-blue"/>
  <img src="https://img.shields.io/badge/Pandas-v1.1.2-blue"/>
  <img src="https://img.shields.io/badge/PyTorch-v1.6.0-blue"/>
</p>
<br/>

## Environment
<p align="justify"> 
  <img src="https://i.imgur.com/IyulesQ.png" alt="Neuroevolution" align="right" width="320">
  <a>The purpose of this project is to test even in a superficial way the functioning of the junction of neural networks with genetic algorithms, the black box algorithms known as neuroevolution. To accomplish this I am using the environment created by myself, ManyTor, using the high performance graphics tool Vispy based on OpenGL. The manipulator arm used has the denavit hertemberg parameters shown in the frame found on the right.</a>  
</p>
  
  
## Setup
<p align="justify"> 
 <a>To clone this repository execute the following line of code:</a>
</p>

```shell
git clone https://github.com/victorkich/Neuroevolution --recursive
```

<p align="justify"> 
 <a>All of requirements is show in the badgets above, but if you want to install all of them, enter the repository and execute the following line of code:</a>
</p>

```shell
pip3 install -r requirements.txt
```

## Objectives
<p align="justify"> 
  The objectives present in this environment are described in ManyTor's documentation, but in summary, the manipulator arm should take as many green balls as possible in a pre-determined number of actions, in this case I am using 50 actions.
</p>

<p align="center"> 
  <img src="media/neuroevolution.gif" alt="Neuroevolution"/>
</p>  

<p align="center"> 
  <i>If you liked this repository, please don't forget to starred it!</i>
  <img src="https://img.shields.io/github/stars/victorkich/Neuroevolution?style=social"/>
</p>
