import os
import kuntur as kt
import matplotlib.pyplot as plt
from kuntur.plots.audio import plot_spectrogram


def main() -> None:
    files = kt.get_dir_files("audio", ext=".wav", recursive=True)

    for file in files:
        # NOTE: Use first channel if comes from webmushra
        audio, fs = kt.read_audio(file, fs=True)
        audio = audio[0:1, ...]
        fig = plot_spectrogram(
            audio[:, int(fs * 0.25):-int(fs * 0.125)],
            fs=fs,
            fft_size=2048,
            hop_size=1024,
            fig_size=(5, 4),
            dpi=300,
            font_kwargs={"fontsize": 14}
        )
        output_file = file.replace("audio", "img").replace(".wav", ".svg")
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        plt.savefig(output_file)


if __name__ == "__main__":
    main()
