# install nemo [link](https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/stable/starthere/best-practices.html) 

- need apt `libsndfile1` and `ffmpeg`
- pip install `Cython` and `nemo_toolkit[all]`

# Pytorch Lightning and Hydra

- [git lightning](https://github.com/Lightning-AI/lightning)
- [git hydra](https://github.com/facebookresearch/hydra)
- easy and performant multi-GPU/multi-node mixed precision training.
- PyTorch wrapper: organizes PyTorch code, scales model trainig, and reduces boilerplate.
- 2 main modules: 
  - `LightningModule` organizes Pytorch code so that DL experiments can be easily understood and REPRODUCED.
  - the `Trainer` is able to take the LightningModule and AUTOMATE everything needed for DL training.
- Nemo models are LightningModules that come equipped with all supporting infrastructure for training and reproducibility. This includes the DL model architecture, data preprocessing, optimizer, check-pointing and experiment logging.
- Nemo uses `Hydra` for configuring both Nemo models and the PyTorch Lightning Trainer.
- `Hydra` is a flexible solution that makes it easy to configure all the Python libraries involved in the end-to-end solution from a configuration file or from the CLI.

# ASR guidance

- Way to add domain specific vocabulary in Nemo: Quartznet and Jasper models are character-based. So pretrained models for these 2 output lowercase English letters and '. Users can retrain them on uppercase letters and punctuation symboles.
- library to convert numbers into words. [inflect](https://pypi.org/project/inflect/)

# Data Augmentation

- Data Augmentation in ASR in invaluable. To save training time, it is recommended to pre-process the dataset offline for a one-time preprocessing cost and then train the dataset on this augmented training set.
- for example, processing a single sample involves:
  - Speed perturbation
  - Time stretch perturbation (sample level)
  - Noise perturbation
  - Impulse perturbation
  - Time stretch augmentation (batch level, neural module)
- [tutorial](https://github.com/NVIDIA/NeMo/blob/stable/tutorials/asr/Online_Noise_Augmentation.ipynb)

# Speech Data Explorer [link](https://github.com/NVIDIA/NeMo/tree/stable/tools/speech_data_explorer)

- It's a Dash-based tool for interactive exploration of ASR/TTS datasets
- It collects:
  - dataset statistics (alphabet, vocabulary, and duration-based histograms)
  - navigation across dataset (sorting and filtering)
  - inspection of individual utterances (waveform, spectrogram and audio player)
  - error analysis (WER, character error rate, word match rate, mean word accuracy, and diff)

# Efficient training with NeMo

## using mixed precision

- it accelerates training speed while protecting against noticeable loss. `Tensor cores` is a specific hardware unit that comes starting with the Volta and Turing architectures to accelerate large matrix to matrix multiply-add operations by operating them on half precision inputs and returning the result in full precision.
- NNs which usually  use massix matmuls can be sped up with mixed precision and `Tensor Cores`. However, some NNs are more sensitive than others. `Apex AMP` is an NVIDIA library that maximize the benefit of mixed precision and Tensor Cores usage for a given network.

## Multi-GPU training

- it can reduce the training time by distributing the workload onto multiple compute instances.
- difference multi-GPU/multi-node: multi-node is an abstraction of multi-GPU training, which requires a distributed compute cluster, where each node can have multiple GPUs. Multi-node training is needed to scale training beyond a single node to  large amounts of GPUs.
  
# FAQ

- Sample rate for ASR: the released models are based on 16kHz audio, therefore, ensure you use models with 16kHz audio. Also you have to match the compression and the frequency.   
- Replace the 6-gram out of the ASR model with a custom LM? LMs supported by Nemo: 
  - Nemo's Beam search decoder with Levenberg-Marquadt(LM) neural module supports the KenLM language model.
    - You should retrain the KenLM language model on your own dataset. [KenLM doc](https://github.com/kpu/kenlm#kenlm)
    - if you want to use a different LM , you will need to implement a corresponding decoder module

- How to use TTS synthesis:
  - obtain speech data ideally at 22050kHz or alternatively at a higher sample rate and then downsample to 22050kHz
  - For the amount of data the more is better, and the more diverse in terms of phonemes the better. Aim for around 20hours of speech after filtering for silences and non-speech audio 