# AI2619 Programming Assignment \#4

*Author: Kunologist*

## Entry

The main content is in `main.ipynb`. Please refer to the instructions inside.

## Others

- The `results` folder contains the output images.
- The `audio` folder contains `source.wav` (input) and all output sound files.
- The `main.pdf` file is the PDF version of the notebook.

## Evaluation

You may want to re-run the code with your own choice of song. To do this, simply replace `source.wav` with your own song, and run through the whole notebook to wait for file generation. If you'd like to get the meta information correct, dive in `main.ipynb` and edit the `audio_meta`.

The project folder has the following structure before running:

```
.
├── audio
│   └── source.wav
├── equalizer.py
├── main.ipynb
└── your_code.py
```

After running `main.ipynb`, the working tree should look like:

```
.
├── audio
│   ├── downsampled_10000.wav
│   ├── downsampled_15000.wav
│   ├── downsampled_5000_linear.wav
│   ├── downsampled_5000.wav
│   ├── highcut.wav
│   ├── readme.md
│   ├── source_arr_downsampled_10000.pkl
│   ├── source_arr_downsampled_10000.wav
│   ├── source_arr_downsampled_15000.pkl
│   ├── source_arr_downsampled_15000.wav
│   ├── source_arr_downsampled_5000_linear.wav
│   ├── source_arr_downsampled_5000.pkl
│   ├── source_arr_downsampled_5000.wav
│   ├── source.pkl
│   ├── source.wav
│   ├── upsampled_10000.wav
│   ├── upsampled_15000.wav
│   ├── upsampled_5000.wav
│   └── vocal_enhancer.wav
├── equalizer.py
├── your_code.py
├── main.ipynb
└── results
    ├── downsampled-spectrum.png
    ├── original-spectrogram.png
    ├── original-waveform.png
    ├── upsampled-spectrum.png
    └── upsampled-waveforms.png
```

To use the equalizer, simply import the module from `equalizer.py`. This file is the same as the one in `main.ipynb`. It is intended to be used as a module, and therefore cannot be run as a script. It's a pity the module is not documented so well, please refer to the code for more information.
