# Dataset Maker for so-vits-svc
# by Divinity

# Cuts audio in folder (next to script) into
# a training set for so-vits-svc (/dataset/raw/name)
# in whatever location you want.

# Tip: put the script on your so-vits-svc folder so you don't have
# to set path or move the files into there

# How to use:
# on CMD in the script's folder enter (<> is an argument or option, () optional):
# main.py <file path or file name> <dataset name> (-f <set folder>) (-r <remove source file>)  

# and Thanks to pydub and click for making this possible

import pydub, os, click

@click.command()
@click.argument('file_path') # or file name for an audio file inside the script's folder
@click.argument('set_name')
@click.option('set_nest_folder', '-f', default='', help='Where to put: /dataset_raw/<set_name>/')
@click.option('remove_source', '-r', is_flag=True)

def slice_audio(file_path, set_name, set_nest_folder, remove_source = False, ):
    if set_nest_folder == '':
        set_nest_folder = os.path.dirname(__file__)
    PATH_TO_SET = (set_nest_folder + '\\dataset_raw\\' + set_name + '\\')

    click.echo("Processing...")  
    extension = file_path.split('.')[1]
    audio_file = pydub.AudioSegment.from_file(file_path, extension)

    if os.path.exists(set_nest_folder + '\\dataset_raw\\') == False:
        os.mkdir(set_nest_folder + '\\dataset_raw\\')
        click.echo("Created the 'dataset_raw' folder.")
    if os.path.exists(set_nest_folder + PATH_TO_SET) == False:
        os.mkdir(PATH_TO_SET)
        click.echo(f"Created the {set_name} folders.")

    slices = audio_file[::10 * 1000]
    for i, slice in enumerate(slices):
        slice.export(f'{PATH_TO_SET}{set_name}-slice{i}.wav')
        click.echo('Slice #{0} of {1} saved.'.format(i, enumerate(slices)))
    
    if remove_source:
        os.remove(file_path)
        click.echo("Removed source file.")

    click.echo("Finished.")

if __name__ == "__main__":
    slice_audio() # type: ignore
