# installing OS-specific dependencies
sudo apt update && sudo apt install ffmpeg
# installing pytorch
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidi
# installing whisper
pip install git+https://github.com/openai/whisper.git -q

