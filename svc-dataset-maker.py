# Dataset Maker for so-vits-svc
# by Divinity

# Cuts audio in folder (next to script) into
# a training set for so-vits-svc (/dataset_raw/name/sub set name)
# in whatever location you want. (also works on pre-existing directories)
# The audio slices are exported as .wav files ready for so-vits-svc training.

# Tip: put the script on your so-vits-svc folder so you don't have
# to set path or move the files into there

# How to use:
# on CMD in the script's folder enter ([] is an argument or option, () optional):
# svc-dataset-maker.py [file path or file name] [dataset name] (-f [set folder]) (-s [sub set folder name]) (-r [remove source file])  

# Thanks to pydub and click for making this possible

import pydub, os, click

@click.command()
@click.argument('file_path') # or file name for an audio file inside the script's folder
@click.argument('set_name')
@click.option('set_nest_folder', '-f', default='', help='Where to put: /dataset_raw/<set_name>/')
@click.option('sub_set_name', '-s', default='', help='Sub set folder name: in /dataset_raw/<set_name>/<sub_set_name>')
@click.option('remove_source', '-r', is_flag=True)

def slice_audio(file_path, set_name, set_nest_folder, sub_set_name, remove_source):
    if set_nest_folder == '':
        set_nest_folder = os.path.dirname(__file__)
    path_to_set = (set_nest_folder + '\\dataset_raw\\' + set_name + '\\')

    click.echo("Processing...")  
    extension = file_path.split('.')[1]
    audio_file = pydub.AudioSegment.from_file(file_path, extension)

    if os.path.exists(set_nest_folder + '\\dataset_raw\\') == False:
        os.mkdir(set_nest_folder + '\\dataset_raw\\')
        click.echo("Created the 'dataset_raw' folder.")
    if os.path.exists(path_to_set) == False:
        os.mkdir(path_to_set)
        click.echo(f"Created the {set_name} folder.")
        
    if sub_set_name != '':
        path_to_set += sub_set_name + '\\'
        if os.path.exists(path_to_set) == False:
            os.mkdir(path_to_set)
            click.echo(f"Created the {sub_set_name} folder.")

    slices = audio_file[::10 * 1000]
    for i, slice in enumerate(slices):
        slice.export(f'{path_to_set}{set_name}-{sub_set_name}-slice{i}.wav')
        click.echo('Slice #{0} of {1} saved.'.format(i, enumerate(slices)))
    
    if remove_source:
        os.remove(file_path)
        click.echo("Removed source file.")

    click.echo("Finished.")

if __name__ == "__main__":
    slice_audio() # type: ignore
