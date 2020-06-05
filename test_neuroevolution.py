import manytor as tor
from tqdm import tqdm
import torch.nn as nn
import torch
import time


class Net(nn.Module):
	def __init__(self, obs_size, act_size, hid_size=64):
		super(Net, self).__init__()

		self.mu = nn.Sequential(
			nn.Linear(obs_size, hid_size),
			nn.Tanh(),
			nn.Linear(hid_size, 30),
			nn.Tanh(),
			nn.Linear(30, act_size),
			nn.Tanh(),
		)

	def forward(self, x):
		return self.mu(x)


epochs = 1000
max_steps = 50
obj_number = 10

model = Net(obs_size=obj_number*3, act_size=4)
model.load_state_dict(torch.load('net_complex_multi.pt'))
model.eval()

env = tor.Environment(obj_number)
obs = env.reset(returnable=True)
env.render()
epochs_time = []
rendering = False
epoch = 0
timer = time.time()

for i in range(1, epochs):

	for p in tqdm(range(max_steps)):
		obs_v = torch.FloatTensor([obs])
		action_v = model.forward(obs_v)
		action = action_v[0].detach().numpy()*180
		obs, reward, done = env.step(action)
		if env.is_done():
			time.sleep(1)
			break
		time.sleep(0.1)

	epoch += 1
	print('Total Reward: ', env.total_reward)
	print('Epoch: ', epoch)
	env.reset()

time.sleep(60)
total_time = time.time()-timer
print('Total Time: ', total_time)
print('Time per Epoch: ', epochs_time)
env.render(stop_render=True)
