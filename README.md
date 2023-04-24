# Dataset Maker for so-vits-svc
by Divinity

Cuts audio in folder (next to script) into
a training set for so-vits-svc (/dataset/dataset/raw/name)
in whatever location you want.
This also works on pre-existing directories
The audio slices are exported as .wav files ready for so-vits-svc training

Tip: put the script on your so-vits-svc folder so you don't have
to set path or move the files into there

# How to use:
On CMD in the script's folder enter ([] is an argument or option, () optional):

svc-dataset-maker.py [file path or file name] [dataset name] (-f [set folder]) (-r [remove source file])  

Thanks to pydub and click for making this possible
