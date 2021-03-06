import numpy as np

exp_name = 'dashcam_ft_exp1'
dataset_name = 'dashcam'
pretrained_fname = '/home/cory/yolo2-pytorch/models/yolo-voc.weights.h5'

network_size_rand_period = 10
inp_size_candidates = [(640, 320), (736, 384), (960, 480), (1024, 544)]
# inp_size = np.array([1280, 736], dtype=np.int)   # w, h
inp_size = np.array([640, 320], dtype=np.int)   # w, h
out_size = inp_size / 32


optimizer = 'SGD'  # 'SGD, Adam'
opt_param = 'all'  # 'all, conv345'

start_step = 0
lr_epoch = (0, 60)
lr_val = (1E-5, 1E-6)

max_epoch = 200

# SGD only
weight_decay = 0.0005
momentum = 0.9

# for training yolo2
object_scale = 5.
noobject_scale = 1.
class_scale = 1.
coord_scale = 1.
iou_thresh = 0.6

# dataset
imdb_train = 'voc_2012_trainval'
imdb_test = 'voc_2007_test'
train_images = '/home/cory/yolo2-pytorch/train_data/dashcam_train_images.txt'
train_labels = '/home/cory/yolo2-pytorch/train_data/dashcam_train_labels.txt'
val_images = '/home/cory/yolo2-pytorch/train_data/dashcam_val_images.txt'
val_labels = '/home/cory/yolo2-pytorch/train_data/dashcam_val_labels.txt'
batch_size = 8
train_batch_size = 8
